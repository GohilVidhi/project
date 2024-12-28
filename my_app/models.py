from django.db import models
from colorfield.fields import ColorField 
# Create your models here.
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),]
class user(models.Model):
    name = models.CharField(max_length=70,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True,unique=True)
    otp=models.IntegerField(default=0,blank=True,null=True)
    password = models.CharField(max_length=30,blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    DOB=models.DateField(blank=True,null=True)
    location=models.CharField(max_length=60,blank=True,null=True)
    
    def __str__(self):
        return self.name 
class categories(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
class size(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
    
class color(models.Model):
    color = ColorField(default='#FF0000',null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="media",null=True,blank=True)
    
    def __str__(self):
        return self.name   
          
class products(models.Model):
    categories_id = models.ForeignKey(categories,on_delete=models.CASCADE,blank=True,null=True)
    size1=models.ManyToManyField(size,null=True,blank=True)
    color1=models.ManyToManyField(color,blank=True,null=True,max_length=50)
    name = models.CharField(max_length=100,null=True,blank=True)
    color = ColorField(default='#FF0000',null=True,blank=True)
    color_name = models.CharField(max_length=100,null=True,blank=True)
    
    sub_name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to="media",null=True,blank=True)
    quantity=models.IntegerField(default=1,null=True,blank=True)
    rating1 = models.IntegerField(blank=True,null=True)        #show stars
    half_rating = models.IntegerField(blank=True,null=True)       #show half stars
    image = models.ImageField(upload_to="media",null=True,blank=True)
    price = models.IntegerField()
    del_price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
        
    
    
class Addtocart(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="media",null=True,blank=True)
    image1 = models.ImageField(upload_to="media",null=True,blank=True)
    size_cart = models.ForeignKey(size, on_delete=models.CASCADE, null=True, blank=True)
    color_cart = models.ForeignKey(color, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
 
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField()

    
    def __str__(self):
        return self.name
        


    
    
class Add_Whishlist(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE,blank=True,null=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to="media",null=True,blank=True)
    
    name=models.CharField(max_length=60,null=True,blank=True)
    price=models.IntegerField()
    dell_price=models.IntegerField()
     
    def __str__(self):
        return self.name
        
        
# class Coupon_code(models.Model):
#     user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
#     code=models.CharField(max_length=60,null=True,blank=True)
#     discount=models.IntegerField()
#     expiry_date=models.DateTimeField()
#     one_time_use=models.BooleanField(default=True)
    
#     def __str__(self) -> str:
#         return self.code
    
    
class Coupon_code(models.Model):
    coupon_code=models.CharField(max_length=50,null=True,blank=True)
    discount=models.IntegerField()
    expiry_time = models.DateTimeField(blank=True,null=True)
       
    def __str__(self) -> str:
        return self.coupon_code
    
    
class User_coupon(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    coupon_id=models.ForeignKey(Coupon_code,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    ex=models.BooleanField(blank=True,null=True)  # coupon expire one time use
    expiry_time = models.DateTimeField(blank=True,null=True)

    def __str__(self) -> str:
        return self.coupon_id.coupon_code
    
class Address(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    mobile=models.IntegerField()
    pincode=models.IntegerField()
    address1=models.TextField()
    town=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Billing_Address(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    f_name=models.CharField(max_length=50,null=True,blank=True)
    l_name=models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=60,null=True,blank=True)
    mobile=models.IntegerField()
    zipcode=models.IntegerField()
    address=models.TextField()
    city=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.f_name
    
ch=(("On the way","On the way"),("Delivered","Delivered"),("Cancelled","Cancelled"),("Returned","Returned"))
class Order(models.Model):
    user_id=models.ForeignKey(user,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    
    address_id=models.ForeignKey(Address,max_length=60,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=60,blank=True,null=True)
    
    order_id=models.CharField(max_length=60,blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    description=models.CharField(max_length=100,blank=True,null=True)
    size_order=models.CharField(max_length=60,blank=True,null=True)
    quantity=models.CharField(max_length=60,blank=True,null=True)
    price=models.IntegerField()
    status=models.CharField(choices=ch,blank=True,null=True,max_length=60)
    total_price=models.IntegerField(default=1,blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    add_date=models.DateTimeField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Rating(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE,null=True,blank=True)  
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)  
    comment=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
                                        
        return self.name
    
    
    
class Review_like(models.Model):
    rating_id=models.ForeignKey(Rating,on_delete=models.CASCADE,null=True,blank=True)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    
    