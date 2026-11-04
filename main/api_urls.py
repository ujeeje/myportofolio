from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
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