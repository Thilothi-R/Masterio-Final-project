from django.utils import timezone
from django.db import models

# Create your models here.
class indexregister(models.Model):
    name=models.CharField(max_length=100)
    mail_id=models.EmailField()
    phone_number=models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name
class contacts(models.Model):
    your_name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    messege=models.TextField()

    def __str__(self):
        return self.your_name
class allstudents(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Username

class feedback(models.Model):
    Course_Name=models.CharField(max_length=100)
    Message=models.TextField()
    datetime=models.DateTimeField(default=timezone.now,verbose_name='datetime')
 
    def __str__(self):
        return self.Course_Name

class category(models.Model):
    category_name=models.CharField(max_length=100)
    Parent_Category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)
    
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url ="" 
        return url 
    def __str__(self):
        return self.category_name
class packagecreate(models.Model):
    Enter_Price=models.CharField(max_length=100)
    Commission=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.Enter_Price


class allinstructor(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username
class alladminuser(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Mail_id=models.EmailField()
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Username


class zoommeet(models.Model):
    Password=models.CharField(max_length=100)
    token=models.CharField(max_length=100)

    def __str__(self):
        return self.Password 
class addcourse(models.Model):
    course_title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    course_level=models.CharField(max_length=100)
    short_description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/%Y/%m/%d',null=True,blank=True)
    overview_url=models.CharField(max_length=100)
    provider=models.CharField(max_length=100)
    requirements=models.CharField(max_length=100)
    outcome=models.CharField(max_length=100)
    tags=models.CharField(max_length=100)
    free_course=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    meta_title=models.CharField(max_length=100)
    meta_description=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.course_title 

