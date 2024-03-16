from django.http import HttpRequest
from products.models import Product

class Cart:
    def __init__(self, request: HttpRequest):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
            # cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product, quantity=1):
        product_id = str(product)
        # if product_id in self.cart:
        #    self.cart[product_id]['quantity'] -= quantity
        # else:
        if product_id in self.cart:
           del self.cart[product_id]

        self.save()

    def update(self, product, quantity=1):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.save()

    def __iter__(self):
        cart = self.cart.copy()
        product_ids = cart.keys()

        product_objs = Product.objects.filter(pk__in=product_ids)

        for obj in product_objs:
            cart[str(obj.pk)]['obj'] = obj


        for item in cart.values():
            if item.get('obj') is not None:
                yield item

    def len(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        # total_price = 0
        products = Product.objects.filter(pk__in=self.cart.keys())

        return sum(product.price*self.cart[str(product.pk)]['quantity'] for product in products)

    def save(self):
        self.session.modified = True

