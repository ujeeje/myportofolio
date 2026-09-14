from django.urls import path

from main.views import show_main, show_experience, show_ctf_blog

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('ctf/', show_ctf_blog, name='show_ctf_blog'),
]