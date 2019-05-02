from django.shortcuts import render
from django.http import HttpResponse
from myapp.men.models import product , wishlist , new_review
from myapp.women.models import wo_product ,wowishlist
from.forms import contactform,new_reviewform

from tkinter import *
from tkinter import messagebox

from gtts import gTTS
import os



# Create your views here.

def about(request):
    # template = 'about.html'
    tts = gTTS(text='You are succesfully logged in.', lang='en')
    tts.save("audio.mp3")
    loginsuccess=os.system("mpg321 audio.mp3")


    return render(request,'about.html',{'loginsuccess':loginsuccess })

def contact(request):
    form = contactform(request.POST)
    if form.is_valid():
        form.save()
        top = Tk()  
  
        top.geometry("1x1")      
        
        messagebox.showinfo("Contact form","Submitted completly")  
           




    return render(request,'contact.html',{ 'form' : form  })

def icons(request):
    template = 'icons.html'
    context = {}
    return render(request,template,context)

def index(request):

    name = product.objects.all()
    women = wo_product.objects.all()
    


    return render(request,'index.html',{'name': name , 'women': women})



def single(request, id):

    # new= new_review.objects.all().order_by('-product_name')
    c = range(15)
    new= new_review.objects.all()


    men = product.objects.get(id=id)
    
    form = new_reviewform(request.POST)
    if form.is_valid():
        form.save()

    return render(request,'single.html',{'men':men , 'form':form ,'new':new , 'c':c })

def single1(request, id):

    # women = wo_product.objects.get(id=id)
    women = wo_product.objects.get(id=id)
    return render(request,'single1.html',{'women':women})


def typography(request):
    template = 'typography.html'
    context = {}
    return render(request,template,context)


def wish(request):
    i = wishlist.objects.all()
    w = wowishlist.objects.all()

    return render(request,'wishlist.html',{ 'i' : i , 'w' : w })


