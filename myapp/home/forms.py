from django import forms
from .models import contacts

from myapp.men.models import new_review

class contactform(forms.ModelForm):

    class Meta:
        model = contacts
        fields = ['Name','Email','Subject','Message']




class new_reviewform(forms.ModelForm):

    class Meta:
        model = new_review
        fields = ['product_name','star']