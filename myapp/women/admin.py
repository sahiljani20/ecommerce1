from django.contrib import admin
from .models import wo_product,discount,payment,review,wowishlist
# Register your models here.

class wo_productAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_type','pri','catagories','size']
    list_filter = ['product_name','product_type','pri','catagories','size']

class discountAdmin(admin.ModelAdmin):
    list_display = ['product_name','percentage']
    list_filter = ['product_name','percentage']

class paymentAdmin(admin.ModelAdmin):
    list_display = ['product_name','paytype','bank_name']
    list_filter = ['product_name','paytype','bank_name']

class reviewAdmin(admin.ModelAdmin):
    list_display = ['product_name','star']
    list_filter = ['product_name','star']


class wowishlistAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_type','pri']
    list_filter = ['product_name','product_type','pri']


admin.site.register(wo_product,wo_productAdmin)
admin.site.register(discount,discountAdmin)
admin.site.register(payment,paymentAdmin)
admin.site.register(review,reviewAdmin)
admin.site.register(wowishlist,wowishlistAdmin)
