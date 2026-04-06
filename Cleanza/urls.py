"""
URL configuration for Cleanza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from RajApp import views
from django.conf import settings
from django.conf.urls.static import static

handler404='RajApp.views.pageNotFound'
handler500='RajApp.views.pageNotFound505'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.Intro, name="Intro"),
    # path('intro/', views.Fun, name="Fun"), #this path used as navigation to navigate the pages

    #create home, about, register page
    path('',views.home, name='home'),
    path('search/',views.search, name='search'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('write_blog/', views.write_blog, name='write_blog'),
    path('blog_submission/', views.blog_submission, name='blog_submission'),
    path('blog/read_blog/<int:blogId>/', views.read_blog, name='read_blog'),

    path('register/', views.register,name="register"),
    # path('session_login/',views.session_login, name="session_login"),
    path('services/bookService/<int:serviceId>/', views.bookService, name="bookService"),
    path('ScheduleService/<int:serviceId>/', views.ScheduleService, name='ScheduleService'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('contact/',views.contact, name="contact"),
    path('project/', views.project, name="project"),
    path('service_booking_submission/', views.service_booking_submission, name="service_booking_submission"),
    path('dashboard/delete_booking/<int:serviceDeleteId>', views.service_booking_delete, name="service_booking_delete"),
    path('dashboard/reschedule_booking/<int:bookedServiceId>', views.service_booking_reschedule, name="service_booking_reschedule"),
    path('booking_Reschedule_Submission/', views.booking_Reschedule_Submission, name="booking_Reschedule_Submission"),
    path('dashboard/booking_review/<int:bookedServiceReview>', views.service_booking_review, name="service_booking_review"),
    path('booking_Review_Submission/', views.booking_Review_Submission, name="booking_Review_Submission"),
    path('community_support/', views.community_support, name="community_support"),
    path('myAccount/', views.myAccount, name="myAccount"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('update_contact/', views.update_contact, name="update_contact"),
    path('update_address/', views.update_address, name="update_address"),
    path('update_password/', views.update_password, name="update_password"),
    #User Settings
    path('mySetting/', views.mySetting, name="mySetting"),
    path('change_Setting/', views.change_Setting, name="change_Setting"),
    #User Support and Help
    path('faqSupport/', views.faqSupport, name="faqSupport"),

    #email verification
    path('email_verification/', views.email_verification, name="email_verification"),
    path('emailVerifiedCodeCheck/', views.emailVerifiedCodeCheck, name="emailVerifiedCodeCheck"),
    path('logout/',views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
