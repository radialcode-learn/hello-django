from django.urls import path
from hello import views


urlpatterns = [
    path("logs", views.home_list_view),
    path("logs/create", views.home_list_view, name="log"),
]
