from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=120)
    description=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    image=models.ImageField(null=True,upload_to="images")
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=100)
    
    @property
    def avg_rating(self):
        rating=self.reviews_set.all().values_list("rating",flat=True)
        if rating:
            return sum(rating)/len(rating)
        else:
            return 0


    @property
    def product_reviews(self):
        return self.reviews_set.all() 


    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

 
   
 

    
class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    date=models.DateField(auto_now_add=True)
    options=(("in-cart","in-cart"),
             ("order-placed","order-placed"),
             ("removed","removed")            
             
             )
    status=models.CharField(max_length=100,choices=options,default="in-cart")

