from django.shortcuts import render, get_object_or_404
from stop_stations.models import Route, Station

# Create your views here.

def home(request):

    def get_center(coordinats):
        min_cor = min(coordinats)
        max_cor = max(coordinats)
        delta = (max_cor - min_cor) / 2
        return min_cor + delta

    if 'route' in request.GET:
        route = get_object_or_404(Route, name=request.GET['route'])
        stations = Station.objects.prefetch_related('routes')\
            .filter(routes=route).all()

        latitudes = [obj.latitude for obj in stations]
        longitudes = [obj.longitude for obj in stations]

        context={
            'routes': Route.objects.all(),
            'stations': stations,
            'route': route,
            'center': {
                'x': get_center(latitudes),
                'y': get_center(longitudes)
                }
        }
    else:
        context = {
            'routes': Route.objects.all(),
        }

    return render(
        request,
        'stop_stations/stations.html',
        context=context
    )
