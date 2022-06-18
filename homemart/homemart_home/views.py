from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import sqlite3

from .forms import PostForm,cartelements
from .models import *
# Create your views here.
name="404"
phone="404_error"
count=0
shopid = "DMB"


def register(request):
    postform=PostForm(request.POST)
    if 'login' in request.POST:
        global phone
        phone = request.POST.get("log_phone")
        password = request.POST["log_pass"]
        try:
                 conn=sqlite3.connect("db.sqlite3")
        except sqlite3.Error as e:
             print(e)
        cur=conn.cursor()
        cur.execute('SELECT * FROM homemart_home_for_registration WHERE phone_nu=? and password=?',(phone,password))
        rows=cur.fetchall()
        if len(rows)==0:
            messages.error(request,"Please Check your phone nu or password!")
            return redirect('login')
        else:
           global name
           name=rows[0][1]
           print(name)
           param={'phone':phone,'name':name}
           return render(request,'index.html',param)
    elif 'cre' in request.POST:
        post=for_registration()
        post.name=request.POST.get("firstname")
        post.password = request.POST.get("pass")
        match_password= request.POST.get("match_pass")
        post.phone_nu = request.POST.get("phone_no")
        post.loc = request.POST.get("loc")
        if not post.password or not post.phone_nu or not post.name or not post.loc:
            messages.error(request, f"please fill all fields.")
            return redirect('login')
        elif match_password != post.password:
            messages.info(request, f"passwords did not match.")
            return redirect('login')
        elif postform.is_valid():
            post.save()
            #return HttpResponseRedirect("")
            messages.success(request,"Conguratulations, Account has been created!")
            return redirect('Home')
        else:
            return redirect('login')
    else:
        return render(request,"login.html")


def forgotten(request):
    return render(request,"forgetp.html")

def staples(request):
    prod=Product.objects.all()
    try:
        conn = sqlite3.connect("db.sqlite3")
    except sqlite3.Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute(
        'select DISTINCT p.cartid  from homemart_home_product as p,homemart_home_cart as cart,homemart_home_for_registration as login where cart.Cartid=p.Cartid and cart.phone_no=?;',
        (phone,))
    row2 = cur.fetchall()
    global count
    count = len(row2)
    row = list()
    naam=["Dmart","Kmart","Big Bazaar"]
    if 'Kmart' == request.POST.get('drop'):
        pos2 = 1
        pos1 = 0
        naam[pos1], naam[pos2] = naam[pos2], naam[pos1]
        cur.execute('SELECT kmart.price FROM homemart_home_product as p, homemart_home_shops as kmart WHERE kmart.cartid = p.cartid and kmart.shopid="KMB";')
        global shopid
        shopid="KMB"
    elif 'Big Bazaar'== request.POST.get('drop'):
        pos2=2
        pos1=0
        naam[pos1], naam[pos2] = naam[pos2], naam[pos1]
        cur.execute('SELECT big_b.price FROM homemart_home_product as p,homemart_home_shops as big_b WHERE big_b.cartid=p.cartid and big_b.shopid="BBB";')
        shopid="BBB"
    elif 'Dmart'== request.POST.get('drop'):
        cur.execute('SELECT dmart.price FROM homemart_home_product as p,homemart_home_shops as dmart WHERE dmart.cartid=p.cartid and dmart.shopid="DMB";')
        shopid="DMB"
    else:
        cur.execute(
            'SELECT dmart.price FROM homemart_home_product as p,homemart_home_shops as dmart WHERE dmart.cartid=p.cartid and dmart.shopid="DMB";')
    rows=cur.fetchall()
    
    
    if "cartid" in request.POST:
        post=cart()
        cartid=post.Cartid=request.POST['cartid']
        post.phone_no=phone
        post.shopid=shopid
        cur.execute('select shopname from homemart_home_shops as shop where shop.cartid=? and shop.shopid=?',(cartid,shopid,))
        shopname1=cur.fetchall()
        post.shopName=shopname1[0][0]
        post.save()
        cur.execute(
            'select DISTINCT p.cartid  from homemart_home_product as p,homemart_home_cart as cart,homemart_home_for_registration as login where cart.Cartid=p.Cartid and cart.phone_no=?;',
            (phone,))
        row2 = cur.fetchall()
    for item in rows:
        for i in item:
            row.append(i)
    zipped_product_price=zip(prod,row)
    #cart.objects.all().delete()
    count = len(row2)
    return render(request, "product_staples.html", {"count":count,'phone':phone,'name':name,'products': zipped_product_price,'naam':naam})
def search(request):
    naam = ["Dmart", "Kmart", "Big Bazaar"]
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    global count
    query= request.GET['query']
    if len(query)>71 or len(query)<1:
        product=Product.objects.none()
        params = {'products': product}
    else:
        productname = Product.objects.filter(productname__icontains=query)
        productdesc = Product.objects.filter(discription__icontains=query)
        product= productname.union(productdesc)
        if "cartid" in request.POST:
            post = cart()
            post.Cartid = request.POST['cartid']
            post.phone_no = phone
            post.save()
            cur.execute(
                'select DISTINCT p.cartid  from homemart_home_product as p,homemart_home_cart as cart,homemart_home_for_registration as login where cart.Cartid=p.Cartid and cart.phone_no=?;',
                (phone,))
            row2 = cur.fetchall()
            count = len(row2)
        print('<p id="shopval" ></p>')
        params = {"count":count,'phone':phone,'products': product,'naam':naam,"query":query,"name":name}
    return render(request, 'search.html', params)

def cartfun(request):
    naam=["Dmart","Kmart","Big Bazaar"]
    try:
        conn = sqlite3.connect("db.sqlite3")
    except sqlite3.Error as e:
        print(e)
    cur = conn.cursor()
    if request.method=='POST':
        cur.execute(
        'select DISTINCT p.cartid  from homemart_home_product as p,homemart_home_cart as cart,homemart_home_for_registration as login where cart.Cartid=p.Cartid and cart.phone_no=?;',
        (phone,))
    row2 = cur.fetchall()
    count = len(row2)
    print(row2)
    cur.execute(
        'select DISTINCT p.productname,p.discription,p.image,p.Cartid,cart.shopName,shop.price,cart.shopid  from homemart_home_product as p,homemart_home_cart as cart,homemart_home_for_registration as login,homemart_home_shops as shop where cart.Cartid=p.Cartid and cart.Cartid=shop.cartid and shop.shopid=cart.shopid and cart.phone_no=?;',
        (phone,))
    product=cur.fetchall()
    #print(product[0])
    return render(request,'cart.html',{'products':product,'count':count,'phone':phone,'name':name,'naam':naam})
def order_confirm(request):
    return render(request,'order_confirmation.html')