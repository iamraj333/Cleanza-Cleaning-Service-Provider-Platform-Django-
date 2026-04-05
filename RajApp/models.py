from django.db import models
import uuid


'''
Models: It is the layout or template of pages, which used for multiple purpose, but in Django application should be only one models.py file.
-It is used to make data in form of tables and it written using an class.
-In models.py we can create multiple class to create to models


HOW TO USE MODEL IN APPLICATION
1. create models using class, for example, class Student(models.Model)
2. Using command 'python manage.py makemigrations' to create data table
3. Using command 'python manage.py migrate' to apply the migration.
4. Go to the admin.py and register the model to managed to give priviledge to the admin to manage the model.
4. After migration we use shell.py to insert data to the table using command, s=Student.object.create();



IMPORTANT NOTE: Everytime you have to run makemigration and migrate where something change or altered in models.py

'''

class Customer(models.Model):
    EmailStatus=[
        ('Pending','Pending'),
        ('Verified','Verified')
    ]
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    areaCode=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    password=models.TextField()
    isEmailVerified=models.CharField(max_length=10,choices=EmailStatus, default='Pending')
    bio=models.TextField(default="")
    remember=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}.{self.name}"
    

#UserSettings
class UserSetting(models.Model):
    User=models.ForeignKey(Customer,on_delete=models.CASCADE)
    WebTheme=models.CharField(max_length=10, default='Dark')
    WebFontSize=models.CharField(max_length=10, default='Medium')
    IsEmailNotification=models.CharField(max_length=10, default='No')
    IsWebNotification=models.CharField(max_length=10, default='No')
    WebLanguage=models.CharField(max_length=10, default='English')
    WebTimeZone=models.CharField(max_length=10, default='IST')

    def __str__(self):
        return f"{self.id} - {self.User.name}"


class BookingDataBase(models.Model):
    StatusChoice=[
        ('Pending', 'Pending'),
        ('Confirm', 'Confirm'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    service_name=models.CharField(max_length=100, default="Not Defined")
    time=models.CharField(max_length=50, default="")
    date=models.DateField(default="")
    propertyType=models.CharField(max_length=10, default="")
    No_Of_Bedroom=models.IntegerField(default=0)
    No_Of_Bathroom=models.IntegerField(default=0)
    Is_UV_Sanitization=models.CharField(max_length=50, default="")
    Service_Address=models.TextField(default="")
    TotalCharge=models.CharField(default="0")
    Customer_ID=models.ForeignKey(Customer, on_delete=models.CASCADE)
    Customer_Name=models.CharField(max_length=50, default="")
    Customer_Email=models.CharField(max_length=50, default="")
    Customer_Phone=models.BigIntegerField(null=True)
    Customer_Instruction=models.TextField(default="")
    Booking_DateTime=models.CharField(max_length=100, default="")
    Booking_Status=models.CharField(max_length=20, choices=StatusChoice, default='Pending')

    def __str__(self):
        return f"{self.BId} - {self.Customer_Name}"
    


class Booking(models.Model):
    StatusChoice=[
        ('Pending', 'Pending'),
        ('Confirm', 'Confirm'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    Service_name=models.CharField(max_length=50, default="")
    time=models.CharField(max_length=50, default="")
    date=models.DateField(default="")
    Service_Address=models.TextField(default="")
    Customer_Instruction=models.TextField(default="")
    TotalCharge=models.CharField(default="0")
    Booking_Status=models.CharField(max_length=20, choices=StatusChoice, default='Pending')
    Booking_DateTime=models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.id}. {self.Customer.name}"
    
#Residental Cleaning
class ResidentalCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    HomeBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    propertyType=models.CharField(max_length=10, default="")
    No_Of_Bedroom=models.IntegerField(default=0)
    No_Of_Bathroom=models.IntegerField(default=0)
    Is_UV_Sanitization=models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.BId} - {self.HomeBooking.Customer.name}"
    

#Kitchen Cleaning
class KitchenCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    KitchenBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    KitchenType=models.CharField(max_length=30, default="")
    GreaseLevel=models.CharField(max_length=20, default="")
    Is_Chimney_Cleaning=models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.BId} - {self.KitchenBooking.Customer.name}"
    

#Bathroom and Toilet Cleaning
class BathroomCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    BathroomBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    BathroomType=models.CharField(max_length=30, default="")
    No_Of_Toilet=models.IntegerField(default=0)
    No_Of_Bathroom=models.IntegerField(default=0)
    Is_Hardwater_Stain=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.BathroomBooking.Customer.name}"
    

#Office Cleaning
class OfficeCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    OfficeBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    OfficeSize=models.CharField(max_length=20, default="")
    No_Of_Washroom=models.IntegerField(default=0)
    Is_Glass_Partition=models.CharField(max_length=10, default="")
    Is_UV_Sanitization=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.OfficeBooking.Customer.name}"
    

#Garden Cleaning
class GardenCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    GardenBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    GardenSize=models.CharField(max_length=20, default="")
    Is_Grass_Trimming=models.CharField(max_length=20, default="")
    Is_Tree_Trimming=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.GardenBooking.Customer.name}"


#Tree Cleaning
class TreeCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    TreeBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    Tree_Service_Type=models.CharField(max_length=20, default="")
    No_Of_Tree=models.IntegerField(default=0)
    Tree_Max_Height=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.TreeBooking.Customer.name}"


#Sofa Cleaning
class SofaCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    SofaBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    SofaType=models.CharField(max_length=20, default="")
    No_Of_Seat=models.IntegerField(default=0)
    Is_Stain_Cleaning=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.SofaBooking.Customer.name}"


#Window Cleaning
class WindowCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    WindowBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    WindowType=models.CharField(max_length=20, default="")
    No_Of_Window=models.IntegerField(default=0)
    Window_Side=models.CharField(max_length=20, default="")
    Window_Height=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.WindowBooking.Customer.name}"


#Post-Construction Cleaning
class Post_ConstructionCleaning(models.Model):
    BId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    ConstructionBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    ConstructionType=models.CharField(max_length=20, default="")
    PropertySize=models.CharField(max_length=20, default="")
    Is_Construction_Stain=models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.BId} - {self.ConstructionBooking.Customer.name}"


#Customer Reviews or feedback
class CustomerFeedback(models.Model):
    ReviewId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    Reviewer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    ReviewBooking=models.OneToOneField(Booking, on_delete=models.CASCADE)
    ReviewRating=models.IntegerField(default=0)
    ReviewText=models.TextField(default="")

    def __str__(self):
        return f"{self.ReviewId} - {self.Reviewer.name}"

#Cleanza Community
class CleanzaCommunity(models.Model):
    CommunityId=models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    CommunityEmail=models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.CommunityId} - {self.CommunityEmail}"


#Contact Data
class ContactUs(models.Model):
    ContactId=models.UUIDField(editable=False,primary_key=True, default=uuid.uuid4)
    ContactName=models.CharField(max_length=50, default="")
    ContactEmail=models.EmailField(max_length=100, default="")
    ContactPhone=models.CharField(max_length=20, default="")
    ContactQuery=models.CharField(max_length=100, default="")
    ContactMessage=models.TextField(default="")

    def __str__(self):
        return f"{self.ContactName} - {self.ContactQuery}"
    
#Blogs
class CleanzaBlog(models.Model):
    publisher=models.ForeignKey(Customer, on_delete=models.CASCADE)
    title=models.CharField(unique=True,max_length=500, default="")
    thumbnail=models.CharField(blank=True,null=True, max_length=1000, default="")
    content=models.TextField(unique=True)
    dateOfPublish=models.DateField()
    category=models.CharField(max_length=50)
    readTime=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.publisher}"
    





