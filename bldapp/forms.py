# user registration form

from faulthandler import disable
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from bldapp.models import UserProfile, BloodDonerTransactions, CampaignMst, StateCityMaster



# define a form class 

class userRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' )


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

class DateInput(forms.DateInput):
    input_type= "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class userProfileDisable(forms.ModelForm):
    userid = forms.IntegerField(disabled=True)
    first_name  = forms.CharField(disabled=True)
    last_name  = forms.CharField(disabled=True)
    bloodgroup = forms.ChoiceField(disabled=True, widget=forms.Select(), choices=bgroup)
    gender = forms.ChoiceField(disabled=True, widget=forms.Select(), choices=gchoice)
    dob = forms.DateField(disabled=True, widget=DateInput())
    mobileno = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)
    subs = forms.BooleanField(disabled=True)
    address1 = forms.CharField(disabled=True)
    address2 = forms.CharField(disabled=True)
    zipcode = forms.CharField(disabled=True)
    state = forms.CharField(disabled=True)
    city = forms.CharField(disabled=True)

    class Meta:
        model = UserProfile
        fields = ['userid','first_name','last_name', 'bloodgroup', 'gender','dob','mobileno','email','subs','address1','address2','zipcode','state','city']
        # fields to be excluded from the form    
        #exclude = []



class userProfileAdd(forms.ModelForm):
    userid = forms.IntegerField()
    first_name  = forms.CharField()
    last_name  = forms.CharField()
    bloodgroup = forms.ChoiceField(widget=forms.Select(), choices=bgroup)
    gender = forms.ChoiceField(widget=forms.Select(), choices=gchoice)
    dob = forms.DateField(widget=DateInput())#format="%m/%d/%Y"))
    mobileno = forms.CharField()
    email = forms.EmailField()
    subs = forms.BooleanField()
    address1 = forms.CharField()
    address2 = forms.CharField()
    zipcode = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['userid','first_name','last_name', 'bloodgroup', 'gender','dob','mobileno','email','subs','address1','address2','zipcode','state','city']


    def __init__(self, *args, **kwargs):
        super(userProfileAdd, self).__init__(*args, **kwargs)
        self.fields['userid'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['first_name'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['last_name'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['bloodgroup'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['gender'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['dob'].widget.attrs={'autocomplete':'off', 'required':'true'} #, 'id':'datepicker', 'placeholder':'Select Date'}
        self.fields['mobileno'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['email'].widget.attrs={'autocomplete':'off', 'required':'true'}
        self.fields['subs'].widget.attrs={'autocomplete':'off'}
        self.fields['address1'].widget.attrs={'autocomplete':'off'}
        self.fields['address2'].widget.attrs={'autocomplete':'off'}
        self.fields['zipcode'].widget.attrs={'autocomplete':'off'}
        self.fields['state'].widget.attrs={'autocomplete':'off'}
        self.fields['city'].widget.attrs={'autocomplete':'off'}



class DonateTrans(forms.ModelForm):

    userid = forms.IntegerField()
    donationdate = forms.DateField(widget=DateInput(), label="Donation Date")
    donationtime = forms.TimeField(widget=TimeInput(), label="Donation Time")
    units = forms.IntegerField(label="Units")
    shelflife = forms.IntegerField(label="Life")

    class Meta:
        model = BloodDonerTransactions
        fields = ['donationdate','donationtime','units','shelflife']
        exclude = ['userid']

    def __init__(self, *args, **kwargs):
        super(DonateTrans, self).__init__( *args, **kwargs)
        
        self.fields['userid'].widget.attrs={"autocomplete":'off', 'required':'false'}
        
        self.fields['donationdate'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['donationtime'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['units'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['shelflife'].widget.attrs={"autocomplete":'off', 'required':'true'}
        
class CampaignMaster(forms.ModelForm):
    campaignname = forms.CharField(max_length=200, label="Campaign Name")
    sdate = forms.DateField(widget=DateInput(), label="Start Date")
    stime = forms.TimeField(widget=TimeInput(), label="Start Time")
    edate = forms.DateField(widget=DateInput(), label="End Date")
    etime = forms.TimeField(widget=TimeInput(), label="End Time")
    location = forms.CharField(max_length=30, label="Location")
    city = forms.CharField(max_length=30, label="City")

    class Meta:
        model = CampaignMst
        fields = ['campaignname', 'sdate', 'stime','edate','etime', 'location','city']

    def __init__(self, *args, **kwargs):
        super(CampaignMaster, self).__init__(*args, **kwargs)
        self.fields['campaignname'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['sdate'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['stime'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['edate'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['etime'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['location'].widget.attrs={"autocomplete":'off', 'required':'true'}
        self.fields['city'].widget.attrs={"autocomplete":'off', 'required':'true'}


class StateCityMasterForm(forms.ModelForm):
    state_code = forms.CharField(max_length=3)
    state_name = forms.CharField(max_length=30)
    city_name = forms.CharField(max_length=40)
    zipcode = forms.CharField(max_length=6)

    class Meta:
        model = StateCityMaster
        fields = ['state_code','state_name','city_name', 'zipcode']
