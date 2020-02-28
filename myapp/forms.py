from django import forms
from myapp.models import Category,UserInfo


class CategoryForm(forms.ModelForm):  
    class Meta:  
        model = Category  
        fields = "__all__"  

class UserCreationForm(forms.ModelForm):  
    class Meta:  
        model = UserInfo
        fields = "__all__"  
