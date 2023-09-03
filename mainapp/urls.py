from django.urls import path
from .views import *
urlpatterns=[
    path('index/',index),
    path('index1/',index1),
    path('registeruser/',registeruser),
    path('loginuser/',loginuser),
    path('logoutt/',logoutt),
    path('adminlogout/',adminlogout),
    path('terms/',terms),
    path('adminlogin/',adminlogin),
    path('adminpage/',adminpage),
    path('popularcar/',popularcar),
    path('popularcardisplay/',popularcardisplay),
    path('popularcardelete/<int:id>',popularcardelete),
    path('justlaunched/',justlaunched),
    path('justlauncheddisplay/',justlauncheddisplay),
    path('justlauncheddelete/<int:id>',justlauncheddelete),
    path('justlaunchededit/<int:id>', justlaunchededit),
    path('upcomingcar/',upcomingcar),
    path('upcomingdisplay/',upcomingdisplay),
    path('upcomingcardelete/<int:id>',upcomingcardelete),
    path('upcomingcaredit/<int:id>', upcomingcaredit),
    path('happycoustmer/',happycoustmer),
    path('happycoustmerdisplay/',happycoustmerdisplay),
    path('happycustomerhtml/',happycustomerhtml),
    path('happycustomerdelete/<int:id>',happycustomerdelete),
    path('carstock/',carstock),
    path('carstockdisplay/',carstockdisplay),
    path('carstockdelete/<int:id>',carstockdelete),
    path('carstockedit/<int:id>',carstockedit),
    path('cargalery/',cargalery),
    path('cargalerydisplay/',cargalerydisplay),
    path('cargaleryuserdisplay/',cargaleryuserdisplay),
    path('cargalerydelete/<int:id>',cargalerydelete),
    path('advertise/',advertise),
    path('advertisedisplay/',advertisedisplay),
    path('advertisedelete/<int:id>',advertisedelete),
    path('ourshowroom/',ourshowroom),
    path('ourshowroomdisplay/',ourshowroomdisplay),
    path('ourshowroomuserdisplay/', ourshowroomuserdisplay),
    path('ourshowroomdelete/<int:id>',ourshowroomdelete),
    path('forgotpassword/', forgot_password),
    path('change/', change),
    path('change_password/<int:id>', change_password),
    path('userprofile/',userprofile),
    path('userdetailsedit/<int:id>',userdetailsedit),
    path('userimageedit/<int:id>',userimageedit),
    path('wish/<int:id>',wish),
    path('wishlistview/',wishlistview),
    path('alreadywishlist/',alreadywishlist),
    path('wishlistdelete/<int:id>',wishlistdelete),
    path('detailview/<int:id>',detailview),
    path('upcomingdetailview/<int:id>',upcomingdetailview),
    path('search/',search),
    path('buy/<int:id>',buy),
    path('totalbuydisplay/',totalbuydisplay),
    path('totalbuydelete/',totalbuydelete),
    path('contact/',contact),
    path('contactmsg/',contactmsg),
    path('contactdisplay/',contactdisplay),
    path('contactdelete/<int:id>',contactdelete),
    path('print/',print),
    path('addmoney/<int:id>', addmoney),
    path('addmoneydisplay/',addmoneydisplay),
    path('withdrawmoney/<int:id>',withdrawmoney),
    path('withdrawdisplay/',withdrawdisplay),
    path('checkbalance/<int:id>',checkbalance),
    path('checkbalancedisplay/',checkbalancedisplay),
    path('res/',res)




]