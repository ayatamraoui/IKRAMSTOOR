from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import CatFrom,ProductFrom,CustomerForm,OrdersFrom
from django.forms import inlineformset_factory
import os
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from .decorators import notLoggedUsers,allowedUsers,forAdmins
from django.contrib.auth.models import Group


# Create your views here.
def home(requset):
    cats = Cat.objects.all()
    catsNav = Cat.objects.all()[:6]
    products = Product.objects.all()#[:10]
    # out_orders = Order.objects.all().count()
    # customer = requset.user.customer
    # order_count = Order.objects.filter(customer=customer).count()
    context = {'cats':cats,'products':products,'catsNav':catsNav}
    return render(requset,"all/home.html", context)


def show(requset,pk):
    cat = Cat.objects.get(id=pk)
    cats = Cat.objects.all()
    Products = Product.objects.all()
    products = Products.filter(nameCat=cat)
    context = {
               'products':products,'cats':cats}
    return render(requset,"all/shop.html", context)


def create(request):
    #form = CatFrom()
    if request.method == 'POST':
         cat = Cat()
         cat.name = request.POST.get('name')
         #print(request.POST)
         #form = CatFrom(request.POST)
         if len(request.FILES) != 0:
             cat.avatar = request.FILES['avatar']
             cat.save()
             return redirect('cats')
    
    return render(request,"all/createCat.html"  )



def cats(request):
    cats = Cat.objects.all()
    return render(request,"all/cat.html" , {'cats': cats})


def update(request,pk):
    cat = Cat.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(cat.avatar) > 0:
                os.remove(cat.avatar.path)
            cat.avatar = request.FILES['avatar']
        cat.name = request.POST.get('name')
       
        cat.save()
        return redirect('cats')
    context = {'cat':cat}
    return render(request,"all/updateCat.html" , context )


def delete(request,pk):
    cat = Cat.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('cats')
    context = {'cat':cat}
    return render(request,"all/delete_form.html" , context )



def products(request):
    products = Product.objects.all()
    cats = Cat.objects.all()
    return render(request,"all/product.html" , {'products': products,'cats':cats})



def update_Product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductFrom(instance=product)
    if request.method == 'POST':
        form = ProductFrom(request.POST, instance=product,files=request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request,"all/update_Product.html" , context )  



def delete_Product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'product':product}
    return render(request,"all/delete_Product.html" , context )



def create_Product(request):
    form = ProductFrom()
    if request.method == 'POST':
        form = ProductFrom(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request,"all/create_product.html" ,context )




def detailProduct(request,pk):
    product = Product.objects.get(id=pk)
    context = {'cats':cats,'product':product}
    return render(request,"all/detailProduct.html",context)





def createOrder(request,pk):

    user = User.objects.get(username=request.user.username)
    product = Product.objects.get(id=pk)

    order = Order() 
    order.user = user
    order.Product = product
    order.status = 'Pending'

    order.save()    
    return redirect('showOrder')


@notLoggedUsers
def register(request):   
            form = CustomerForm()
            if request.method == 'POST': 
                   form = CustomerForm(request.POST)
                   if form.is_valid():
                        user = form.save()
                        username = form.cleaned_data.get('username')
                        group = Group.objects.get(name="customer")
                        user.groups.add(group)
                        messages.success(request , username + ' Created Successfully !')
                        return redirect('login')
                   else:
                          messages.error(request ,  ' invalid Recaptcha please try again!')  
 
        
            context = {'form':form}

            return render(request , 'all/register.html', context )


@notLoggedUsers
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'email or password is not valid')

    context = {}
    return render(request,"all/login.html", context)
    


@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
# @forAdmins
def dashboard(request):
    return render(request,"all/dashboard.html")



def userLogout(request):
   logout(request)
   return redirect('home')




def delete_Orders(request,pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('showOrder')
    context = {'orders':orders}
    return render(request,"all/delete_Orders.html" , context )

#code mohamedgg


def showOrder(request):
    user = User.objects.get(username=request.user.username)
    Orders = Order.objects.filter(user=user)
    order_count = Order.objects.filter(user=user).count()
    return render(request,"all/showOrder.html",{'Orders': Orders,'order_count':order_count})


def showCats(request):
    cats = Cat.objects.all()
    out_orders = Order.objects.all().count()
    # user = User.objects.get(username=request.user.username)
    # order_count = Order.objects.filter(user=user).count()
    return render(request,"all/cats.html" , {'cats': cats,'out_orders':out_orders})

def showProduct(request):
    products = Product.objects.all()
    out_orders = Order.objects.all().count()
    # user = User.objects.get(username=request.user.username)
    # order_count = Order.objects.filter(user=user).count()
    return render(request,"all/products.html" , {'products': products,'out_orders':out_orders})


def escpasAdmin(request):
#    Orders = Order.objects.all()
    Customers=Customer.objects.all()
    products = Product.objects.all()
    Cats = Cat.objects.all()
#    context={'Orders': Orders,'Customers': Customers,'products':products}
    out_orders = Order.objects.all().count()
    out_ordersDelivered = Order.objects.filter(status="Delivered").count()
    out_ordersPending = Order.objects.filter(status="Pending").count()
    out_ordersinprogress = Order.objects.filter(status="in progress").count()
    out_ordersoutoforder = Order.objects.filter(status="out of order").count()
    context={'out_orders': out_orders,'products':products,'Customers': Customers,'Cats':Cats,'out_ordersDelivered':out_ordersDelivered,'out_ordersPending':out_ordersPending,'out_ordersinprogress':out_ordersinprogress,'out_ordersoutoforder':out_ordersoutoforder}
    return render(request,"all/escpasAdmin.html",context)



def contact(request):
    cats = Cat.objects.all()
    out_orders = Order.objects.all().count()
    # user = User.objects.get(username=request.user.username)
    # order_count = Order.objects.filter(user=user).count()
    return render(request,"all/contact.html" , {'cats': cats,'out_orders':out_orders})

def about(request):
    cats = Cat.objects.all()
    out_orders = Order.objects.all().count()
    # user = User.objects.get(username=request.user.username)
    # order_count = Order.objects.filter(user=user).count()
    return render(request,"all/about.html" , {'cats': cats,'out_orders':out_orders})


def escpasAdminProduct(request):
#    Orders = Order.objects.all()
    Customers=Customer.objects.all()
    products = Product.objects.all()
    Cats = Cat.objects.all()
#    context={'Orders': Orders,'Customers': Customers,'products':products}
    out_orders = Order.objects.all().count()
    out_ordersDelivered = Order.objects.filter(status="Delivered").count()
    out_ordersPending = Order.objects.filter(status="Pending").count()
    out_ordersinprogress = Order.objects.filter(status="in progress").count()
    out_ordersoutoforder = Order.objects.filter(status="out of order").count()
    context={'out_orders': out_orders,'products':products,'Customers': Customers,'Cats':Cats,'out_ordersDelivered':out_ordersDelivered,'out_ordersPending':out_ordersPending,'out_ordersinprogress':out_ordersinprogress,'out_ordersoutoforder':out_ordersoutoforder}
    return render(request,"all/escpasAdminProduct.html",context)







def escpasAdminOrder(request):
    Orders = Order.objects.all()
    Customers=Customer.objects.all()
    products = Product.objects.all()
    Cats = Cat.objects.all()
#    context={'Orders': Orders,'Customers': Customers,'products':products}
    out_orders = Order.objects.all().count()
    out_ordersDelivered = Order.objects.filter(status="Delivered").count()
    out_ordersPending = Order.objects.filter(status="Pending").count()
    out_ordersinprogress = Order.objects.filter(status="in progress").count()
    out_ordersoutoforder = Order.objects.filter(status="out of order").count()
    context={'out_orders': out_orders,'products':products,'Customers': Customers,'Cats':Cats,'Orders':Orders,'out_ordersDelivered':out_ordersDelivered,'out_ordersPending':out_ordersPending,'out_ordersinprogress':out_ordersinprogress,'out_ordersoutoforder':out_ordersoutoforder}
    return render(request,"all/escpasAdminOrder.html",context)



def escpasAdminUsers(request):
    Orders = Order.objects.all()
    products = Product.objects.all()
    Cats = Cat.objects.all()
    user = User.objects.all()
#    context={'Orders': Orders,'Customers': Customers,'products':products}
    out_orders = Order.objects.all().count()
    out_ordersDelivered = Order.objects.filter(status="Delivered").count()
    out_ordersPending = Order.objects.filter(status="Pending").count()
    out_ordersinprogress = Order.objects.filter(status="in progress").count()
    out_ordersoutoforder = Order.objects.filter(status="out of order").count()
    context={'out_orders': out_orders,'products':products,'Cats':Cats,'Orders':Orders,'user':user,'out_ordersDelivered':out_ordersDelivered,'out_ordersPending':out_ordersPending,'out_ordersinprogress':out_ordersinprogress,'out_ordersoutoforder':out_ordersoutoforder}

    return render(request,"all/escpasAdminUsers.html",context)


def EditOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrdersFrom(instance=order)
    if request.method == 'POST':
        form = OrdersFrom(request.POST, instance=order, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escpasAdminOrder')
    context = {'form': form}
    return render(request, "all/update_Order.html", context)


# def showOrder(request):
#     user = User.objects.get(username=request.user.username)
#     Orders = Order.objects.filter(user=user)
#     order_count = Order.objects.filter(user=user).count()
#     return render(request,"all/showOrder.html",{'Orders': Orders,'order_count':order_count})