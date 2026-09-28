from django.shortcuts import render

from main.models import Experience
from main.models import CTFWriteup
from main.forms import ExperienceForm
from main.forms import CTFWriteupBlog

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied  
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "npm": "2506614795",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada keamanan siber, ilmu forensik, dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    is_editor = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Editor").exists()
    )

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "experience_list": experiences,
        "title_query": title_query,
        "is_editor": is_editor,
    }
    return render(request, "experience.html", context)

def show_ctf_blog(request):
    title_query = request.GET.get("title", "").strip()
    writeups = CTFWriteup.objects.all()

    if title_query:
        writeups = writeups.filter(title__icontains=title_query)

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "writeups": writeups,
        "title_query": title_query,
    }

    return render(request, "ctf_blog.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(experiences_json, content_type="application/json")

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "form": form,
        "form_title": "Add New Experience",
        "button_label": "Create",
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    is_editor = request.user.groups.filter(name="Editor").exists()

    if not request.user.is_superuser and not is_editor:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "form": form,
        "form_title": "Edit Experience",
        "button_label": "Update",
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def create_writeup(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = CTFWriteupBlog(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Write-up baru berhasil ditambahkan!")
        return redirect("main:show_ctf_blog")

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "form": form,
    }
    return render(request, "writeup_form.html", context)

def get_writeups_json(request):
    title_query = request.GET.get("title", "").strip()
    writeups = CTFWriteup.objects.all()

    if title_query:
        writeups = writeups.filter(title__icontains=title_query)

    data = list(writeups.values(
        "id",
        "title",
        "description",
        "writeup_url",
    ))

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_writeup(request, writeup_id):
    if not request.user.is_superuser:
        raise PermissionDenied    
    
    writeup = get_object_or_404(CTFWriteup, pk=writeup_id)

    if request.method == "POST":
        writeup.delete()
        messages.success(request, "Write-up berhasil dihapus!")

    return redirect("main:show_ctf_blog")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, writeup_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    writeup = get_object_or_404(CTFWriteup, pk=writeup_id)

    if writeup.starred_by.filter(pk=request.user.pk).exists():
        writeup.starred_by.remove(request.user)
    else:
        writeup.starred_by.add(request.user)

    return redirect("main:show_ctf_blog")