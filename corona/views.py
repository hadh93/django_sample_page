from django.http import HttpResponse
from django.template import loader

from .scripts import corona_city, corona_data

# Create your views here.

def index(request):
    template = loader.get_template('corona/corona_index.html')
    context = { 'corona_data': corona_data.get_corona_summary()
    ,'corona_city':corona_city.get_city_data() }
    return HttpResponse(template.render(context, request))
