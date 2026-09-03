from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

def health(_request):
    return JsonResponse({"status": "ok", "service": "extreme-api"})

urlpatterns = [path("health/", health), path("admin/", admin.site.urls), path("api/auth/login/", obtain_auth_token), path("api/", include("clients.urls"))]
