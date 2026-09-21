from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_ctf_blog,
    create_writeup,
    get_writeups_json,
    delete_writeup,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("ctf/", show_ctf_blog, name="show_ctf_blog"),
    path("ctf/add/", create_writeup, name="create_writeup"),
    path("api/ctf/", get_writeups_json, name="get_writeups_json"),
    path("ctf/<uuid:writeup_id>/delete/", delete_writeup, name="delete_writeup"),
]