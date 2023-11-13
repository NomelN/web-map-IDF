from django.shortcuts import render
import folium
from .models import Localisation
from folium.plugins import FastMarkerCluster

# Create your views here.
def index(request):
    # localisations = Localisations.objects.all()

    # Create a folium map carte centred on Chelles
    m = folium.Map(location=[48.866667, 2.333333], zoom_start=12)

    # Create a FastMarkerCluster and add it to the map
    marker_cluster = FastMarkerCluster(data=[]).add_to(m)

    # Add a marker to the map for each location
    for localisation in Localisation.objects.all():
        popup_content = {
            'Label VVF': localisation.label_vvf,
            'Ville': localisation.ville,
            }
        if localisation.label_vvf == "4 fleurs":
            folium.Marker(
                location=[localisation.latitude, localisation.longitude],
                popup=popup_content,
                icon=folium.Icon(color='green')
            ).add_to(marker_cluster)
        elif localisation.label_vvf == "3 fleurs":
            folium.Marker(
                location=[localisation.latitude, localisation.longitude],
                popup=popup_content,
                icon=folium.Icon(color='orange')
            ).add_to(marker_cluster)
        elif localisation.label_vvf == "2 fleurs":
            folium.Marker(
                location=[localisation.latitude, localisation.longitude],
                popup=popup_content,
                icon=folium.Icon(color='purple')
            ).add_to(marker_cluster)
        elif localisation.label_vvf == "1 fleur":
            folium.Marker(
                location=[localisation.latitude, localisation.longitude],
                popup=popup_content,
                icon=folium.Icon(color='darkgreen')
            ).add_to(marker_cluster)

    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)
