from django.shortcuts import render
#from django.http import HttpResponse

#home_page = None
# Create your views here.
def home_page(request):
    return render(request, 'home.html')# remove: HttpResponse('<html><title>To-Do lists</title></html>') #test result = "false is not true"
    #render built into django
    #tell it which file we want to use
