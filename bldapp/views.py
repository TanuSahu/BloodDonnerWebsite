from email import message
from tkinter.ttk import LabeledScale
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CampaignMaster, userRegistration, userProfileAdd, userProfileDisable, DonateTrans, StateCityMasterForm
import random

from datetime import datetime

# import the models

from .models import CampaignMst, UserProfile, StateCityMaster


# Create your views here.

'''
class indexPage():
    context = None
    template_name = 'indexpage.html'

'''
def indexPage(request):
    return render(request,
        'indexpage.html',
        None
        )

def aboutUs(request):
    return render(request,
    'aboutUs.html',
    None
    )

class Authentication:
    def login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    context = {'message': 'User Status is Invalid. Contact Admin..'}
                    return render(request, 'errorPages/usererror.html', context)
            else:
                context = {'message': 'User / Password is incorrect OR User does not exists.'}
                return render(request, 'errorPages/usererror.html', context)
        else:
            return render(request, 'registrations/login.html')


    def register(request):
        if request.method == "POST":
            form = userRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.save()

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(request, username=user.username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = userRegistration()
        return render(request,'registrations/register.html', {'form': form})


def userProfile(request):
    # fetch the existing data and display

    try:
        data = UserProfile.objects.get(userid = request.user)
        userform = userProfileDisable(instance = data)
    except:
        messages.success(request,'Profile Needs Updation')
        userform = userProfileDisable()

    return render(request, 
                  'userProfile.html',
                  {'userform': userform}

                  )


def validateDate(datein):
    dtfmt = "%d/%m/%Y %H:%M:%S.%f"
    d = datetime.strftime(datein, dtfmt)    
    indate = datetime.strptime(d, dtfmt)
    currdate = datetime.now()
    diffdate = currdate - indate
    return round(diffdate.days / 365)


def modifyProfile(request):
     # code to update the user profile
    try:
        data = UserProfile.objects.get(userid = request.user)
    except:
        data = None
   
    if request.method == "POST":
        if data:
            userform = userProfileAdd(request.POST, instance = data)
        else:
            userform = userProfileAdd(request.POST)

        if userform.is_valid():
            profile = userform.save(commit=False)
            # validate the date, difference in years should be > 18
            # year range 1960 - 2004
            if validateDate(profile.dob) < 18:
                messages.error(request,'Date is invalid!! Donner Should be 18 years and above')
                return redirect('userProfile')
            profile.userid = request.user
            profile.save()
            messages.success(request,'Data Saved Successfully')
            return redirect('userProfile')
        else:
            messages.success(request,'Error in Data! Please Check')
            return redirect('userProfile')
           
    else:
        if data:
            userform = userProfileAdd(instance=data)
        else:
            userform = userProfileAdd()
    return render(request, 'userProfile.html', {'userform': userform} )


def chart_colors(l):
    color_list = []
    for _ in range(l):
        r = str(random.randint(0, 256))
        b = str(random.randint(0, 256))
        g = str(random.randint(0, 256))
        rgb = f"{r},{g},{b}"

        color_list.append(rgb)
    return color_list


def dashboard(request):
    dLabels = ['A','A+','B','B+']
    cdata = [10, 13, 13, 23]

    # queries to extract data from models

    clist = chart_colors(len(dLabels))
    print()
    context = {'dLabels': dLabels, 'cdata': cdata, 'ccolor': chart_colors}


    return render(request,
            'dashboard.html',
            context
            )


def donateTrans(request):

    if request.method == "POST":
        form = DonateTrans(request.POST)
       
        if form.is_valid():
            mform = form.save(commit=False)
            mform.userid = request.user
            mform.save()
            messages.success(request, "Data Saved Successfully")
            return redirect('donate')

        else:
            messages.error(request, "Invalid Data")
            return redirect('donate')

    dform = DonateTrans(initial={'userid':request.user.id})
    return render(request, 'donateForm.html', {"dform": dform})


def masterForm(request):
    return render(request,
                  'masters.html',
                  None)


def CampaignForm(request):

    data = CampaignMst.objects.all()

    if request.method == "POST":
        form = CampaignMaster(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Saved Successfully")
            return redirect("masters")
    form = CampaignMaster()    
    return render(request,
                  'campaign.html',
                  {'form': form, 'data': data})

def CityStateForm(request):
    data = StateCityMaster.objects.all()

    if request.method=="POST":
        form = StateCityMasterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Saved Successfully")
            return redirect("masters")
    form = StateCityMasterForm()
    return render(request,
                  'citystate.html',
                  {'form': form, 'data': data})
