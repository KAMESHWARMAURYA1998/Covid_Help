
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from bedavaibility import views
from bedavaibility.views import HospitalDetailView

urlpatterns = [
    path('',views.home ,name='home'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(),name="hospital_detail")
]
