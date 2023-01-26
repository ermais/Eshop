from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Fieldset,ButtonHolder,Submit,Field

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.NumberInput)

class UpdateCartForm(forms.Form):
    product = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(widget=forms.NumberInput)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        product = kwargs['initial']['product']
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
            '',
            Field('quantity',css_class=f"item-{product}"),
            'product'
            ),
            
        )
