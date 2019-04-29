from django.urls import path,include
from .views import womens,woshow,woedit,woupdate,wodestroy

urlpatterns = [
    path('',womens, name='womens'),
    
    path('woshow/',woshow , name='woshow'),  
    path('woedit/<int:id>', woedit , name='woedit'),  
    path('woupdate/<int:id>/', woupdate , name='woupdate'),  
    path('woshow/',woshow , name='woshow'),  

    path('<int:id>', wodestroy, name='wodestroy'),  

]

