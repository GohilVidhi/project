from django.contrib import admin
from django.http import HttpRequest
from .models import *
# Register your models here.



#change in admin panel for hide buttons:-
# class user_data(admin.ModelAdmin):
    # def has_add_permission(self, request):
    #     return  False
    
    # def has_delete_permission(self, request,obj=None):
    #     return False
    
    # def has_view_permission(self, request,obj=None):
    #     return False
 
# admin.site.register(user,user_data)

admin.site.register(user)
admin.site.register(categories)
admin.site.register(products)
admin.site.register(size)
admin.site.register(color)



admin.site.register(Addtocart)

admin.site.register(Add_Whishlist)

admin.site.register(Coupon_code)

admin.site.register(Address)
admin.site.register(Billing_Address)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(Review_like)
admin.site.register(User_coupon)





