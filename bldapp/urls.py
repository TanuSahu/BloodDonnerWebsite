from django.urls import path
from .views import indexPage, userProfile, aboutUs, dashboard, modifyProfile, donateTrans, masterForm, CampaignForm, CityStateForm

urlpatterns = [
    path('', indexPage, name="home" ),
    path('aboutUs/', aboutUs, name="aboutUs"),
    path('dashboard/', dashboard, name="dashboard"),
    
    path('userProfile/', userProfile, name="userProfile"),
    path('modifyProfile/', modifyProfile, name="modifyProfile"),
    path('donate/', donateTrans, name="donate"),
    path('masters/', masterForm, name='masters'),

    path('citystate/', CityStateForm, name="citystate"),
    path('campaign/', CampaignForm, name="campaign"),

]
