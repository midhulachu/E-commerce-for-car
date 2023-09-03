from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import auth
def index(request):
    return render(request,'index2.html')
def terms(request):
    return render(request,'terms.html')
# def index1(request):
#     return render(request,'index3.html')
def index1(request):
 try:
   id1 = request.session['id']
   w=regmodel.objects.get(id=id1)
   c = popularcarmodel.objects.all()
   im = []
   cn = []
   pr = []
   da = []
   for i in c:
       im1 = str(i.image).split('/')[-1]
       im.append(im1)
       cna = i.carname
       cn.append(cna)
       pri = i.price
       pr.append(pri)
       daa = i.date
       da.append(daa)
   pair = zip(im, cn, pr, da)
   a = justlaunchedmodel.objects.all()
   im = []
   cn = []
   pr = []
   da = []
   idd=[]
   for i in a:
     im1 = str(i.image).split('/')[-1]
     im.append(im1)
     cna = i.carname
     cn.append(cna)
     pri = i.price
     pr.append(pri)
     daa = i.date
     da.append(daa)
     id=i.id
     idd.append(id)
   pai = zip(im, cn, pr, da,idd)
   b = upcomingmodel.objects.all()
   im = []
   cn = []
   pr = []
   da = []
   idd=[]
   for i in b:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
        pri = i.price
        pr.append(pri)
        daa = i.date
        da.append(daa)
        id=i.id
        idd.append(id)
   paii = zip(im, cn, pr, da,idd)
   e = carstockmodel.objects.all()
   im = []
   cn = []
   pr = []
   opr=[]
   da = []
   idd=[]
   for i in e:
       im1 = str(i.image).split('/')[-1]
       im.append(im1)
       cna = i.carname
       cn.append(cna)
       pri = i.price
       pr.append(pri)
       op=i.offerprice
       opr.append(op)
       daa = i.date
       da.append(daa)
       idi=i.id
       idd.append(idi)
   paire = zip(im, cn, pr,opr, da,idd)
   return render(request, 'index3.html', {'w':w,'a': pai, 'c': pair,'b':paii,'e':paire})
 except:
       return redirect(index)

def registeruser(request):
    if request.method=='POST':
        a=registeruserform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['firstname']
            ln=a.cleaned_data['lastname']
            un=a.cleaned_data['username']
            p=a.cleaned_data['password']
            nu=a.cleaned_data['number']
            im=a.cleaned_data['image']
            cp=a.cleaned_data['confirmpassword']
            e=a.cleaned_data['email']
            ui=int('1'+str(nu))
            b=regmodel.objects.all()
            for i in b:
                if(un==i.username or e==i.email):
                    return HttpResponse('allready esixt')
            else:
                if(p==cp):
                    c=regmodel(firstname=fn,lastname=ln,username=un,password=p,email=e,userid=ui,image=im,number=nu,balance=0)
                    c.save()
                    # request.session['balance']=b.balance
                    return redirect(index)
                else:
                    return HttpResponse('wrong pass')

    return render(request,'registeruser.html')
def loginuser(request):
     if request.method=='POST':
         a=loginuserform(request.POST)
         if a.is_valid():
             un=a.cleaned_data['email']
             p=a.cleaned_data['password']
             # b=User.objects.all()
             b = regmodel.objects.all()
             for i in b:
                 if i.email==un and i.password==p:
                     request.session['id'] = i.id
                     # return HttpResponse('login failed')
                     return redirect(index1)
             else:
                 return HttpResponse('login failed')
     return render(request,'loginuser.html')
def userdetailsedit(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.username = request.POST.get('username')
        a.password = request.POST.get('password')
        a.email=request.POST.get('email')
        a.number=request.POST.get('number')
        a.save()
        return redirect(userprofile)
    return render(request,'userdetailsedit.html',{'a':a})

def userimageedit(request, id):
        a = regmodel.objects.get(id=id)
        img = str(a.image).split('/')[-1]
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                a.save()
            else:
                a.image = request.FILES['image']
                a.save()
            a.save()
            return redirect(userprofile)

        return render(request, 'userimageedit.html', {'a': a, 'img': img})


def forgot_password(request):
    a=regmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ac=request.POST.get('username')
        for i in a:
            if(i.email==em and i.username==ac):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/mainapp/change_password/{id}"
                frm='dakshithmidhun7@gmail.com'
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check email")
        else:
            return HttpResponse("sorry")
    return render(request,'forgotpassword.html')
def change(request):
    return render(request,'forgotpasswordchange.html')
def change_password(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('rpin')
        if p1==p2:
            a.password=p1
            a.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('sorry')
    return render(request,'forgotpasswordchange.html')
def logoutt(request):
    logout(request)
    return redirect(index)
def userprofile(request):
    id1=request.session['id']
    w=regmodel.objects.get(id=id1)
    img=str(w.image).split('/')[-1]
    return render(request,'userprofile.html',{'w':w,'img':img})

def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            User=authenticate(request,username=username,password=password)
            if User is not None:
                return redirect(adminpage)

            else:
                return HttpResponse('login failed')
    return render(request,'loginadmin.html')
def adminlogout(request):
    logout(request)
    return redirect(index)
def adminpage(request):
 try:
    return render(request,'adminfrontpage.html')
 except:
     return redirect(index)
def popularcar(request):
    if request.method=='POST':
        a=popularcarform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['carname']
            pon=a.cleaned_data['price']
            b=popularcarmodel(image=top,carname=con,price=pon)
            b.save()
            return redirect(popularcardisplay)
        else:
            return HttpResponse('failed')
    return render(request,'popularcar.html')


def popularcardisplay(request):
    a=popularcarmodel.objects.all()
    im=[]
    cn=[]
    pr=[]
    da=[]
    id=[]
    for i in a:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna=i.carname
        cn.append(cna)
        pri=i.price
        pr.append(pri)
        daa=i.date
        da.append(daa)
        idd=i.id
        id.append(idd)
    pair=zip(im,cn,pr,da,id)
    return render(request,'popularcardisplay.html',{'a':pair})
def popularcardelete(request,id):
    a=popularcarmodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(popularcardisplay)
def justlaunched(request):
    if request.method=='POST':
        a=justlaunchedform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['carname']
            pon=a.cleaned_data['price']
            b=justlaunchedmodel(image=top,carname=con,price=pon)
            b.save()
            return redirect(justlauncheddisplay)
        else:
            return HttpResponse('failed')
    return render(request,'justlaunched.html')

def justlauncheddisplay(request):
    a=justlaunchedmodel.objects.all()
    im=[]
    cn=[]
    pr=[]
    da=[]
    id=[]
    for i in a:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna=i.carname
        cn.append(cna)
        pri=i.price
        pr.append(pri)
        daa=i.date
        da.append(daa)
        idd=i.id
        id.append(idd)
    pair=zip(im,cn,pr,da,id)
    return render(request,'justlauncheddisplay.html',{'a':pair})
def justlauncheddelete(request,id):
    e=justlaunchedmodel.objects.get(id=id)
    os.remove(str(e.image))
    e.delete()
    return redirect(justlauncheddisplay)

def justlaunchededit(request, id):
        a = justlaunchedmodel.objects.get(id=id)
        img = str(a.image).split('/')[-1]
        if request.method == 'POST':
            a.carname = request.POST.get('carname')
            a.price = request.POST.get('price')
            if request.FILES.get('image') == None:
                a.save()
            else:
                a.image = request.FILES['image']
                a.save()
            a.save()
            return redirect(justlauncheddisplay)

        return render(request, 'justlaunchededit.html', {'a': a, 'img': img})
def upcomingcar(request):
    if request.method=='POST':
        a=upcomingform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['carname']
            pon=a.cleaned_data['price']
            b=upcomingmodel(image=top,carname=con,price=pon)
            b.save()
            return redirect(upcomingdisplay)
        else:
            return HttpResponse('failed')
    return render(request,'upcomingcar.html')
def upcomingdisplay(request):
    b=upcomingmodel.objects.all()
    im=[]
    cn=[]
    pr=[]
    da=[]
    id=[]
    for i in b:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna=i.carname
        cn.append(cna)
        pri=i.price
        pr.append(pri)
        daa=i.date
        da.append(daa)
        idd=i.id
        id.append(idd)
    paii=zip(im,cn,pr,da,id)
    return render(request,'upcomingdisplay.html',{'b':paii})
def upcomingcardelete(request,id):
    e=upcomingmodel.objects.get(id=id)
    os.remove(str(e.image))
    e.delete()
    return redirect(upcomingdisplay)

def upcomingcaredit(request, id):
        a = upcomingmodel.objects.get(id=id)
        img = str(a.image).split('/')[-1]
        if request.method == 'POST':
            a.carname = request.POST.get('carname')
            a.price = request.POST.get('price')
            if request.FILES.get('image') == None:
                a.save()
            else:
                a.image = request.FILES['image']
                a.save()
            a.save()
            return redirect(upcomingdisplay)

        return render(request, 'upcomingedit.html', {'a': a, 'img': img})
def happycoustmer(request):
    if request.method=='POST':
        a=happycoustmerform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['carname']
            pon=a.cleaned_data['comments']
            b=happycoustmermodel(image=top,carname=con,comments=pon)
            b.save()
            return redirect(happycoustmerdisplay)
        else:
            return HttpResponse('failed')
    return render(request,'happycoustmer.html')
def happycoustmerdisplay(request):
    d=happycoustmermodel.objects.all()
    im=[]
    cn=[]
    pr=[]
    da=[]
    idm=[]
    for i in d:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna=i.carname
        cn.append(cna)
        pri=i.comments
        pr.append(pri)
        daa=i.date
        da.append(daa)
        idd=i.id
        idm.append(idd)
    paii=zip(im,cn,pr,da,idm)
    return render(request,'happycoustmerdisplay.html',{'d':paii})
def happycustomerhtml(request):
    d = happycoustmermodel.objects.all()
    im = []
    cn = []
    pr = []
    da = []
    for i in d:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
        pri = i.comments
        pr.append(pri)
        daa = i.date
        da.append(daa)
    pair = zip(im, cn, pr, da)
    return render(request, 'happycustomerhtml.html', {'d': pair})
def happycustomerdelete(request,id):
    a=happycoustmermodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(happycoustmerdisplay)
def carstock(request):
    if request.method=='POST':
        a=carstockform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            img=a.cleaned_data['imagee']
            imgg=a.cleaned_data['imageee']
            con=a.cleaned_data['carname']
            pon=a.cleaned_data['price']
            ofp=a.cleaned_data['offerprice']
            ml=a.cleaned_data['milage']
            tr=a.cleaned_data['transmission']
            fu=a.cleaned_data['fuel']
            se=a.cleaned_data['seat']
            pw=a.cleaned_data['powerwindow']
            cl=a.cleaned_data['centrallocking']
            abs=a.cleaned_data['abs']
            mu=a.cleaned_data['music']
            gps=a.cleaned_data['gps']
            di=a.cleaned_data['display']
            su=a.cleaned_data['sunroof']
            ow=a.cleaned_data['ownership']
            ac=a.cleaned_data['aircontitioning']
            b=carstockmodel(image=top,imagee=img,imageee=imgg,carname=con,price=pon,offerprice=ofp,milage=ml,transmission=tr,fuel=fu,seat=se,powerwindow=pw,centrallocking=cl,
                            abs=abs,music=mu,gps=gps,display=di,sunroof=su,ownership=ow,aircontitioning=ac)
            b.save()
            return redirect(carstockdisplay)
        else:
            return HttpResponse('failed')
    return render(request,'carstock.html')
def carstockdisplay(request):
    e = carstockmodel.objects.all()
    im = []
    cn = []
    pr = []
    cpr=[]
    da = []
    id=[]
    for i in e:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
        pri = i.price
        pr.append(pri)
        cp=i.offerprice
        cpr.append(cp)
        daa = i.date
        da.append(daa)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn, pr,cpr,da,id)
    return render(request, 'carstockdisplay.html', {'e': pair})
def carstockdelete(request,id):
    e=carstockmodel.objects.get(id=id)
    os.remove(str(e.image))
    os.remove(str(e.imagee))
    os.remove(str(e.imageee))
    e.delete()
    return redirect(carstockdisplay)

def carstockedit(request, id):
        a = carstockmodel.objects.get(id=id)
        img = str(a.image).split('/')[-1]
        imgg=str(a.imagee).split('/')[-1]
        imggg=str(a.imageee).split('/')[-1]
        if request.method == 'POST':
            a.carname = request.POST.get('carname')
            a.price=request.POST.get('price')
            a.offerprice=request.POST.get('offerprice')
            a.milage=request.POST.get('milage')
            a.transmission=request.POST.get('transmission')
            a.fuel=request.POST.get('fuel')
            a.seat=request.POST.get('seat')
            a.powerwindow=request.POST.get('powerwindow')
            a.centrallocking=request.POST.get('centrallocking')
            a.abs=request.POST.get('abs')
            a.music=request.POST.get('music')
            a.gps=request.POST.get('gps')
            a.display=request.POST.get('display')
            a.sunroof=request.POST.get('sunroof')
            a.ownership=request.POST.get('ownership')
            a.aircontitioning=request.POST.get('aircontitioning')

            if request.FILES.get('image') == None:
                a.save()
            else:
                a.image = request.FILES['image']
                a.save()
            a.save()
            return redirect(carstockdisplay)

        return render(request, 'carstockedit.html', {'a': a, 'img': img,'imgg':imgg,'imggg':imggg})
def cargalery(request):
    if request.method=='POST':
        a=cargaleryform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['carname']

            b=cargalerymodel(image=top,carname=con)
            b.save()
            return redirect(cargalerydisplay)
        else:
            return HttpResponse('failed')
    return render(request, 'cargalery.html')
def cargalerydisplay(request):
    f = cargalerymodel.objects.all()
    im = []
    cn = []
    id=[]
    for i in f:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn,id)
    return render(request, 'cargalerydisplay.html', {'f': pair})
def cargaleryuserdisplay(request):
    f = cargalerymodel.objects.all()
    im = []
    cn = []
    for i in f:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
    pair = zip(im, cn)
    return render(request, 'cargaleryuserdisplay.html', {'f': pair})
def cargalerydelete(request,id):
    a=cargalerymodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(cargalerydisplay)
def advertise(request):
    if request.method=='POST':
        a=advertiseform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['image']
            con=a.cleaned_data['comment']

            b=advertisemodel(image=top,comment=con)
            b.save()
            return HttpResponse('Advertisment add successfully')
        else:
            return HttpResponse('failed')
    return render(request, 'advertise.html')

def advertisedisplay(request):
    g = advertisemodel.objects.all()
    im = []
    cn = []
    id=[]
    for i in g:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.comment
        cn.append(cna)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn,id)
    return render(request, 'advertisedisplay.html', {'g': pair})
def advertisedelete(request,id):
    g=advertisemodel.objects.get(id=id)
    os.remove(str(g.image))
    g.delete()
    return redirect(advertisedisplay)
def ourshowroom(request):
    if request.method == 'POST':
        a = ourshowroomform(request.POST, request.FILES)
        if a.is_valid():
            top = a.cleaned_data['image']
            con = a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            em=a.cleaned_data['email']
            b = ourshowroommodel(image=top, address=con,phone=ph,email=em)
            b.save()
            return redirect(ourshowroomdisplay)
        else:
            return HttpResponse('failed')
    return render(request, 'ourshowroom.html')
def ourshowroomdisplay(request):
    h = ourshowroommodel.objects.all()
    im = []
    cn = []
    ph=[]
    em=[]
    id=[]
    for i in h:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.address
        cn.append(cna)
        phn=i.phone
        ph.append(phn)
        emm=i.email
        em.append(emm)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn,ph,em,id)
    return render(request, 'ourshowroomdisplay.html', {'h': pair})
def ourshowroomuserdisplay(request):
    h = ourshowroommodel.objects.all()
    im = []
    cn = []
    ph=[]
    em=[]
    id=[]
    for i in h:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.address
        cn.append(cna)
        phn=i.phone
        ph.append(phn)
        emm=i.email
        em.append(emm)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn,ph,em,id)
    return render(request, 'ourshowroomuserdisplay.html', {'h': pair})
def ourshowroomdelete(request,id):
    g=ourshowroommodel.objects.get(id=id)
    os.remove(str(g.image))
    g.delete()
    return redirect(ourshowroomdisplay)
def wish(request,id):
    a=carstockmodel.objects.get(id=id)
    a1=wishmodel.objects.all()
    for i in a1:
        if i.newsid==a.id and i.uid==request.session['id']:
            return redirect(alreadywishlist)
    b=wishmodel(image=a.image,carname=a.carname,price=a.price,offerprice=a.offerprice,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return redirect(wishlistview)
def wishlistview(request):
    id=request.session['id']
    a=wishmodel.objects.all()
    # b=wishmodel.objects.get(id=id)

    # img=str(a.image).split('/')[-1]
    return render(request,'wishlistview.html',{'a':a,'id':id})
def wishlistdelete(request,id):
    a = wishmodel.objects.get(id=id)
    # os.remove(str(a.image))
    a.delete()
    return redirect(wishlistview)
def detailview(request,id):
        w = carstockmodel.objects.get(id=id)
        img = str(w.image).split('/')[-1]
        imgg=str(w.imagee).split('/')[-1]
        imggg=str(w.imageee).split('/')[-1]
        return render(request, 'detailview.html', {'w': w,'img':img,'imgg':imgg,'imggg':imggg})
def upcomingdetailview(request, id):
    w = upcomingmodel.objects.get(id=id)
    img = str(w.image).split('/')[-1]
    return render(request, 'upcomingdetailsview.html', {'w': w, 'img': img})
def search(request):
    e = carstockmodel.objects.all()
    im = []
    cn = []
    pr = []
    cpr=[]
    da = []
    id=[]
    for i in e:
        im1 = str(i.image).split('/')[-1]
        im.append(im1)
        cna = i.carname
        cn.append(cna)
        pri = i.price
        pr.append(pri)
        cp=i.offerprice
        cpr.append(cp)
        daa = i.date
        da.append(daa)
        idd=i.id
        id.append(idd)
    pair = zip(im, cn, pr,cpr,da,id)
    return render(request, 'search.html', {'e': pair})
def buy(request,id):
    idd = request.session['id']
    a=wishmodel.objects.get(id=id)
    b=buymodel(carname=a.carname,price=a.offerprice,uid=request.session['id'])
    b.save()
    c=regmodel.objects.get(id=idd)
    if c.balance>=a.offerprice:
     c.balance-=a.offerprice
     c.save()
    else:
        return HttpResponse('sorry insufficient balance')
    return render(request, 'buydisplay.html', {'a': a})
def totalbuydisplay(request):
    a=buymodel.objects.all()
    id = request.session['id']
    return render(request,'totalbuydisplay.html',{'a':a,'id':id})
def totalbuydelete(request):
    a = buymodel.objects.all()
    a.delete()
    return redirect(totalbuydisplay)

def contact(request):
    if request.method=='POST':
        a=contactform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['name']
            ln=a.cleaned_data['email']
            un=a.cleaned_data['subject']
            p=a.cleaned_data['message']
            b=contactmodel(name=fn,email=ln,subject=un,message=p)
            b.save()
            return redirect(contactmsg)
        else:
            return HttpResponse('some error happened in your message,please try again')
    return render(request,'contact.html')
def contactmsg(request):
    return render(request,'contactmsg.html')
def contactdisplay(request):
    a=contactmodel.objects.all()
    return render(request,'contactdisplay.html',{'a':a})
def contactdelete(request,id):
    g=contactmodel.objects.get(id=id)
    g.delete()
    return redirect(contactdisplay)
def alreadywishlist(request):
    return render(request,'alreadywishlist.html')
def print(request):
    a=wishmodel.objects.all()
    id=request.session['id']
    # img=str(a.image).split('/')[-1]
    return render(request,'print.html',{'a':a,'id':id})
def addmoney(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount') #withot form
        password = request.POST.get('password')
        request.session['am'] = am
        if password == a.password:
            a.balance+=int(am)
            a.save()
            b=addamount(amount=am,uid=request.session['id'])
            b.save()
            return redirect(addmoneydisplay)
        else:
            return HttpResponse('failed')
    return render(request,'addamount.html')
def addmoneydisplay(request):
    am=request.session['am']
    id=request.session['id']
    a=regmodel.objects.get(id=id)
    return render(request,'adddisplay.html',{'am':am,'a':a})
def withdrawmoney(request,id):
    x=regmodel.objects.get(id=id)
    if request.method=='POST':
        am = request.POST.get('amount')  # withot form
        request.session['am'] = am
        password = request.POST.get('password')
        if password == x.password:
         if(x.balance>=int(am)):
            x.balance -= int(am)
            x.save()
            b=withmoney(amount=am,uid=request.session['id'])
            b.save()
            return redirect(withdrawdisplay)
         else:
            return HttpResponse('insufficientbalance')
        else:
            return HttpResponse('password incorrect')
    return render(request,'withdrawamount.html')
def withdrawdisplay(request):
    am=request.session['am']
    id = request.session['id']
    a = regmodel.objects.get(id=id)
    return render(request,'withdrawdisplay.html',{'am':am,'a':a})

def checkbalance(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        request.session['balance']=a.balance
        password=request.POST.get('password')
        if password==a.password:
            return redirect(checkbalancedisplay)
        else:
            return HttpResponse('wrong passsword')
    return render(request,'checkbalance.html')
def checkbalancedisplay(request):
    id = request.session['id']
    a = regmodel.objects.get(id=id)
    balance=request.session['balance']
    return render(request,'checkbalancedisplay.html',{'a':a,'balance':balance})
def res(request):
    return render(request,'responsive.html')