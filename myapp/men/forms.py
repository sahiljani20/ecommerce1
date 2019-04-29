
from django import forms
from .models import wishlist


# class Postview(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields='__all__'



class wishlistform(forms.ModelForm):

    class Meta:
        model= wishlist
        fields= ['product_name','product_type','catagories','pri','size','disc']