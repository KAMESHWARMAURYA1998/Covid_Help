from django.shortcuts import render
from django.http.response import HttpResponse
from bedavaibility.models import Availability, Facility, Hospital,  State, City
from django.views import generic

# Create your views here.

class HospitalDetailView(generic.DetailView):
    model = Hospital




def home(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')
    
    
   
    
    

    facility = Facility.objects.all().order_by('pk');
    state = State.objects.all()
    if selected_state_id :
        city = City.objects.filter(state = selected_state_id)
    else:
   
        city = City.objects.all()
    

    
    


    if selected_city_id:
        
        hospital = Hospital.objects.filter(city= City(pk =selected_city_id ))

    else:
        hospital = Hospital.objects.all()



    if selected_facility_id :
        availabilities = Availability.objects.all()
        if selected_city_id :
            availabilities = Availability.objects.filter(hospital__city = City(pk = selected_city_id))
        availabilities = availabilities.filter(facility = Facility(pk = selected_facility_id), available__gt = 0)
        hospital = []
        for avl in availabilities :
            hospital.append(avl.hospital)
        

    context = {
        'facilities':facility,
        'states':state,
        'cities':city,
        'hospitals':hospital,
        'selected_state_id':selected_state_id ,
        'selected_city_id':selected_city_id,
        'selected_facility_id':selected_facility_id

    }
    return render(request,'index.html', context = context)
