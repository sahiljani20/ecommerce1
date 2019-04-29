from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import wo_product,wowishlist
from .forms import wishlistform



# Create your views here.

def womens(request):
    
    product = wo_product.objects.all()

    form = wishlistform(request.POST)
    if form.is_valid(): 
        form.save()
        return redirect("woshow/")
    



    return render(request,'womens.html',{'product': product , 'form':form})

def woshow(request):
     wish = wowishlist.objects.all()
     return render(request,'woshow.html',{ 'wish' : wish  })


def woedit(request, id):  

    employee = wowishlist.objects.get(id=id)  
    return render(request,'woedit.html', {'employee':employee  })  

def woupdate(request, id):  
    i = wowishlist.objects.get(id=id)
    employee = wowishlist.objects.get(id=id)  
    form = wishlistform(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/women/woshow/")  
    return render(request, 'woedit.html', {'form': form , 'i':i})  

def wodestroy(request, id):  
    employee = wowishlist.objects.get(id=id)  
    employee.delete()  
    return redirect('woshow/')  

