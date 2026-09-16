from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import CTFWriteup

class CTFWriteupBlog(ModelForm):
    class Meta:
        model = CTFWriteup
        fields = [
            "title",
            "description",
            "writeup_url",
        ]

        labels = {
            "title": "Nama Event",
            "description": "Deskripsi Write-Up",
            "writeup_url": "URL Write-up",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Apa event yang kamu ikuti?",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan apa yang kamu lakukan",
                    "rows": 3,
                }
            ),
            "writeup_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/.../",
                }
            ),
        }