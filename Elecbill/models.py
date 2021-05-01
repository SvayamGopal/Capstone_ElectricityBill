from django.db import models

# Create your models here.

class elecbill(models.Model):
    c_name= models.CharField(max_length=100)
    c_id=models.CharField(max_length=100)
    c_img=models.ImageField(upload_to='',blank=True)
    c_email=models.EmailField(max_length=100)
    c_date=models.CharField(max_length=100)
    c_city=models.CharField(max_length=100)
    c_address=models.CharField(max_length=100)
    utility=models.CharField(max_length=100)
    units=models.IntegerField()
    bill=models.IntegerField()
    copy=models.CharField(max_length=100)
    
    class Meta:
        db_table="table_elec"
