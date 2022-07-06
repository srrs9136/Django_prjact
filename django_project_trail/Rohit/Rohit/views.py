from distutils.log import info

from xml.dom.minidom import Document
from django import urls
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render,redirect
from numpy import outer



from django.shortcuts import render
from django.http import HttpResponse
from requests import request


from Rohit.forms import AddForm
from Rohit.forms import calForm
from Rohit.forms import AddForm

def index(request):
    if request.method =='GET':
        num = request.GET.get('a')
        num1 = request.GET.get('b')
        # file=open('ro.txt','a')
        # file.write(num)
        # file.close()
        
        Info = {
            'page': "Welcome page",
            'output':{'Name':num,'Name2':num1}
           
            }    
        
       
        return render(request,"index.html",Info)
    
    



def text(request):
    fn = AddForm()
    if request.method =='GET':
        num = request.GET.get('addend0')
        num1 = request.GET.get('addend1')
        final = num+num1    
    
    dic = {
        'data':fn,
        'out':[{'s':num,'b':num1}],
        'p':final
        
    }
    return render(request,"text.html",dic)
    
   
 


def calcu(request):
    classename = calForm()
    
    if request.method == "GET":
        aa= request.GET.get('number1')
        bb= request.GET.get('number2')
        p = sum(aa,bb)
        
    
        cl = {
            'output':classename,
            'list':[{'one':aa,'two':bb}],
            'op':classename,
            'prt':p
             
           
           
        }
    return render(request,"calculator.html",cl)