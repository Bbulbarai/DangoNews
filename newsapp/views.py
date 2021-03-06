
from django.shortcuts import render, redirect
from .forms import hereglegch_burtgeh, event_add
from .models import  User_model, News, Event
from django.core.mail import send_mail
from django.http import HttpResponse
# from .forms import UploadFileForm
# from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.signing import Signer
import random

# Create your views here.
def index(request):
    return render(request, 'newsapp/index.html')

def home(request):
    return render(request, 'newsapp/news.html')

def burtguuleh(request):
    print("ta bvrtgvvleh")
    if request.method == 'POST':
        form = hereglegch_burtgeh(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = hereglegch_burtgeh()
    return render(request, 'newsapp/burtguuleh.html', {'form':form})
 

def burtguuleh2(request):
    User_models = User_model.objects.all().order_by('-id')
   # uid = reques.Post
   # delete_user = get_object_404(User, pk=id)
   #User_model.check = True
    return render(request, 'newsapp/burtguuleh2.html', {'User_models':User_models})


def send(request, pk):
    obj = User_model.objects.get(id=pk)
    context = {'object':obj}
    # print(id)
    return render(request, 'newsapp/send.html', context)

#login hiih
def torf(request, pk):
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'

    for p in range(1):
        passwor = ''
        for c in range(8):
            pwd = random.choice(chars)
            if passwor != pwd:
                passwor += pwd

        for p in range(1):
            nass = ''
        for c in range(8):
            pwd = random.choice(chars)
            if nass != pwd:
                nass += pwd
    obj = User_model.objects.filter(id=pk)
    if request.POST.get('name'):
        name = request.POST.get('name')
    else:
        name = 'user'
    if request.POST.get('password'):
        password = request.POST.get('password')
    else:
        password = '123'
    obj.update(
        name = nass,
        password = passwor,
        check = True
    )

    email = User_model.objects.filter(id=pk).first()
    send_mail(
            'django bulbar',
            email.lastname + ' таны нэвтрэх нэр: ' + nass + '  таны нууц үг: ' + passwor,
            'bbulbarai3@gmail.com',
            [email.email],
            fail_silently=False)
    # print(id)
    return render(request, 'newsapp/news.html')

def news(request):
    Newss = News.objects.order_by('-id').filter
    return render(request, 'newsapp/news.html', {'Newss':Newss})

def news2(request, id):
    #Newss2 = News.objects.order_by('-id')
    Newss2 = News.objects.filter(id=id) #ene 2in yalgag asuuna deer filtertei bgagag
    #print(Newss2)
    return render(request, 'newsapp/news2.html',{'Newss2':Newss2})

def login(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        login = User_model.objects.filter(name=name, password=password)
        if login:
            return redirect('upload')
        else:
            return redirect('login')
    # return render(request, 'login.html', {'form2':'form2'})
    return render(request, 'newsapp/login.html', {'form2':'form2'})

def upload(request):
    return render(request, 'newsapp/upload.html')


def calendar(request):
    
    return render(request,  'newsapp/calendar.html')

def calendar2(request):
     if request.method == "POST":
         date = request.POST.get('date')
         form = event_add(request.POST)
         if form.is_valid():
            print(form)
            form.save()
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            print(title, description)

     form = event_add()
     return render(request, 'newsapp/calendar2.html', {'form':form})


# def event(request):
#     obj = event.objects.all()
#     if request.method == 'POST':
#         form = event_add(request.POST)
#     return render(request,  'newsapp/calendar2.html', {'form':form})
