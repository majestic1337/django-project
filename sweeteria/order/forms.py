from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'product','adress', 'phone_num', 'username']

class OrderFormEdit(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'adress', 'phone_num', 'username']