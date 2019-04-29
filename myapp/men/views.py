from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import product , wishlist
from .forms import wishlistform

# from .forms import Postview
# from .models import Post

# Create your views here.
# def upload(request):
#     # if request.method =="GET":
#     #     form=Postview()
#     #     return render(request,'image.html',{'form':form})
    
#     if request.method == 'POST':
#         form = Postview(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

#         obj = Post.objects.all()
#         return render(request,'image1.html',{'obj':obj})
#     else:
#         form=Postview()
#         return render(request,'image.html',{'form':form})

# Create your views here.


def mens(request):

     p = product.objects.all()
     name = product.objects.all()
     # price = product.objects.all()
     # dis = product.objects.all()


     # if(price>0):
     #      c = ( price * dis )/100
     #      d = price-c 
     # else:
     #      d = price
     form = wishlistform(request.POST)
     if form.is_valid(): 
          form.save()
          return redirect("show/")
     


     return render(request,'mens.html',{'name':name,'pid' : p ,'form':form})



def test(request):
     p = product.objects.all()
     return render(request,'mens.html',{'pid' : p })
    
def show(request):
     wish = wishlist.objects.all()
     return render(request,'show.html',{ 'wish' : wish  })


def edit(request, id):  
    employee = wishlist.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    i = wishlist.objects.get(id=id)
    employee = wishlist.objects.get(id=id)  
    form = wishlistform(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("show/")  
    return render(request, 'edit.html', {'form': form , 'i':i})  

def destroy(request, id):  
    employee = wishlist.objects.get(id=id)  
    employee.delete()  
    return redirect('show/')  