from django.shortcuts import render
import folium
from .models import Localisation


# Create your views here.
def index(request):
    # localisations = Localisations.objects.all()

    # Create a folium map carte centred on Chelles
    m = folium.Map(location=[48.866667, 2.333333], zoom_start=9)

    # Add a marker to the map for each location
    for localisation in Localisation.objects.all():
        folium.Marker(location=[localisation.latitude, localisation.longitude],
                      popup=localisation.ville,
                      ).add_to(m)


    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)
