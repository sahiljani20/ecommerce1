
from django import forms
from .models import wowishlist


# class Postview(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields='__all__'



class wishlistform(forms.ModelForm):

    class Meta:
        model= wowishlist
        fields= ['product_name','product_type','catagories','pri','size','disc']