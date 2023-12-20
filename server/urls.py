from django.urls import path, include

BASE_URL = "api/v1/"

urlpatterns = [
    path(BASE_URL+ "auth/", include("authentication.urls"))
]
