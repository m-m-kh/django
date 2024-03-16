from django import  template

register = template.Library()

@register.filter
def price(value:str):
    print(value)
    value = f'{value:,}'
    value = list(str(value))

    # print(value)
    nums = {
        '0':'۰',
        '1':'١',
        '2':'٢',
        '3':'۳',
        '4':'۴',
        '5':'۵',
        '6':'۶',
        '7':'۷',
        '8':'۸',
        '9':'۹',

    }
    value = ''.join(map(lambda x:nums.get(x,','), value))

    return value

@register.filter
def active_comments(comments):
    return comments.filter(text='fawfkwknl')
@register.filter
def multi(price, quantity):
    return int(price) * int(quantity)

