from django.shortcuts import render
from django.views.generic import View
from user_app.models import Recordmodel
# Create your views here.
class Createview(View):
    def get(self,request):
        return render(request,"create.html")
    
    def post(self,request):
        print(request.POST)
        Recordmodel.objects.create(
            name = request.POST.get("name"),
            age = request.POST.get("age"),
            mark = request.POST.get("mark")
        )
        return render(request,"create.html")
    
class Readview(View):
    def get(self,request):
        read = Recordmodel.objects.all()
        return render(request,"read.html",{"read":read}) 

class Updateview(View):
    def get(self,request,**kwargs):
        update_id = kwargs.get("pk")
        update = Recordmodel.objects.get(id=update_id)
        return render(request,"update.html",{"update":update})
    
    def post(self,request,**kwargs):
        update_id = kwargs.get("pk")
        update = Recordmodel.objects.get(id=update_id)
        print(request.POST)
        update.name = request.POST.get("name")
        update.age = request.POST.get("age")
        update.mark = request.POST.get("mark")
        update.save()
        return render(request,"update.html")
    

        
    
