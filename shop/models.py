from django.db import models

# Create your models here.
class Product(models.Model):
    product_id  = models.AutoField # Auto incrementing integer field
    product_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300) # Description of product
    category = models.CharField(max_length=50, default="") # Can Provide a default value as well 
    subcategory=models.CharField(max_length=50, default="") 
    pub_date = models.DateField() # Date Field
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images", default="") # Select the upload folder

    def __str__(self): # Change the representation
        return self.product_name