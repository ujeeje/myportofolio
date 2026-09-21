from django.forms import ChoiceField, ModelForm, Select, TextInput, Textarea, URLInput
from django.utils import timezone

from main.models import Experience
from main.models import CTFWriteup

class ExperienceForm(ModelForm):
    status = ChoiceField(
        choices=[
            ("ongoing", "On-going"),
            ("done", "Done"),
        ],
        label="Status",
        widget=Select(),
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "status",
        ]

        labels = {
            "title": "Judul Experience",
            "description": "Deskripsi",
            "category": "Kategori",
            "status": "Status",
        }

        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Teaching Assistant Coordinator",
                "maxlength": 255,
            }),
            "description": Textarea(attrs={
                "placeholder": "Ceritakan experience kamu",
                "rows": 3,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["status"].initial = (
                "ongoing" if self.instance.is_ongoing else "done"
            )

    def save(self, commit=True):
        experience = super().save(commit=False)
        status = self.cleaned_data.get("status")

        if status == "ongoing":
            experience.ended_at = None
        elif status == "done" and experience.ended_at is None:
            experience.ended_at = timezone.now()

        if commit:
            experience.save()

        return experience

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
