from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50,null=True,default='')
    category = models.CharField(max_length=50,null=True,default='')
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name