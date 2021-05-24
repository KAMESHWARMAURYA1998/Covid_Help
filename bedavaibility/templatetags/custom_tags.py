from bedavaibility.models import Availability
from django import template


register = template.Library()

@register.simple_tag
def getvalue(value):
    if value :
        return 'bg-success'
    return 'bg-danger'



@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital = hospital).order_by('facility_id')



@register.simple_tag
def is_state_selected(selected_state, pk):
    
    if selected_state ==str(pk) :

        return 'selected'
    return ''

@register.simple_tag
def is_city_selected(selected_city_id, pk) :
  
    
    if selected_city_id ==str(pk) :
        return 'selected'
    return ''

@register.simple_tag
def is_facility_selected(selected_facility_id, pk) :
  
    
    if selected_facility_id ==str(pk) :
        return 'selected'
    return ''