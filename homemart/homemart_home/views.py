from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import sqlite3
from .forms import PostForm
from .models import *
# Create your views here.

def register(request):
    postform=PostForm(request.POST)
    if 'login' in request.POST:
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
            messages.success(request,"conguratulations,you are successfully logged in!")
            return redirect('Home')
    elif request.method=='POST':
        post=for_registration()
        post.name=request.POST.get("firstname")
        post.password = request.POST.get("pass")
        match_password= request.POST.get("match_pass")
        post.phone_nu = request.POST.get("phone_no")
        post.loc = request.POST.get("loc")
        if not post.password or not post.phone_nu or not post.name or not post.loc:
            messages.error(request, f"please fill all fields.")
            # return HttpResponseRedirect("")
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
def Home(request):
    return render(request, "index.html")
def staples(request):
    prod=Product.objects.all()
    try:
        conn = sqlite3.connect("db.sqlite3")
    except sqlite3.Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute('SELECT dmart.price,kmart.price,big.price as p FROM homemart_home_product as p,homemart_home_d_mart_price as dmart,homemart_home_Big_bazaar_price as big,homemart_home_k_mart_price as kmart WHERE dmart.cartid=p.cartid and big.cartid=p.cartid and kmart.cartid=p.cartid and p.id=1')
    row=cur.fetchall()
    print(row)
    naam=["Dmart","Kmart","Big Bazaar"]
    return render(request, "product_staples.html", {'products': prod,'row':row,'naam':naam})
