from django.contrib import admin
from bedavaibility.models import Facility, State, City, Hospital, Availability
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save,sender=Hospital)
def afterHospitalSave(signal, instance, **keyargs):
    facilities = Facility.objects.all()
    for facility in facilities:
        availability = Availability(hospital = instance, facility = facility)
        availability.save()
    


@receiver(post_save,sender=Facility)
def afterFacilitySave(signal, instance, **keyargs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availability = Availability(hospital = hospital, facility = instance)
        availability.save()



class FacilityAdmin(admin.ModelAdmin):

    model = Facility
    # list_display = ['hospital','bed_availability',
    #                            'bed_total',
    #                            'oxygen_availability',
    #                            'oxygen_total',
    #                            'ventilator_avvailibility',
    #                            'ventilator_total']

    list_display = ['title'
                     ]

    # def bed(self , object):
    #     return f'{object.bed_availability}/{object.bed_total}'

    # def oxygen(self , object):
    #     return f'{object.oxygen_availability}/{object.oxygen_total}'


    # def ventilator(self , object):
    #     return f'{object.ventilator_avvailibility}/{object.ventilator_total}'

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name','address','city','phone']


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name','state']


class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital','facility','total','available','updated_at']
    list_editable = ['total','available']





admin.site.register(State)
admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability, AvailabilityAdmin)