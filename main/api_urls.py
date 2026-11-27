from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from main import api_views

app_name = "api"

urlpatterns = [
    path(
        "auth/token/",
        authtoken_views.obtain_auth_token,
        name="api_token_auth",
    ),
    path("auth/logout/", api_views.api_logout, name="api_logout"),
    path("projects/", api_views.project_list, name="project-list"),
    path("experiences/", api_views.experience_list, name="experience-list"),
    path(
        "ctf-writeups/",
        api_views.ctfwriteup_list,
        name="ctfwriteup-list",
    ),
    path(
        "ctf-writeups/<uuid:writeup_id>/",
        api_views.ctfwriteup_detail,
        name="ctfwriteup-detail",
    ),
    path(
        "ctf-writeups/<uuid:writeup_id>/star/",
        api_views.ctfwriteup_star,
        name="ctfwriteup-star"
    ),
]
