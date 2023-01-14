from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.

# Create the models for blood donation application

sd =  datetime.now().strftime("%Y-%b-%d")
st =  datetime.now().strftime("%H:%M")


bgroup = (
    ("A", "A"),
    ("B","B"),
    ("B+","B+"),
    ("B-","B-"),
    ("O+","O+"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("O-","O-"),
)

gchoice = (
    ('M',"Male"),
    ('F','Female'),
    ('O', 'Others'),
)

class UserProfile(models.Model):
    profileid = models.AutoField(primary_key=True,db_column="Profile ID")
    userid = models.OneToOneField(User, on_delete=models.CASCADE, db_column="User ID", verbose_name="User Id")
    first_name  = models.CharField(max_length=30, db_column="First Name", help_text="Enter First Name")
    last_name  = models.CharField(max_length=30, db_column="Last Name", help_text="Enter Last Name")
    bloodgroup = models.CharField(max_length=3, choices = bgroup, default='B+', db_column="Blood Group", help_text="Select Blood Group")
    gender = models.CharField(max_length=1, choices = gchoice, default="M", db_column="Gender", help_text="Select Gender")
    dob = models.DateField(db_column="Date of Birth", verbose_name="Date of Birth", help_text="Enter / Select Date of Birth (YYYY-MM-DD)")
    mobileno = models.CharField(max_length=10, db_column="Mobile Number")
    email = models.EmailField(max_length=50, db_column="EMail")
    subs = models.BooleanField(db_column="Subscription", default = False, verbose_name="Subscribe ? ")
    address1 = models.CharField(max_length=300, db_column="Address1")
    address2 = models.CharField(max_length=300, db_column="Address2", null=True, blank=True)
    zipcode = models.CharField(max_length=6, db_column="Zip Code")
    state = models.CharField(max_length=10, db_column="State")
    city = models.CharField(max_length=20, db_column="City")

    def __str__(self):
        return str(self.userid)

    class Meta:
        db_table = "User Profile"

class StateCityMaster(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")
    state_code = models.CharField(max_length=3, db_column="State Code", null=True)
    state_name = models.CharField(max_length=30, db_column="State Name", null=True)
    city_name = models.CharField(max_length=40, db_column="City", null=True)
    zipcode = models.CharField(max_length=6, db_column="ZipCode", null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "StateCity Master"

class BloodDonerTransactions(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    donationdate = models.DateField(db_column="Donation Date", null=True)
    donationtime = models.TimeField(db_column="Donation Time", null=True)
    units = models.IntegerField(db_column="Units", default=0)
    shelflife = models.IntegerField(db_column="Shelf Life", default=2)

    def __str__(self):
        return str(self.userid)

    class Meta:
        db_table = "BlDoner Trans"

class DonnerSumary(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    lastdateDonation = models.DateField(db_column="Last DonationDate", null=True)
    noofunits = models.IntegerField(db_column="Units", null=True)
    threshhold = models.IntegerField(db_column="ThreshHold Value", null=True)

    def __str__(self):
        return str(self.userid)

    class Meta:
        db_table = "Donner Summary"

class CampaignSumary(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")
    cdate = models.DateField(db_column="Campaign Date", null=True)
    location = models.CharField(max_length=50, db_column="Location", null=True)
    noofdoners = models.IntegerField(db_column="NoOf Doners", default = 0)
    bloodgroup = models.CharField(max_length=3, db_column="Blood Group", choices=bgroup, default="A")

    class Meta:
        db_table = "Campaign Sumary"


class CampaignMst(models.Model):
    id = models.AutoField(primary_key=True, db_column="ID")
    campaignname = models.CharField(max_length=200, db_column="Campaign Name", default='')
    sdate = models.DateField(db_column="Start Date", null=True)
    stime = models.TimeField(db_column="Start Time", null=True)
    edate = models.DateField(db_column="End Date", null=True)
    etime = models.TimeField(db_column="End Time", null=True)
    location = models.CharField(max_length=30, db_column="Location", default='')
    city = models.CharField(max_length=30, db_column="City", default='')

    def __str__(self):
        return self.campaignname

    class Meta:
        db_table = "Campaign Master"

class CampaignDetails(models.Model):
    cid = models.ForeignKey(CampaignMst, on_delete=models.CASCADE, db_column="ID", null=True)
    guestname = models.CharField(max_length=100, db_column="Guest Name", default='')
    mobileno = models.CharField(max_length=10, db_column="Mobile Number", default='')
    email = models.EmailField(max_length=100, db_column="Email", default='')
    gender = models.CharField(choices = gchoice, max_length=1, db_column="Gender", default='M')
    age = models.IntegerField(db_column="Age", default=18)
    bloodgroup = models.CharField(max_length=3, choices = bgroup, db_column="Blood Group", default="A")



    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Campaign Details"