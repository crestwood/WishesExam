from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User,UserManager,Item


def index(request):
    return render(request, 'wishlist/index.html')

def register(request):
    print(request.POST['dateHired'])
    request.session['first_name'] = request.POST['first_name']
    request.session['user_name'] = request.POST['user_name']


    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:

        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        userid = User.objects.create(first_name = request.POST['first_name'], user_name = request.POST['user_name'], password = hashed,hireDate=request.POST['dateHired'])
        request.session['userid'] = userid.id
        request.session['first_name'] = userid.first_name
        return redirect('/dashboard')

def login(request):
    if User.objects.filter(user_name = request.POST['user_name']):
        user = User.objects.get(user_name=request.POST['user_name'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['userid'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/dashboard')


        else:
            messages.error(request, "Invalid User Name or Password")
            return redirect('/')
    else:
        messages.error(request, "Invalid User Name or Password")
        return redirect('/')    

def dashboard(request):



    user_list = Item.objects.all().filter(created_by__id__contains=request.session['userid'])
    liked_list = Item.objects.all().filter()
    allItems = Item.objects.all()
    context = {
        'user_list': user_list,
        'this_user' : User.objects.get(id=request.session['userid']),
        'allItems': allItems,
    }
    
    return render(request, 'wishlist/dashboard.html',context)


def additempage(request):
    return render(request, 'wishlist/additem.html')
def additem(request):
    errors = User.objects.itemValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/additempage')
    else:
        # current_user = request.session['user_id']
        this_user = User.objects.get(id=request.session['userid'])   
        new_item = request.POST['item_name']
        Item.objects.create(item=new_item,created_by=this_user)
        return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/') 

def showitem(request):
    item = request.POST['item']

    context = {
        'item':item,
    }
    print(request.POST['item'])
    return render(request, 'wishlist/showItem.html',context)

def addToList(request):
    this_user = User.objects.get(id=request.session['userid'])   
    this_item = Item.objects.get(id=request.POST['itemToAdd'])
    this_item.liked_by.add(this_user) 
    this_item.save() 


    return redirect('/dashboard')



