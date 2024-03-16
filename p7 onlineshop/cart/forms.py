from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,
                                  widget=forms.NumberInput(attrs={'class':'quantity-input',
                                                                  'name' : "qty",
                                                                    'id' : "qty",
                                                                  'value':'1'}),label='')


