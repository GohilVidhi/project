"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('about',views.about,name="about"),
    
    
    
    path('delete_address/<int:id>',views.delete_address,name="delete_address"),
    path('edit_address/<int:id>',views.edit_address,name="edit_address"),
    
    
    path('address',views.address,name="address"),
    path('billing_details',views.billing_details,name="billing_details"),
    path('cart',views.cart,name="cart"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('contact',views.contact,name="contact"),
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('log_out',views.log_out,name="log_out"),
    path('check_login',views.check_login,name="check_login"),
    path('orders',views.orders,name="orders"),
    path('profile',views.profile,name="profile"),
    path('register',views.register,name="register"),
    path('add_user',views.add_user,name="add_user"),
    path('reset_password',views.reset_password,name="reset_password"),
    path('otp_generate',views.otp_generate,name="otp_generate"),
    path('check_otp',views.check_otp,name="check_otp"),
    path('wishlist/<int:id>',views.wishlist,name="wishlist"),
    path('search',views.search,name="search"),
    path('shop_grid',views.shop_grid,name="shop_grid"),
    path('product_details',views.product_details,name="product_details"),
    path('product_details1/<int:id>',views.product_details1,name="product_details1"),
    path('blog_post',views.blog_post,name="blog_post"),
    path('blog_read',views.blog_read,name="blog_read"),
    
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('change_password',views.change_password,name="change_password"),
    
    path('cate_url',views.cate_url,name="cate_url"),
    path('price_filter',views.price_filter,name="price_filter"),
    path('product_color',views.product_color,name="product_color"),
    # path('cart_plus/<int:id>/', views.cart_plus, name='cart_plus'),
    # path('cart_mines/<int:id>/', views.cart_mines, name='cart_mines'),
    
    path('add_to_cart/<int:id>/', views.single_add_to_cart, name='single_add_to_cart'),
    
    
    path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
    
    path('show_Wishlist',views.show_Wishlist,name='show_Wishlist'),
    path('delete_Wishlist/<int:id>',views.delete_Wishlist,name='delete_Wishlist'),
    
    path('cart_quantity_update',views.cart_quantity_update,name='cart_quantity_update'),
    path('apply_coupon',views.apply_coupon,name='apply_coupon'),
    path('add_address',views.add_address,name='add_address'),
    path('create_rating', views.create_rating, name='create_rating'),
    path('add_like/<int:id>', views.add_like, name='add_like'),
    path('remove_dislike/<int:id>', views.remove_dislike, name='remove_dislike'),

]
