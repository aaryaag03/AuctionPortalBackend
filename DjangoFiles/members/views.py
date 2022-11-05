from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users,ItemsOnBid
import hashlib
from requests import Session
import json
from django.contrib.auth.hashers import make_password, check_password

hashed_pwd = make_password("plain_text")
check_password("plain_text",hashed_pwd)

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def clientLogin(request):
    template=loader.get_template('cl.html')
    return HttpResponse(template.render({},request))

def clientRegister(request):
    template=loader.get_template('cr.html')
    return HttpResponse(template.render({},request))

def clientRegistered(request):
    client_username=request.POST['username']
    client_password=request.POST['password']
    hashed_client_password=make_password(client_password)
    client_email=request.POST['email']
    client_confirm_password=request.POST['confirm_password']

    for x in Users.objects.all().values():
        if(x['username']==client_username):
            return HttpResponse("Username taken")

    if(client_confirm_password!=client_password):
            return HttpResponse("Passwords do not match")

    user=Users(username=client_username, role='0',password=hashed_client_password,balance=0,email=client_email)
    user.save()
    return HttpResponseRedirect(reverse('clientLogin'))

def clientLoggedIn(request):
    
    client_username=request.POST['username']
    client_password=request.POST['password']
    clients=Users.objects.filter(username=client_username).values()
    if(len(clients)==0):
        return HttpResponse("Username does not exist")

    saved_hashed_password = clients[0]['password']
    saved_role=clients[0]['role']
    
    if(saved_role!=0):
        return HttpResponse("Not a valid client!")
    if(check_password(client_password,saved_hashed_password)!=True):
        return HttpResponse("Wrong password!") 
    template=loader.get_template('chome.html')
    context={
        'client':clients[0]
        # more to be added
    }
    return HttpResponse(template.render(context,request))

def adminLogin(request):
    template=loader.get_template('al.html')
    return HttpResponse(template.render({},request))

def adminRegister(request):
    template=loader.get_template('ar.html')
    return HttpResponse(template.render({},request))

def adminRegistered(request):
    admin_username=request.POST['username']
    admin_password=request.POST['password']
    hashed_admin_password=make_password(admin_password)
    admin_email=request.POST['email']
    admin_confirm_password=request.POST['confirm_password']

    for x in Users.objects.all().values():
        if(x['username']==admin_username):
            return HttpResponse("Username taken")

    if(admin_confirm_password!=admin_password):
            return HttpResponse("Passwords do not match")

    user=Users(username=admin_username, role='1',password=hashed_admin_password,balance=0,email=admin_email)
    user.save()
    return HttpResponseRedirect(reverse('adminLogin'))

def adminLoggedIn(request):
    admin_username=request.POST['username']
    admin_password=request.POST['password']
    admins=Users.objects.filter(username=admin_username).values()
    if(len(admins)==0):
        return HttpResponse("Username does not exist")

    saved_hashed_password = admins[0]['password']
    saved_role=admins[0]['role']
    if(saved_role!=1):
        return HttpResponse("Not a valid admin!")
    if(check_password(admin_password,saved_hashed_password)!=True):
        return HttpResponse("Wrong password!") 

    template=loader.get_template('ahome.html')
    context={
        'admin':admins[0]
        # more to be added
    }
    return HttpResponse(template.render(context,request))

def auctionPortalItems(request):
    items=ItemsOnBid.objects.filter(valid=1).values()
    current_username=request.POST['username']
    context={
    'items':items,
    'current_username':current_username
    }
    return render(request,'auction.html',context)

def addItem(request):
    current_username=request.POST['username']
    context={
        'current_username':current_username
    }
    return render(request,'addItem.html',context)

def itemAdded(request):
    item_name=request.POST['item_name']
    item_descr=request.POST['item_descr']
    item_picture=request.POST['item_picture']
    minimum_bid=request.POST['minimum_bid']
    username=request.POST['username']
    item=ItemsOnBid(item_name=item_name,item_descr=item_descr,item_picture=item_picture,highest_bid=minimum_bid,highest_bidder_username=username,owner_username=username,valid='0')
    item.save()
    return HttpResponse("Request has been sent to admin")

def bidUpdate(request) :
    current_item_bid=int(request.POST['bid'])
    current_item_id=request.POST['item_id']
    current_username=request.POST['username']
    item=ItemsOnBid.objects.get(id=current_item_id)
    saved_highest_bid=item.highest_bid
    if(current_item_bid>saved_highest_bid) :
        item.highest_bid=current_item_bid
        item.highest_bidder_username=current_username
        item.save() 
        return HttpResponse("Bid UPDATED")
    return HttpResponse("Bid not ACCEPTED")

def bidRequest(request) :
    items=ItemsOnBid.objects.filter(valid=0).values()
    context={
    'items':items
    }
    return render(request,'requests.html',context)

def bidAccept(request) :
    current_item_id=request.POST['item_id']
    item=ItemsOnBid.objects.get(id=current_item_id)
    item.valid=1
    item.save()
    return HttpResponse("Item Accepetd")

def bidReject(request) :
    current_item_id=request.POST['item_id']
    item=ItemsOnBid.objects.get(id=current_item_id)
    item.delete()
    return HttpResponse("Item Deleted")

def crypto(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/category'

    parameters = {
    'id':"605e2ce9d41eae1066535f7c",
    'start':'1',
    'limit':'20',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3a23a8ef-d582-4884-8ae5-7c8acaaf56a7',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    json_data = json.loads(response.text)
    with open("data_file.json", "w") as write_file:
        json.dump(json_data, write_file, indent=4)
    newdata=json_data['data']
    Bitcoin=newdata['coins']
    coinarray=Bitcoin[0]
    quote=coinarray['quote']
    USD=quote['USD']
    price=USD['price']
    template=loader.get_template('crypto.html')
    context={
        "nice":20,
        "pricey":price
    }
    return HttpResponse(template.render(context,request))
    