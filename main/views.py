from django.shortcuts import render

from main.models import Experience
from main.models import CTFWriteup


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
        "name": "Jefry",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_ctf_blog(request):
    writeups = CTFWriteup.objects.all()
    context = {
        'writeups': writeups
    }
    return render(request, 'ctf_blog.html', context)