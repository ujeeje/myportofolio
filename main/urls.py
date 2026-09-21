from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_ctf_blog,
    create_writeup,
    get_writeups_json,
    delete_writeup,
    create_experience,
    update_experience,
    delete_experience,
    get_experiences_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("ctf/", show_ctf_blog, name="show_ctf_blog"),
    path("ctf/add/", create_writeup, name="create_writeup"),
    path("api/ctf/", get_writeups_json, name="get_writeups_json"),
    path("ctf/<uuid:writeup_id>/delete/", delete_writeup, name="delete_writeup"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experiences_json, name="get_experiences_json"),
]