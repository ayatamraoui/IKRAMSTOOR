from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Cat,Product,Customer,User,Order



class CatFrom(ModelForm):
    class Meta:
        model = Cat
        fields = "__all__"


class ProductFrom(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class OrdersFrom(ModelForm):
    class Meta:
        model = Order
        fields = ['status']
