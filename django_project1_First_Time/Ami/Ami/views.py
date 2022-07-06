from distutils.log import info

from xml.dom.minidom import Document
from django import urls
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render,redirect
from numpy import outer







# def Home(request):
#      INFO ={}
     
#      try:
#           ms=request.GET.get('names'),
#           msg=request.GET.get('passwrd')
          
#           INFO ={
#              'title':"Home page",
#              'Pagename':[1,2,5,3],
#              "area" :"Music",
#              'tabless':[{"name":ms,'age':msg,}],
#              "details":[{'name':'rohit','Sir':'vishwakrma',"music":'arijit'}]  
#          }

        
#      except :
#           pass
#           return HttpResponseRedirect('/come')
          
#      return render(request,'homepage.html',INFO)



#----------wellcome page Function------------
from django.http import HttpResponse

def welcome(request):
#     return HttpResponse('<h1>Hello HttpResponse</h1>') 
     if request.method=='GET':
          one = request.GET.get('num1')
          one2 = request.GET.get('num2')
          # s = one+one2
          final = {
               'heading':"1 st Page ",
               "user_input":[{'n':one,'p':one2}],
               "title":'First Page'      
          }
     
     return render(request,'welcomepage.html',final)


     
 
# ------------------First page funtion-----------------
def fpage(request):
     try:
          if request.method=='GET':
               one = request.GET.get('num1')
               one2 = request.GET.get('num2')
               # s = one+one2
               final = {
                    'heading':"1 st Page ",
                    "user_input":[{'n':one,'p':one2}],
                    "title":'First Page'      
               }
     
               
     except:
          pass
     return render (request,'fpage.html',final)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     

def RichHome(request):
     return render(request,'rich.html')

#-----------Secound page function---------------
def spage(request):
           
     return render (request,'spage.html')

# #-----------fout page  page function------------
def fourpage(request):
     return render (request,'fourpage.html')

# #-----------third page function-----------------
def tpage(request):
     return render (request,'tpage.html')

# #---------Swelcome  font page function-------------



# from django.http import HttpResponse
# from django.template import loader


# def testing(request):
#   mymembers = Members.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'members': mymembers,
#   }
#   return HttpResponse(template.render(context, request))  




from django.shortcuts import render
from .form import InputForm




# ---------------------------#exmple-------------------------------
 
# Create your views here.
# def home_view(request):
#      fn = InputForm()
     
     
   
#      if request.method=='GET':
#           one = request.GET.get('num1')
#           one2 = request.GET.get('num2')
          
#           final = {
#                'heading':"1 st Page ",
#                "user_input":[{'a':one,'b':one2}],
#                "title":'First Page',
#                'data':fn
               
#           }
     
#           return render(request, "homes.html",final)  


    #--------------------------------------exmpleee---------------------------
    
    
    
    
def home_view(request):
     fn = InputForm
     if request.method == "GET":
          aa = request.GET.get('nu')
          bb = request.GET.get('num')
          
               
     
     deta = {
          'user':[{'z':aa,'x':bb}],
          'info':fn
     }
     
     return render(request,'homes.html',deta)