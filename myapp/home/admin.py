from django.contrib import admin
from .models import login,wishlist,discount,rating,contacts
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin




# Register your models here.


class loginAdmin(admin.ModelAdmin):
    list_display = ['user_name','password']
    list_filter = ['user_name','password',]

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['product_name','quantity']
    list_filter = ['product_name','quantity']

class discountAdmin(admin.ModelAdmin):
    list_display = ['product_name','percentage']
    list_filter = ['product_name','percentage']

class ratingAdmin(admin.ModelAdmin):
    list_display = ['star']
    list_filter = ['star']

class contactsAdmin(admin.ModelAdmin):
    list_display = ['Name','Subject','Email']
    list_filter = ['Name','Subject','Email']


admin.site.register(login,loginAdmin)
admin.site.register(wishlist,wishlistAdmin)
admin.site.register(discount,discountAdmin)
admin.site.register(rating,ratingAdmin)
admin.site.register(contacts,contactsAdmin)