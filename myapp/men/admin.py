from django.contrib import admin
from .models import product,payment,wishlist,new_review
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ['catagories','img','product_name','product_type','pri','size','price_choice']
    list_filter = ['catagories','img','product_name','product_type','pri','size','price_choice']

class paymentAdmin(admin.ModelAdmin):
    list_display = ['paytype','bank_name']
    list_filter = ['paytype','bank_name']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_type','pri']
    list_filter = ['product_name','product_type','pri']

class new_reviewAdmin(admin.ModelAdmin):
    list_display = ['star']




admin.site.register(product,productAdmin)
admin.site.register(payment,paymentAdmin)
admin.site.register(new_review,new_reviewAdmin)
admin.site.register(wishlist,wishlistAdmin)