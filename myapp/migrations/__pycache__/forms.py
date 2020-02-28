from django.shortcuts import render,HttpResponse,redirect
from MyApp.models import Dept,Emp,UserInfo,Cart
from MyApp.forms import DeptForm

class DeptForm(forms.ModelForm):  
    class Meta:  
        model = Dept  
        fields = "__all__"  
