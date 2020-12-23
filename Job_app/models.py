from django.db import models
from datetime import date, datetime
import re
import bcrypt

class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    birthday=models.DateField()
    education=models.TextField()
    field_of_experience=models.TextField()
<<<<<<< HEAD
=======
    image = models.ImageField(upload_to="images/",blank=True)
>>>>>>> b99e7a3388ad5f6dc4404a631cc28c9e5c0674be
    password=models.CharField(max_length=255)
    interests=models.TextField()
    about=models.TextField()
    role=models.ForeignKey(Role,related_name='user', on_delete=models.CASCADE) # foreignkey one to many  user with role
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Session (models.Model):
    date=models.DateField()
    period=models.TimeField()
    description=models.TextField()
    user=models.ForeignKey(User,related_name='user_session', on_delete=models.CASCADE) # foreignkey one to many  user with session 
    consultant=models.ForeignKey(User,related_name='consultant_session', on_delete=models.CASCADE)# foreignkey one to many  user with session 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Partner(models.Model):
    name=models.CharField(max_length=255)
    field_of_company=models.TextField()
    about=models.TextField()
<<<<<<< HEAD
=======
    image = models.ImageField(upload_to="images/",blank=True)
>>>>>>> b99e7a3388ad5f6dc4404a631cc28c9e5c0674be
    admin=models.ForeignKey(User,related_name='partner', on_delete=models.CASCADE)# foreignkey one to many user with partner
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Story(models.Model):
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)# foreignkey one to one user with story
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
<<<<<<< HEAD

# Create your models here.

=======



# def user_login(login_info):
#     user_exist = User.objects.filter(email=login_info['email'])
#     if len(user_exist):
#         password= login_info['password']
#         if bcrypt.checkpw(password.encode(), user_exist[0].password.encode()):
#             return user_exist[0]
#     return False

>>>>>>> b99e7a3388ad5f6dc4404a631cc28c9e5c0674be
