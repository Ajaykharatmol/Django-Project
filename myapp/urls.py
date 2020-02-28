from django.urls import path
from . import views

urlpatterns = [
    
    path('hello',views.hello,name="hello"),
    path('showallCat',views.showallCat,name="showallCat"),
    path('addCat',views.addCat),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path("login",views.login),
    path("validate",views.validate),
    path("logout",views.logout),
    path("register",views.register),
    path('selectCat',views.selectCat),
    path("addtocart/<int:id>",views.addtocart),
    path("showallcartitems",views.showcart),
    path("deleteitem/<int:id>",views.deleteitem),
    path("",views.Home),
    path("AddItems",views.AddItems),
    path("MakePayment",views.MakePayment),
   path("payment",views.payment),
    ]

