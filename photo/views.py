from photo.models import photos
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        title = request.POST['title']
        if file and title:
            file = photos.objects.create(image=file,title=title,user=request.user)
    Photos = photos.objects.filter(user=request.user)
    return render(request,'index.html',{'Photos':Photos})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['pass']
        user = authenticate(username=username,password=Password)
        if user:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['pass']
        print(username,Password)
        user = User.objects.create_user(username=username,password=Password)
        if user:
            return redirect('login')
    return render(request,'signup.html')