from django.shortcuts import render

from main.models import Experience
from main.models import CTFWriteup
from main.forms import ExperienceForm
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
    json_response = get_experiences_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Jefry Acmal Dzikhrullah",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_ctf_blog(request):
    json_response = get_writeups_json(request)
    writeups = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    writeups = [writeup.object for writeup in writeups]
    title_query = request.GET.get("title", "").strip()

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

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_experience(request):
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

def update_experience(request, experience_id):
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

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")

    return redirect("main:show_experience")

def create_writeup(request):
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

    writeups_json = serializers.serialize("json", writeups)
    return HttpResponse(writeups_json, content_type="application/json")

def delete_writeup(request, writeup_id):
    writeup = get_object_or_404(CTFWriteup, pk=writeup_id)

    if request.method == "POST":
        writeup.delete()
        messages.success(request, "Write-up berhasil dihapus!")

    return redirect("main:show_ctf_blog")