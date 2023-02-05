from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import info
from django.template import loader
from django.urls import reverse
# from django.contrib import messages

# Create your views here.

def search(request):
    if request.method == 'POST':
        searched= request.POST.get ('search')
        re=info.objects.filter(name__contains=searched)
    return render(request,'search.html',{'searched':searched, 'items':re})

    # else:
    #     return render(request,'search.html')

def index(request):
    if request.method == 'POST':
        name= request.POST.get ('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        age= request.POST.get('age')
        qb =info(name=name,email=email,phone=phone,age=age)
        qb.save()
    return render(request,'index.html')

def infofg(request):
    allInfo=info.objects.all()
    # for items in allInfo:
    #     print(items.name)
    # print(allInfo)
    context={'items':allInfo}
    return render(request,'info.html',context)

def delete(request,id):
    print('dad')
    print(id)
    member = info.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('info'))

def update(request, id):
    mymember =info.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'item': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    age = request.POST.get('age')

    member = info.objects.get(id=id)

    member.name = name
    member.email= email
    member.phone= phone
    member.age= age
    member.save()

    return HttpResponseRedirect(reverse('info'))