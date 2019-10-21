"""AmazonWebsite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from ama import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^t/', views.showIndex),

    url(r'^head/',views.HeadSection),
    url(r'^body/', views.BodySection),

    url(r'^register/',views.Register),
    url(r'^registration/',views.Registration),

    url(r'^login/',views.Login),

    url(r"^accountexist/",views.accountexist),
    url(r"^accountdetails/",views.AccountalreadyExist),
    url(r"^productdetails/",views.ProductDetails),

    url(r"^aboutus/",views.AboutUs),

    url(r"^contactus/",views.ContactUs),

    url(r"^Home/",views.HomePage),

    url(r"^wiki/",views.wikipedia),

    url(r"^proceed1/",views.purchase),
    url(r"^proceed/",views.purchaseItem),


    url(r"^addcart/",views.Addcart),

    url(r"^logout/",views.Logout),

    url(r"^comment/",views.Comments),
    url(r"^comments/",views.CommentsSection),

    url(r"^adminstration/",views.Adminstration),
    url(r"^adminstrationdetails/",views.AdminstrationDetails),

    url(r"^viewproduct/",views.viewProduct),
    url(r"^viewproductDetails/",views.viewProductDetails),

    url(r"^viewpurchase/", views.viewPurchase),
    url(r"^viewpurchasedetails/", views.viewPurchaseDetails),

]
