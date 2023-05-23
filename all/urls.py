from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="home"),
    
    path('cat/',views.cats, name="cats"),
    path('create',views.create, name="create"),
    path('update/<str:pk>',views.update, name="update"),
    path('delete/<str:pk>',views.delete, name="delete"),
   
    path('show/<str:pk>',views.show, name="show"),

    
    path('register/',views.register, name="register"),
    path('login/',views.userlogin, name="login"),
    path('logout/',views.userLogout, name="logout"),

    path('product/',views.products, name="products"),
    path('create_Product',views.create_Product, name="create_Product"),
    path('update_Product/<str:pk>',views.update_Product, name="update_Product"),
    path('delete_Product/<str:pk>',views.delete_Product, name="delete_Product"),
    
    path('detailProduct/<str:pk>',views.detailProduct, name="detailProduct"),

    
    path('createOrder/<str:pk>/',views.createOrder, name="createOrder"),
    path('delete_Orders/<str:pk>',views.delete_Orders, name="delete_Orders"),
    path('showOrder',views.showOrder, name="showOrder"),

    path('showCats/',views.showCats, name="showCats"),
    path('showProduct/',views.showProduct, name="showProduct"),

    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),


    path('escpasAdmin',views.escpasAdmin, name="escpasAdmin"),

    path('escpasAdminProduct',views.escpasAdminProduct, name="escpasAdminProduct"),

    path('escpasAdminOrder',views.escpasAdminOrder, name="escpasAdminOrder"),
    path('escpasAdminUsers',views.escpasAdminUsers, name="escpasAdminUsers"),

    path('EditOrder/<str:pk>',views.EditOrder, name="EditOrder"),
    path('showOrder',views.showOrder, name="showOrder"),



   
]  

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)