from django.urls import path,include
from .views import about,contact,icons,index,single,typography,single1,wish
from users.views import SignUp

# from .views import typo


urlpatterns = [
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('icons/',icons,name='icons'),
    path('',index,name='index'),
    path('men/mens/<id>/',single,name='single'),
    path('womens/<id>/',single1,name='single1'),
    path('typography/',typography, name='typography'),
    path('signup/',SignUp.as_view(), name='signup'),
    path('wishlist/',wish, name='wishlist'),

]
