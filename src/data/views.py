from django.shortcuts import render
from .form import info1
from django import http
from django.http import HttpResponse
from .models import info
from django.core.paginator import Paginator as pg


def adddata(request):
    form = info1(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save() 
        return http.HttpResponseRedirect('')
    context={
        'form':form
    }
    return render(request, "myform.html",context)

def output(request):
    post =  info.objects.all()  
    paginator = pg(post,1)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, "fetch.html",{'post':post})



#another method

# def save_to_form(request):
#     all_info = info()
#     all_info.name = request.POST.get("name")
#     all_info.email = request.POST.get("email")
#     all_info.phone = request.POST.get("contact")
#     all_info.pic = request.POST.get("pic")
#     all_info.department = request.POST.get("department",False)
#     all_info.save()
#     return render(request,"myform1.html")






