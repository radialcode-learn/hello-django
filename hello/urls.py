from django.urls import path
from hello import views


urlpatterns = [
    path("", views.home_list_view),
    path("log/", views.home_list_view, name="log"),
]
