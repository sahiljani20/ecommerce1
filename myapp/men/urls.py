from django.urls import path,include
from .views import mens,test,show,edit,destroy,update

urlpatterns = [
    path('',mens, name='mens'),
    path('id/',test, name= 'test'),
    # path('post/',views.upload,name="upload"),
    path('show/',show , name='show'),  
    path('edit/<int:id>', edit , name='edit'),  
    path('update/<int:id>', update , name='update'),  
    path('update/show/',show , name='show'),  

    path('<int:id>', destroy, name='destroy'),  

]

