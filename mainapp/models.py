from django.db import models
class regmodel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    number=models.IntegerField()
    image=models.FileField(upload_to='mainapp/static')
    email=models.EmailField()
    password=models.CharField(max_length=20)
    userid=models.IntegerField()
    balance=models.IntegerField()

class popularcarmodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    date=models.DateField(auto_now=True)
class justlaunchedmodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    date=models.DateField(auto_now=True)
class upcomingmodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    date=models.DateField(auto_now=True)
class happycoustmermodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    comments=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
class carstockmodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    imagee = models.FileField(upload_to='mainapp/static')
    imageee = models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    offerprice = models.IntegerField()
    milage=models.IntegerField()
    transmission=models.CharField(max_length=20)
    fuel=models.CharField(max_length=20)
    seat=models.IntegerField()
    powerwindow=models.CharField(max_length=20)
    centrallocking=models.CharField(max_length=20)
    abs=models.CharField(max_length=20)
    music=models.CharField(max_length=20)
    gps=models.CharField(max_length=20)
    display=models.CharField(max_length=20)
    sunroof=models.CharField(max_length=20)
    ownership=models.CharField(max_length=20)
    aircontitioning=models.CharField(max_length=20)
    date=models.DateField(auto_now=True)
class wishmodel(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    offerprice = models.IntegerField()
    date=models.DateField(auto_now=True)

class cargalerymodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    carname=models.CharField(max_length=30)
class advertisemodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    comment=models.CharField(max_length=30)
class ourshowroommodel(models.Model):
    image=models.FileField(upload_to='mainapp/static')
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email= models.EmailField(max_length=30)
class buymodel(models.Model):
    carname=models.CharField(max_length=30)
    price=models.IntegerField()
    uid=models.IntegerField()
class contactmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=30)
    message=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)

class addamount(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
class withmoney(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)