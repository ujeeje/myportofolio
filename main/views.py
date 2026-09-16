from django.shortcuts import render

from main.models import Experience
from main.models import CTFWriteup
from main.forms import CTFWriteupBlog

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def show_main(request):
    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "npm": "2506614795",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada keamanan siber, ilmu forensik, dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_ctf_blog(request):
    writeups = CTFWriteup.objects.all()
    context = {
        "name": "Jefry Acmal Dzikhrullah",
        'writeups': writeups
    }
    return render(request, 'ctf_blog.html', context)

def create_writeup(request):
    form = CTFWriteupBlog(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Write-up baru berhasil ditambahkan!")
        return redirect("main:show_ctf_blog")

    context = {
        "name": "Jefry",
        "form": form,
    }
    return render(request, "writeup_form.html", context)