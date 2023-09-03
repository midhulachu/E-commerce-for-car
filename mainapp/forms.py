from django import forms

class registeruserform(forms.Form):
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    number=forms.IntegerField()
    image=forms.FileField()
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)

class loginuserform(forms.Form):
    email=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class popularcarform(forms.Form):
    image=forms.FileField()
    carname=forms.CharField(max_length=20)
    price=forms.IntegerField()
class justlaunchedform(forms.Form):
    image=forms.FileField()
    carname=forms.CharField(max_length=20)
    price=forms.IntegerField()
class upcomingform(forms.Form):
    image=forms.FileField()
    carname=forms.CharField(max_length=20)
    price=forms.IntegerField()
class happycoustmerform(forms.Form):
    image=forms.FileField()
    carname=forms.CharField(max_length=20)
    comments=forms.CharField(max_length=50)
class carstockform(forms.Form):
    image=forms.FileField()
    imagee = forms.FileField()
    imageee = forms.FileField()
    carname=forms.CharField(max_length=20)
    price=forms.IntegerField()
    offerprice = forms.IntegerField()
    milage=forms.IntegerField()
    transmission=forms.CharField(max_length=20)
    fuel=forms.CharField(max_length=20)
    seat=forms.IntegerField()
    powerwindow=forms.CharField(max_length=20)
    centrallocking=forms.CharField(max_length=20)
    abs=forms.CharField(max_length=20)
    music=forms.CharField(max_length=20)
    gps=forms.CharField(max_length=20)
    display=forms.CharField(max_length=20)
    sunroof=forms.CharField(max_length=20)
    ownership=forms.CharField(max_length=20)
    aircontitioning=forms.CharField(max_length=20)
class cargaleryform(forms.Form):
    image=forms.FileField()
    carname=forms.CharField(max_length=20)
class advertiseform(forms.Form):
    image=forms.FileField()
    comment=forms.CharField(max_length=200)
class ourshowroomform(forms.Form):
    image=forms.FileField()
    address=forms.CharField(max_length=20)
    phone=forms.IntegerField()
    email=forms.EmailField(max_length=30)
class contactform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    subject=forms.CharField(max_length=30)
    message=forms.CharField(max_length=500)