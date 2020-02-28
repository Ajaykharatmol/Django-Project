from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from myapp.models import Category,UserInfo,Products,Cart,Payment
from myapp.forms import CategoryForm,UserCreationForm

def hello(request):
    return HttpResponse("Hello World")

def Home(request):
    depts = Category.objects.all()
    return render(request,"index.html",{'depts':depts})


def login(request):
    return render(request,"LoginAndSign.html",{})

def validate(request):
    if(request.method=="POST"):
        udata = request.POST.get("uname")
        uemail = request.POST.get("uemail")
        pwd = request.POST.get("pwd")        
        result = UserInfo.objects.filter(uname=udata,uemail=uemail,password=pwd)
        if(result != None):
            request.session["uname"]=udata
            return redirect(selectCat)
        else:
            return redirect(login)


def logout(request):
        if(request.method=="POST"):
            udata = request.POST.get("uname")
            request.session["uname"]=udata
            session.pop['uname', None]
        return redirect(login)

def register(request):
    if (request.method=="POST"):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 ==  password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"")
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,"")
                
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            messages.info(request,"")
            
            return redirect("register")
        return redirect("/myapp/login")
    else:
        return render(request,"register.html")

        

    


        
        
    


def showallCat(request):
    depts = Category.objects.all()
    return render(request,"showallCat.html",{'depts':depts})


def addCat(request):
    if (request.method=="GET"):
        form  = CategoryForm()
        return render(request,'addCat.html',{"form":form})
    else:
        #save code
        form = CategoryForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(showallCat)

def delete(request,id):
    d = Category.objects.filter(id=id)
    d.delete()    
    return redirect(showallCat)


def edit(request,id):  
    if(request.method == "GET") :
        d = Category.objects.get(id=id)                
        return render(request,'edit.html',{'dept':d})
    
    elif(request.method == "POST"):
        id = request.POST.get("id")
        d = Category.objects.get(id=id) 
        form = CategoryForm(request.POST, instance = d)  
        if form.is_valid():  
            form.save()  
        return redirect(showallCat) 

def selectCat(request):
    depts = Category.objects.all()
    if(request.method=="GET"):
        return render(request,"catlist.html",{'depts':depts})
    else:
       
        id = request.POST.get("dept")
        d = Category.objects.get(id=id) 
        emps = Products.objects.filter(dept=d)    
        #return HttpResponse(emps)
        return render(request,"showMobile.html",{'depts':depts,'emps':emps})



def addtocart(request,id):  
    #Cart.objects.all().delete() 
    
    user = UserInfo.objects.get(uname=request.session["uname"])
    emp = Products.objects.get(id=id)    
    data = Cart.objects.filter(emp=emp)
    
    if(data.count()==0):
        mycart = Cart()    
        mycart.user = user
        mycart.emp = emp
        mycart.save()
    return redirect(showcart)

def showcart(request):
    user = UserInfo.objects.get(uname=request.session["uname"])
    cart_items = Cart.objects.filter(user=user.id)
    emps = []    
    total = 0
    for c in cart_items:
        e1 = Products.objects.get(id=c.emp.id)
        total = total + e1.Product_Price
        emps.append(e1)
    
    request.session["total"] = total
    print(request.session["total"])
    return render(request,"showAllMobileItems.html",{"emps" : emps,"total":total})
    
def deleteitem(request,id):
    e = Products.objects.get(id=id)
    item = Cart.objects.get(emp=e)
    item.delete()
    return redirect(showcart)

def AddItems(request):
    return redirect(selectCat)

def MakePayment(request):
    total = request.session["total"]
    return render(request,"payment.html",{"total":total})

def payment(request):
    if(request.method=="POST"):
        cardno = request.POST.get("cardno")
        cvvno =  request.POST.get("cvvno")
        expiryDate = request.POST.get("expiryDate")
        
        
        try:
            p = Payment.objects.get(cardno =cardno,cvvno=cvvno,expiryDate = expiryDate)
            print(p)
            total = request.session["total"]
            p.amount = p.amount - total
            p1 = Payment.objects.get(cardno =222,cvvno=222,expiryDate = '12/2020')
            p1.amount = p1.amount + total
            p.save()
            p1.save()
            
            return HttpResponse("Payment Received",p)
        except:
            return HttpResponse("Card Mismatch")
    
        