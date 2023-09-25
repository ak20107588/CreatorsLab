from django.db import models

# Create your models here.

class User(models.Model):
    UserName=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Password=models.CharField( max_length=255)
    
class UploadFile(models.Model):
    FileUpload=models.FileField( upload_to='fileupload')