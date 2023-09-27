from django.views.generic import ListView, CreateView, DetailView

from cars.forms import CarModelForm
from cars.models import Car


# CLASS BASED VIEWS
# class CarsView(View):
#     def get(self, request):
#         query = request.GET
#         cars = []
#         if query.get("search"):
#             cars = Car.objects.filter(model__icontains=query.get("search")).order_by(
#                 "model"
#             )
#         else:
#             cars = Car.objects.all().order_by("-model")
#         return render(request, template_name="cars.html", context={"cars": cars})


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


# class NewCarView(View):
#     @staticmethod
#     def get(request):
#         new_car_form = CarModelForm()
#         return render(request, template_name="new_car.html", context={"new_car_form": new_car_form})
#
#     @staticmethod
#     def post(request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, template_name="new_car.html", context={"new_car_form": new_car_form})


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

# FUNCTION BASED VIEWS
# Create your views here.
# @require_http_methods(["GET"])
# def cars_view(request):
#     query = request.GET
#     cars = []
#     if query.get("search"):
#         cars = Car.objects.filter(model__icontains=query.get("search")).order_by(
#             "model"
#         )
#     else:
#         cars = Car.objects.all().order_by("-model")
#     return render(request, template_name="cars.html", context={"cars": cars})


# def new_car_view(request):
#     if request.method == "POST":
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, template_name="new_car.html", context={"new_car_form": new_car_form})
