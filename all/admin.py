from django.contrib import admin

from .models import *

admin.site.register(Cat),
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Size)
admin.site.register(Color)