from django.urls import path
from . import views

urlpatterns = [
    path("submit/", views.submit_request, name="submit_request"),
    path("track/<int:request_id>/", views.track_request, name="track_request"),
]
