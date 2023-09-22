from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from cars.forms import CarModelForm
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
        cars = Car.objects.all().order_by("-model")
    return render(request, template_name="cars.html", context={"cars": cars})


def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, template_name="new_car.html", context={"new_car_form": new_car_form})
