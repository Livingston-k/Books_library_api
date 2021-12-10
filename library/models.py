from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    publish_date = models.DateField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=8,null=True,blank=True)
    num_pages= models.IntegerField(default=0)
    isbn13 = models.CharField(max_length=13,null=True,blank=True)

    def __str__(self):
        return self.title
