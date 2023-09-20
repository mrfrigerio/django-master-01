from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from cars.models import Car


# Create your views here.
@require_http_methods(["GET"])
def cars_view(request):
    query = request.GET
    cars = []
    if query.get("search"):
        cars = Car.objects.filter(model__icontains=query.get("search")).order_by(
            "model"
        )
    else:
        cars = Car.objects.all().order_by().order_by("-model")
    return render(request, template_name="cars.html", context={"cars": cars})


def new_car_view(request):
    return 'Novo Carro'
