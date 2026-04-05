from django.contrib import admin
# from .models import Student
# from .models import Employee
from .models import Customer, BookingDataBase, ResidentalCleaning, OfficeCleaning, KitchenCleaning, GardenCleaning, Post_ConstructionCleaning, TreeCleaning, Booking, BathroomCleaning, SofaCleaning, WindowCleaning, CustomerFeedback, CleanzaCommunity, ContactUs, UserSetting, CleanzaBlog
'''
Amdin: It can access the data and helps in authentication.

TO CREATE ADMIN:
1. Using command: python manage.py createsuperuser
2. Enter username
3. Enter email (optional)
4. Enter Password
5. Go to the ./admin page


Modify Admin Panel:
1. Change Panel Header: admin.site.site_header=' '
2. Change Browser Table Title: admin.site.site_title=''
3. Change Index Title: admin.site.index_title=''
'''

# Register your models here.
# admin.site.register(Student)
# admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(BookingDataBase)
admin.site.register(Booking)
admin.site.register(ResidentalCleaning)
admin.site.register(KitchenCleaning)
admin.site.register(BathroomCleaning)
admin.site.register(OfficeCleaning)
admin.site.register(GardenCleaning)
admin.site.register(TreeCleaning)
admin.site.register(SofaCleaning)
admin.site.register(WindowCleaning)
admin.site.register(Post_ConstructionCleaning)
admin.site.register(CustomerFeedback)
admin.site.register(CleanzaCommunity)
admin.site.register(ContactUs)
admin.site.register(UserSetting)
admin.site.register(CleanzaBlog)


#Modifying admin panel page
admin.site.site_header="Rajkumar Django "
admin.site.site_title="My Django Tutorial"
admin.site.index_title="Django Tutorial by RJ"
