from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import accounts.views
import cars.views

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("cars/", cars.views.CarsListView.as_view(), name="cars_list"),
                  path("new_car/", cars.views.NewCarCreateView.as_view(), name="new_car"),
                  path("car/<int:pk>/", cars.views.CarDetailView.as_view(), name="car_detail"),
                  path("register/", accounts.views.register_view, name="register"),
                  path("login/", accounts.views.login_view, name="login"),
                  path("logout/", accounts.views.logout_view, name="logout")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
