from django.contrib import admin

# Register your models here.


# Register your models here.

from myapp.models import Category,UserInfo,Products,Cart,Payment

class CategoryAdmin(admin.ModelAdmin):
    pass

class UserInfoAdmin(admin.ModelAdmin):
    pass

class ProductsAdmin(admin.ModelAdmin):
    pass

class CartAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Category,CategoryAdmin )
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Payment,PaymentAdmin)