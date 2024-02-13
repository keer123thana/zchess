from django.shortcuts import render
import zchess2.mod_chess2 as mc
def home(request):
    list1=mc.displayrows()
    
   
    
    return render(request,'zchess2/index.html',{'param1':list1})
# Create your views here.
