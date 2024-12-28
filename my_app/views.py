from django.shortcuts import render , redirect,HttpResponse
from .models import *
import random
from django.core.mail import send_mail
import requests
from django.conf import settings
from django.contrib import  messages
import razorpay
# Create your views here.


#====================index=====================
def index(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        cid = Addtocart.objects.filter(user_id=uid)
        cart_count=Addtocart.objects.filter(user_id=uid).count()  # Count Cart Item
        con={"uid":uid,"cid":cid,"cart_count":cart_count}
        return render(request,"index.html",con)
    else:
        return render(request, "login.html")
                                                                                                 
#====================search product=====================
def search(request):
    if 'email' in request.session:
        srh=request.GET.get("srh")
        print(srh)
        pid = products.objects.all()
        if request.POST:

            srh=request.POST["srh"]
            if srh:
                pid=products.objects.filter(name__icontains=srh)
                print(pid)
            con={"pid":pid,"srh":srh}
            return render(request,"shop_grid.html",con)
        else:
            return render(request,"search.html")
            
    else:
        return render(request,"login.html")
#====================shop_grid=====================
def shop_grid(request):
    if 'email' in request.session:  
        uid=user.objects.get(email=request.session['email'])
        get_categories = categories.objects.all()
        pid = products.objects.all().order_by("-id")
        count = products.objects.all().count()
        
        #sorting 
        s=request.GET.get("sort")

        #cart product color change
        whishlist_product=Add_Whishlist.objects.filter(user_id=uid)
        l1=[]
        for i in whishlist_product:
            l1.append(i.product_id.id)
        #-----
        
        
        #cart product color change
        cart_item_color=Addtocart.objects.filter(user_id=uid)
        l2=[]
        for i in cart_item_color:
            l2.append(i.product_id.id)
        #-----
        
        if s=="lth":
            pid = products.objects.all().order_by("price")
        elif s=="htl":
            pid = products.objects.all().order_by('-price')
        elif s=="atz":
            pid = products.objects.all().order_by('name')
        elif s=="zta":
            pid = products.objects.all().order_by('-name')
        else:
            pid = products.objects.all().order_by("-id")
            
         
        context = {
            "get_categories": get_categories,
            "pid": pid, 
            'l1':l1,
            'count':count,"whishlist_product":whishlist_product,
            'cart_item_color':cart_item_color,'l2':l2
        }
        return render(request, "shop_grid.html", context)
    else:
         return render(request,"login.html")
     
    
#==================== click button on add_to_cart=====================
def add_to_cart(request, id):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        pid = products.objects.get(id=id)
        pcid = Addtocart.objects.filter(product_id=pid, user_id=uid).first()
        if pcid:
            pcid.quantity += 1
            pcid.total_price = pcid.quantity * pcid.price
            pcid.save()
        else:
            Addtocart.objects.create(
                product_id=pid,
                user_id=uid,
                name=pid.name,
                image=pid.image,
                price=pid.price,
                quantity=1, 
                total_price=pid.price*pid.quantity)    
        return redirect("cart")
    else:
        return redirect("cart")


    
#====================show cart details=====================

# def cart(request):
#     if "email" in request.session:
#         uid = user.objects.get(email=request.session['email'])
#         cid = Addtocart.objects.filter(user_id=uid)
#         pid = products.objects.filter(id__in=[item.product_id.id for item in cid])
#         prod = Addtocart.objects.filter(user_id=uid)
#         cart_count=Addtocart.objects.filter(user_id=uid).count()  # Count Cart Item
#         l1 = []
#         sub_total = 0
#         charge = 0
#         total_price = 0
#         discount=0
#         for i in prod:
#             a = i.quantity * i.price
#             l1.append(a)
#             sub_total = sum(l1)
#             total_price = sub_total + charge - discount
#         for i in cid:
#             print("dfsak",i.size_cart)    
         
#         con = {"uid": uid, "cid": cid, "pid": pid, "total_price": total_price, "sub_total": sub_total, "charge": charge, "cart_count":cart_count,"discount":discount}
#         return render(request, "cart.html", con)
#     else:   
#         return render(request, "login.html")

#====================product details in add to cart=====================

def single_add_to_cart(request, id):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        pid = products.objects.get(id=id)

        selected_size_id = request.POST.get('size')
        selected_color_id = request.POST.get('color')

        selected_size = size.objects.get(id=selected_size_id)
        selected_color = color.objects.get(id=selected_color_id)

        pcid = Addtocart.objects.filter(product_id=pid, user_id=uid , size_cart=selected_size,color_cart=selected_color).exists()

        if pcid:
            pcid = Addtocart.objects.get(product_id=pid, user_id=uid,size_cart=selected_size,color_cart=selected_color)
            # pcid.quantity += 1
            pcid.total_price = pcid.quantity * pcid.price
            pcid.color_cart = selected_color
            pcid.size_cart = selected_size
            pcid.save()
        else:
            Addtocart.objects.create(
                product_id=pid,
                user_id=uid,
                name=pid.name,
                image=pid.image,
                price=pid.price,
                size_cart=selected_size,
                color_cart=selected_color,
                quantity=1,
                total_price=pid.price)
        return redirect("cart")
    else:
        return render(request, "login.html")

#=============cart delete==================
def delete_cart(request,id):
    dell=Addtocart.objects.get(id=id)
    dell.delete()
    return redirect("cart")

#==============Coupon==========================
from django.utils import timezone
# def apply_coupon(request):
#     if "email" in request.session:
#         uid = user.objects.get(email=request.session['email'])
#         aid = Addtocart.objects.filter(user_id=uid)
#         l1 = []
#         sub_total = 0
#         charge = 50
#         for i in aid:
#             l1.append(i.total_price)
#         print(l1)
#         sub_total = sum(l1)
#         print("sub_total:- ", sub_total)
#         total_price = sub_total + charge
#         print("total price : ", total_price)
#         discount = 0
#         if request.POST:
#             coupon = request.POST['code']
#             print("code:- ", coupon)
#             caid = Coupon_code.objects.filter(code=coupon,one_time_use=True).exists()
#             print("coupon:-", caid)
#             if caid:
#                 cid = Coupon_code.objects.get(code=coupon)
#                 now_time = timezone.now()
#                 cid.one_time_use=False    #use coupon only one time then after false
#                 cid.save()
#                 if cid.expiry_date > now_time:
#                     total_price -= cid.discount     
#                     discount = cid.discount
#                     request.session['discount'] = discount
#                     con = {
#                         "charge": charge, "sub_total": sub_total, "uid": uid,
#                         "aid": aid, "discount": discount, "total_price": total_price}
#                     messages.info(request, "Code applied successfully")
#                     return redirect("cart")
#                 else:
#                     cid.delete()
#                     con = {
#                         "charge": charge, "sub_total": sub_total, "uid": uid, "aid": aid,
#                         "total_price": total_price, "discount": 0}
#                     messages.info(request, "Coupon has expired and has been deleted")
#                     return render(request, "cart.html", con)
#             else:
#                 con = {
#                     "charge": charge, "sub_total": sub_total, "uid": uid, "aid": aid,
#                     "total_price": total_price, "discount": 0}
#                 messages.info(request, "No discount on this code")
#                 return redirect("cart")
#         else:
#             return render(request, "cart.html")
#     else:   
#         return render(request, "login.html")

#=============product_details1 formate==================
import math
def product_details1(request,id):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        rating_show=Rating.objects.all()
        pid=products.objects.get(id=id)
        rate_id=Rating.objects.filter(product_id=pid)
        like_id=Review_like.objects.all().count()
        review_count=Rating.objects.all().count()
        l1 = []
        for i in rate_id:
            l1.append(i.rating)

        print(l1)

        if rate_id.count() > 0:
            a = sum(l1)/rate_id.count()#start count and sum: total stars/total reviews
            a=round(a,1)
            print(a)
            a1 = math.ceil(a)  # for half star
            print(a1)
            pid.rating1=a
            pid.half_rating=a1
            pid.save()
        else:
            a = 0
            a1 = 0
            print("No ratings available")
                

        con={"pid":pid,"uid":uid,"rate_id":rate_id,"review_count":review_count,"rating_show":rating_show,"l1":l1,"a":a,"a1":a1,"like_id":like_id}
        return render(request,"product_details.html",con)
    else:
        return render(request,"login.html")
#=========================
from django.urls import reverse

# def like(request, id):
#     like_id = Review_like.objects.get(id=id)
#     like_id.like += 1
#     like_id.save()
#     return redirect("product_details1")

# def dislike(request, review_id):
#     like_id = Review_like.objects.get(id=id)
#     like_id.dislike += 1
#     like_id.save()
#     return redirect("product_details1")
# def add_like(request, id):
#     like_id, created = Review_like.objects.get_or_create(id=id)
#     like_id.like += 1
#     like_id.save()
#     return redirect("product_details1")

# def remove_dislike(request, id):
#     like_id, created = Review_like.objects.get_or_create(id=id)
#     like_id.dislike += 1
#     like_id.save()
#     return redirect("product_details1")
from django.db import IntegrityError
def add_like(request, id):
    try:
        like_id, created = Review_like.objects.get_or_create(
            id=id,
            defaults={'like': 1, 'dislike': 0}  # Default values for new objects
        )
        if not created:
            like_id.like += 1
            like_id.save()
    except IntegrityError:
        return HttpResponse("An error occurred while processing your request.")
    return redirect("product_details1")

def remove_dislike(request, id):
    try:
        like_id, created = Review_like.objects.get_or_create(
            id=id,
            defaults={'like': 0, 'dislike': 1}  # Default values for new objects
        )
        if not created:
            like_id.dislike += 1
            like_id.save()
    except IntegrityError:
        return HttpResponse("An error occurred while processing your request.")
    return redirect("product_details1")
#========== shop filter categories ================
def cate_url(request): 
    if 'email' in request.session:
        catget_categories=categories.objects.all()
        pid = products.objects.all()
        c1=request.GET.getlist("option-category")
        pid=[]
        for i in c1:
            a=categories.objects.get(name=i)
            p=products.objects.filter(categories_id=a)
            pid.extend(p)

        con={"catget_categories":catget_categories,"pid":pid}

        return render(request,"shop_grid.html",con)
    else:    
        return render(request,"login.html")

#========== shop filter price_filter ================

def price_filter(request):
    if 'email' in request.session:
        catget_categories=categories.objects.all()
        pid = products.objects.all()
        if request.POST:
            min_price=request.POST["min_price"]
            max_price=request.POST["max_price"]
            
            pid=products.objects.filter(price__gte=min_price,price__lte=max_price)
            
            con={"pid":pid,"catget_categories":catget_categories}
            
            return render(request,"shop_grid.html",con)
        else:
            con={"pid":pid,"catget_categories":catget_categories}
            
            return render(request,"shop_grid.html",con)
    else:
        return render(request,"login.html")
        
#=================in cart quantity increment============
def cart_quantity_update(request):
    uid =user.objects.get(email=request.session['email'])
    if request.POST:
        quantity=request.POST['quantity']
        product_id=request.POST["product_id"]
        print(uid,quantity,product_id)
        csid=Addtocart.objects.get(user_id=uid,id=product_id)
        csid.quantity+=int(quantity)
        csid.total_price=csid.price*csid.quantity
        csid.save()
        print(csid)
    return redirect("cart")

#==================add wishlist=======================
def wishlist(request, id):
    uid = user.objects.get(email=request.session['email'])
    pid = products.objects.get(id=id)
    w_id = Add_Whishlist.objects.filter(product_id=pid, user_id=uid).first()
    a=request.GET.get('next')
        
    if w_id:
        w_id.delete()
        
        messages.info(request, "Item Removed From Your Wishlist")
    else:
        Add_Whishlist.objects.create(
            user_id=uid,
            product_id=pid,
            price=pid.price,
            dell_price=pid.del_price,
            
            name=pid.name,
            image=pid.image,)
        
        messages.info(request, "Item Saved In Your Wishlist")
    if a=="/cart":

        return redirect("cart")
    else:        
        return redirect("shop_grid")

#==================delete_Wishlist product=======================
    
def delete_Wishlist(request,id):
    dell=Add_Whishlist.objects.get(id=id)
    dell.delete()
    return redirect("show_Wishlist")

#================== show_Wishlist product=======================
def show_Wishlist(request):
    uid=user.objects.get(email=request.session['email'])
    whish=Add_Whishlist.objects.filter(user_id=uid)
    w_count=Add_Whishlist.objects.all().count()
    
    con={"uid":uid,"whish":whish,"w_count":w_count}
    return render(request,"wishlist.html",con)


#============show colors in shop page=================
def product_color(request):
    if 'email' in request.session:
        clr=request.GET.getlist('color1')
        pid = products.objects.all()
        catget_categories=categories.objects.all()
        pid=[]
        for i in clr:
            c = products.objects.filter(color=i)
            pid.extend(c)
        print(pid)
        print(c)
        context = {
            'pid': pid,
            'clr': clr,
            'catget_categories':catget_categories
        }
        print(clr)
        print(pid)
        return render(request, 'shop_grid.html', context)
    else:
        return render(request,"login.html")

#==============checkout details and payment================    
def address(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        cid = Addtocart.objects.filter(user_id=uid)
        show_address = Address.objects.all()
        cart_items = Addtocart.objects.filter(user_id=uid)
 
        l1 = []
        sub_total = 0
        charge = 50
        # discount = 0

        for i in cid:
            l1.append(i.total_price)
            sub_total = sum(l1)
            total_price = sub_total + charge
        
        # if sub_total == 0 and "discount" in request.session: 
        #     #after payment sub_total 0 then discount also 0
        #     charge = 0
        #     total_price = 0
        #     del request.session['discount']
            
        # else:
        #     charge = 50

        # if "discount" in request.session:
        #     discount = request.session.get("discount")
        #     total_price = sub_total + charge - discount
        # else:
          
            # total_price = sub_total + charge

        #Payment
        amount = max(total_price, 1) * 100
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE', '77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})
        print(response, "******")
        
        if request.method == 'POST':
            address_id = request.POST.get('address_id')

            
            print(address_id)
            if address_id:
                selected_address = Address.objects.get(id=address_id)
                
            for k in cart_items:
                
                Order.objects.create(
                order_id=response['id'],
                    user_id=uid,
                    address_id=selected_address,
                    name=k.name,
                    image=k.image,
                    price=k.price,
                    size_order = k.size_cart,
                    quantity=k.quantity,
                    total_price=k.quantity*k.price,
                    )
                k.delete() 
            return redirect('orders')
        context = {
            "show_address": show_address,
            "uid":uid,
            "cid": cid,
            "sub_total": sub_total,
            # "discount": discount,
            "charge": charge,
            "total_price": total_price,
            "response": response}
        return render(request, "address.html", context)
    else:
        return render(request, "login.html")
    
    
#=============== checkout add_address post============
def add_address(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        pincode = request.POST['pincode']
        address1 = request.POST['address1']
        town = request.POST['town']
        city = request.POST['city']
        state = request.POST['state'] 
        Address.objects.create(
            name=name, mobile=mobile, pincode=pincode,
            address1=address1, town=town, city=city, state=state,)
    return render(request, "address.html")


#====================show orders=======================
from datetime import datetime, timedelta
# def orders(request):
#     if 'email' in request.session:
#         oid=Order.objects.all()
#         if request.POST:
#             S = request.POST.get("filter_order")
#             time_filter = request.POST.get("flexRadioTime")
#             print(S)
#             if S:
#                 oid=Order.objects.filter(status=S)
#                 if time_filter:
#                     current_date = datetime.now().date()
#                     if time_filter == 'last_30_days':
#                         start_date = current_date - timedelta(days=30)
#                         oid = oid.filter(add_date__gte=start_date)
                        
#                     elif time_filter == 'last_6_months':
#                         start_date = current_date - timedelta(days=6*30)
#                         oid = oid.filter(add_date__gte=start_date)
                        
#                     elif time_filter == 'last_year':
#                         start_date = current_date - timedelta(days=365)
#                         oid = oid.filter(add_date__gte=start_date)
                                                                                     
#             else:       
#                 oid=Order.objects.all()
                
#             con={"oid":oid,"ch":ch}
#             return render(request,"orders.html",con)
#         else:
#             con={"oid":oid,"ch":ch}
#             return render(request,"orders.html",con)
#     else:
#         return render(request,"login.html")



#===============

def orders(request):
    if 'email' in request.session:
        # Initialize the queryset to all orders
        oid = Order.objects.all()

        # Check if the request is a POST request
        if request.method == 'POST':
            S = request.POST.get("filter_order")  # Get selected status filter
            time_filter = request.POST.get("filter_time")  # Get selected time filter
            print(time_filter) 
            # Apply status filter if selected
            if S:
                oid = oid.filter(status=S)
            
            # Apply time filter if selected
            if time_filter:
                current_date = datetime.now().date()
                print(f"Current Date: {current_date}")  # Print current date
                
                if time_filter == 'last_30_days':
                    start_date = current_date - timedelta(days=30)
                    oid = oid.filter(add_date__gte=start_date)
                    print(f"Filtering from: {start_date} to {current_date}")  # Print start and end dates

                elif time_filter == 'last_6_months':
                    start_date = current_date - timedelta(days=6*30)
                    oid = oid.filter(add_date__gte=start_date)
                    print(f"Filtering from: {start_date} to {current_date}")  # Print start and end dates
                    
                elif time_filter == 'last_year':
                    start_date = current_date - timedelta(days=365)
                    oid = oid.filter(add_date__gte=start_date)
                    print(f"Filtering from: {start_date} to {current_date}")  # Print start and end dates
        
        # Prepare the context with the filtered or unfiltered order list
        con = {"oid": oid, "ch": ch}
        return render(request, "orders.html", con)
    
    # If the user is not logged in, redirect to the login page
    else:
        return render(request, "login.html")
#==========================
# def orders(request):
#     if 'email' in request.session:
#         oid = Order.objects.all()

#         if request.method == 'POST':
#             filter_order = request.POST.get("filter_order")
#             time_filter = request.POST.get("flexRadioTime")

#             if filter_order:
#                 oid = Order.objects.filter(status=filter_order)
            
#             if time_filter:
#                 current_date = datetime.now().date()
#                 if time_filter == 'Last 30 days':
#                     start_date = current_date - timedelta(days=30)
#                 elif time_filter == 'Last 6 months':
#                     start_date = current_date - timedelta(days=6*30)
#                 elif time_filter == 'Last year':
#                     start_date = current_date - timedelta(days=365)
#                 else:
#                     start_date = None
                
#                 if start_date:
#                     oid = oid.filter(order_date__gte=start_date)
#         else:
#             # Handle the case where the request is not POST (optional)
#             pass

#         # Ensure `ch` is defined somewhere or adjust this based on your actual code
#         ch = None  # Define or replace this with actual logic

#         con = {"oid": oid, "ch": ch}
#         return render(request, "orders.html", con)
#     else:
#         return render(request, "login.html")
#=================checkout delete_address===============
def delete_address(request,id):
    show_address=Address.objects.get(id=id)
    show_address.delete()
    return redirect("address")

#=================checkout edit_address===============
def edit_address(request, id):
    show_address = Address.objects.get(id=id)
    print(show_address)
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        pincode = request.POST['pincode']
        address1 = request.POST['address1']
        town = request.POST['town']
        city = request.POST['city']
        state = request.POST['state']
        
        show_address.name = name
        show_address.mobile = mobile
        show_address.pincode = pincode
        show_address.address1 = address1
        show_address.town = town
        show_address.city = city
        show_address.state = state
        show_address.save()
        
        return redirect("address") 
    else:
        context = {'show_address': show_address}
        return render(request, 'address.html', context) 

#==================new user Register login====================
def add_user(request):
    if request.POST:
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=6089bc4afeb248cfbae263ac6dd99ef8&email={email}")

        try:
            uid = user.objects.get(email=email)
            message_for_email = "email already exist"
            return render(request,"register.html",{"message_for_email":message_for_email})
        except:
            if response.status_code == 200:
                data = response.json()
                if data["deliverability"] == "DELIVERABLE":
                    if password == confirm_password:
                        if len(password) >= 8:
                            lower = []
                            uper = []
                            digit = []
                            special = []
                            for i in password:
                                if i.islower():
                                    lower.append(i)
                                elif i.isupper():
                                    uper.append(i)
                                elif i.isdigit():
                                    digit.append(i)
                                else:
                                    special.append(i)
                            if len(lower) == 0 or len(uper) == 0 or len(digit) == 0 or len(special) == 0 :
                                message_for_password_critearia = "password have not follow this condition"
                                return render(request,"register.html",{"message_for_password_critearia":message_for_password_critearia})
                            else:
                                user.objects.create(name=name,mobile=mobile,email=email,password=password)
                                return redirect("login")
                        else:
                            message_for_password_length = "password length must have 8 character"
                            return render(request,"register.html",{"message_for_password_length":message_for_password_length})
                    else:
                        message_for_password = "please enter same password"
                        return render(request,"register.html",{"message_for_password": message_for_password})
                else:
                    message_for_email_not_availabel = "email is not on google"
                    return render(request,"register.html",{"message_for_email_not_availabel":message_for_email_not_availabel})
            else:
                message_for_unregister_email = "Failed to validate email"
                return render(request,"register.html",{"message_for_unregister_email":message_for_unregister_email})
    else:
        return render(request,"register.html")

#==================reset password =========================
def check_otp(request):
    if request.POST:
        new_password = request.POST['newPassword']
        confirm_password = request.POST['confirmPassword']
        get_otp = request.POST['otp']
        try:
            uid = user.objects.get(otp=get_otp)
            if new_password == confirm_password:
                if len(new_password) >= 8:
                    lower = []
                    uper = []
                    digit = []
                    special = []
                    for i in new_password:
                        if i.islower():
                            lower.append(i)
                        elif i.isupper():
                            uper.append(i)
                        elif i.isdigit():
                            digit.append(i)
                        else:
                            special.append(i)
                    if len(lower) == 0 or len(uper) == 0 or len(digit) == 0 or len(special) == 0 :
                        message_for_password_critearia = "password have not follow this condition"
                        return render(request,"reset_password.html",{"message_for_password_critearia":message_for_password_critearia})
                    else:
                        uid.password = new_password
                        uid.save()
                        return redirect("login")
                else:
                    message_for_password_length = "password length must have 8 character"
                    return render(request,"reset_password.html",{"message_for_password_length":message_for_password_length})
            else:
                message_for_not_match_password = "password does not match"
                return render(request,"reset_password.html",{"message_for_not_match_password":message_for_not_match_password})
        except:
            message_for_wrong_otp = "OTP is wrong."
            return render(request,"reset_password.html",{"message_for_wrong_otp":message_for_wrong_otp})
        
#============get_otp=======================
def otp_generate(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)

        try:
            uid=user.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail("Django",f"your OTP is {otp} ","dhruvchudasama999@gmail.com",[email])
            context={"uid":uid,"email":email}
            return render(request,"reset_password.html",context)
        except:
            message_for_wrong_email = "Email does not exist please enter diferent email"
            return render(request,"otp_generate.html",{"message_for_wrong_email":message_for_wrong_email})
    return render(request,"otp_generate.html")

#===================login=========================
def check_login(request):
    if 'email' in request.session:  
        uid = user.objects.get(email=request.session['email'])
        return render(request, "index.html")

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            data = user.objects.get(email = email, password = password)
            request.session['email'] = data.email
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            return redirect("index")
        except:
            message_for_login = "Invalid Login"
            return render(request,"login.html",{"message_for_login":message_for_login})

    

 
def login(request):
    return render(request,"login.html")

def log_out(request):
    if 'email' in request.session:  
        del(request.session['email'])
        return redirect("login")
    else:
        return redirect('login')



# def log_out(request):
#     if "email" in request.session:
#         del request.session['email']  # Clear user-specific session data
#     if "discount" in request.session:
#         del request.session['discount']  # Clear the discount for the coupon
#     return redirect("login")

def blog_post(request):
    if 'email' in request.session:
        return render(request,"blog_post.html")
    else:
        return render(request,"login.html")

def blog_read(request):
    if 'email' in request.session:
        return render(request,"blog_read.html")
    else:
        return render(request,"login.html")




# another Address formate
def billing_details(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        aid = Addtocart.objects.filter(user_id=uid)
        show_address = Address.objects.all()
        if request.method == 'POST':
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            email=request.POST['email']
            mobile = request.POST['mobile']
            zipcode = request.POST['zipcode']
            address = request.POST['address']

            city = request.POST['city']
            country = request.POST['country']
            
            Billing_Address.objects.create(f_name=f_name,l_name=l_name,email=email, mobile=mobile, zipcode=zipcode,
                                   address=address,city=city, country=country)
            
            return redirect('billing_details')
        
        con = {"show_address": show_address}
      
        return render(request,"billing_details.html",con)
    else:
        return render(request, "login.html")
    
    
    
    

def product_details(request):
    if 'email' in request.session:
        return render(request,"product_details.html")
    else:
        return render(request,"login.html")

def profile(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        con={"uid":uid}
        return render(request,"profile.html",con)
    else:
        return render(request,"login.html")
    
 
from datetime import datetime
def edit_profile(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')

            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            DOB = request.POST.get('DOB')
            location = request.POST.get('location')
            
                
            if DOB:
                try:
                   
                    parsed_date = datetime.strptime(DOB, '%Y-%m-%d').date()
                    uid.DOB = parsed_date
                except ValueError:
                    
                    con = {"uid": uid, "GENDER_CHOICES": GENDER_CHOICES }
                    return render(request, "edit_profile.html", con)
            else:
            
                uid.DOB
            
            uid.name=name
            uid.email=email
            uid.mobile=mobile
            uid.gender=gender
            
            uid.location=location
            uid.save()
            
            request.session['email']=email
            con={"uid":uid,"GENDER_CHOICES":GENDER_CHOICES}
            return render(request,"edit_profile.html",con)
        else:
            con={"uid":uid,"GENDER_CHOICES":GENDER_CHOICES}
            return render(request,"edit_profile.html",con)
            
    else:
        return render(request,"login.html")

def change_password(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        if request.POST:
            old_password= request.POST['old_password']
            new_password = request.POST['new_password']
            c_password = request.POST['c_password']
            if uid.password==old_password:
                if new_password==c_password:
                    uid.password=new_password
                    
                    uid.save()
                    con = {"uid": uid}
                    return render(request,"edit_profile.html",con)
                else:
                    print("invalid new password")
                    con={"e_msg":"Password Do Not Match","uid": uid}
                    return render(request,"edit_profile.html",con)
            else:
                print("invalid old password")
                con={"e_msg":"invalid old password","uid": uid}
                return render(request,"edit_profile.html",con)
        else:
                   
            return render(request,"edit_profile.html")
    else:
        return render(request,"login.html")
                    
def about(request):
    if 'email' in request.session:
        return render(request,"about.html")
    else:
        return render(request, "login.html")    
 
#===============contact page ===================
def contact(request):
    if 'email' in request.session:
        return render(request,"contact.html")
    else:
        return render(request, "login.html")
    

def register(request):
    if 'email' in request.session:
        return render(request,"register.html")
    else:
        return render(request,"login.html") 
    
def reset_password(request):
    return render(request,"reset_password.html")  

# def cart_plus(request, id):
#     c = Addtocart.objects.get(id=id)
#     c.quantity += 1
#     c.total_price = c.quantity * c.price
#     c.save()
#     return redirect("cart")

# def cart_mines(request, id):
#     c =Addtocart.objects.get(id=id)
#     if c.quantity == 1:
#         c.delete()
#     else:
#         c.quantity -= 1
#         c.total_price = c.quantity * c.price
#         c.save() 
#     return redirect("cart")





"""=============================================="""
"""----------⭐ Item Rating & Reviews ⭐--------"""
from django.urls import reverse
def create_rating(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        
        if request.method == 'POST':
            rate = request.POST['rate']
            comment = request.POST['comment']
            product_id = request.POST['product_id']
            date = timezone.localtime(timezone.now()).date()
            
            redirect_url = reverse('product_details1', kwargs={'id': product_id})
            pid = products.objects.get(id=product_id)
            
            review_image = request.FILES.get('review_image')
            Rating.objects.create(
                product_id=pid,
                rating=rate,
                comment=comment,
                name=uid.name,  
                
                date=date,
                image=review_image
            )
            
            return redirect(redirect_url)

        con = {"uid": uid}
        return render(request, "product_details.html", con)
    else:
        return render(request, "login.html")
    
    
#=============================

def cart(request):
    if "email" in request.session:
        uid = user.objects.get(email=request.session['email'])
        cid = Addtocart.objects.filter(user_id=uid)
        pid = products.objects.filter(id__in=[item.product_id.id for item in cid])
        prod = Addtocart.objects.filter(user_id=uid)
        cart_count=Addtocart.objects.filter(user_id=uid).count()
        ucid=User_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()
      
        print(ucid)
        l1 = []
        sub_total = 0
        charge = 0
        total_price = 0
        discount=0
        for i in prod:
            a = i.quantity * i.price
            l1.append(a)
            sub_total = sum(l1)
            charge = 50
        total_price = sub_total + charge
        if ucid == None:
            discount=0
        else:  
            discount=ucid.coupon_id.discount
            total_price-=ucid.coupon_id.discount
            print(ucid.coupon_id.discount)
        if cid.count() == 0 and ucid != None:
            ucid.ex=False
            discount=0
            total_price=0
            ucid.save()
            
        for i in cid:
            print("dfsak",i.size_cart)    


        con = {"uid": uid, "cid": cid, "pid": pid, "total_price": total_price, "sub_total": sub_total, "charge": charge, "cart_count":cart_count,"discount":discount}
        return render(request, "cart.html", con)
    else:   
        return render(request, "login.html")


    
# def apply_coupon(request):
    
#     uid=user.objects.get(email=request.session['email'])
#     if request.POST:
#         coupon_code = request.POST['code']
        
#         ccid=Coupon_code.objects.filter(coupon_code=coupon_code).exists()
#         if ccid:
#             ccid1=Coupon_code.objects.get(coupon_code=coupon_code)
#             ucid=User_coupon.objects.filter(user_id=uid, coupon_id=ccid1).exists()
#             if ucid:
#                 messages.info(request, "You have already used this coupon.")
#                 return redirect("cart")
#             else:
#                 User_coupon.objects.create(user_id=uid, coupon_id=ccid1,ex=True)
#                 messages.success(request, "Coupon applied successfully!")
#                 return redirect("cart")
    
#         else:
#             messages.error(request, "Invalid coupon code .")
#             return redirect("cart")

#     else:
#         return render(request,"cart.html")    

#==============

# from django.utils.timezone import now
# def apply_coupon(request):
#     uid=user.objects.get(email=request.session['email'])
#     if request.POST:
#         coupon_code=request.POST['code']
#         print("coupon post",coupon_code)
#         ccid=Coupon_code.objects.filter(coupon_code=coupon_code).exists()
#         if ccid:
#             ccid1=Coupon_code.objects.get(coupon_code=coupon_code)
#             if ccid1.expiry_time < now():
#                 messages.info(request, "Expired coupon")
#                 return redirect("cart")
#             uccid=User_coupon.objects.filter(user_id=uid,coupon_id=ccid1)
#             if uccid:
#                 messages.info(request,"exists")
#                 return redirect("cart")
            
#             else:
#                 User_coupon.objects.create(user_id=uid,coupon_id=ccid1,expiry_time=ccid1.expiry_time)
#                 messages.info(request,"created")
                
#                 return redirect("cart")
#         else:
#             messages.info(request,"invalid coupon")
            
#             return redirect("cart")
            
#     else:
#         return redirect("cart")
    
from django.utils.timezone import now
def apply_coupon(request):
    uid=user.objects.get(email=request.session['email'])
    if request.POST:
        coupon_code=request.POST['code']
        print(coupon_code)
        ccid=Coupon_code.objects.filter(coupon_code=coupon_code).exists()
        
        if ccid:
            ccid1=Coupon_code.objects.get(coupon_code=coupon_code)
            if ccid1.expiry_time<now():
                messages.info(request,"expired coupon")
                
                return redirect("cart")
                
            ucid=User_coupon.objects.filter(user_id=uid,coupon_id=ccid1).exists()
            if ucid:
                messages.info(request,"exists")
                return redirect("cart")
                
            else:
                User_coupon.objects.create(user_id=uid,coupon_id=ccid1)
                messages.info(request,"created")
                return redirect("cart")
            
        else:
            messages.info(request,"invalid coupon")
            return redirect("cart")
    else:
        return redirect("cart")

#==============
# def apply_coupon(request):
#     uid=user.objects.get(email=request.session['email'])
#     if request.POST:
#         code=request.POST['code']
#         print("dfsdsafdsfa",code)
#         ceid=Coupon_code.objects.filter(coupon_code=code).exists()
#         if ceid:
#             ceid=Coupon_code.objects.get(coupon_code=code)
#             ucid=User_coupon.objects.filter(user_id=uid,coupon_id=ceid).exists()
#             if ucid:
#                 messages.success(request,"user coupon exists")
#                 return redirect(cart)
#             else:
                
                
#                 User_coupon.objects.create(user_id=uid,coupon_id=ceid)
#                 messages.success(request,"success")
                
#                 return redirect(cart)
#         else:
#             messages.success(request,"not found")
#             return redirect(cart)
            
                
#     else:
#         return render(request,"cart.html")   