from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)
# basically in above logic first we have declared an list before product and then later on we have 
# seperated the unique products according to their category and then we have applied for loop in that unique list to display the products
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact= Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print(name,email,phone,desc)
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html',{'product':product[0]})
# in above render we have sended product[0] bcoz product is an list so we cant send product

def checkout(request):
    if request.method=="POST":  
        items_json=request.POST.get('iemsJson', '')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone','')
        order=Order(items_json=items_json, name=name, email=email,address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed.")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

