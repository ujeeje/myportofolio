from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import CTFWriteup

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "On-going")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience added")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Done")
        self.assertNotContains(response, "On-going")

class CTFBlogTest(TestCase):
    def setUp(self):
        self.ctf_writeup = CTFWriteup.objects.create(
            title="Pekan RISTEK 2025",
            description="Kompetisi ini diselenggarakan oleh RISTEK FASILKOM UI 2025",
            pdf_filename="Write up CTF Pekan RISTEK 2025_KITA INI BANGSA YANG BESAR.pdf"
        )

    def test_ctf_url_is_accessible(self):
        response = self.client.get(reverse("main:show_ctf_blog"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ctf_blog.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_ctf_writeup_model(self):
        self.assertEqual(str(self.ctf_writeup), "Pekan RISTEK 2025")
        self.assertEqual(self.ctf_writeup.pdf_filename, "Write up CTF Pekan RISTEK 2025_KITA INI BANGSA YANG BESAR.pdf")

    def test_ctf_blog_page_with_data(self):
        response = self.client.get(reverse("main:show_ctf_blog"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ctf_writeup.title)
        self.assertContains(response, self.ctf_writeup.description)
        self.assertContains(response, self.ctf_writeup.pdf_filename)
        self.assertContains(response, "Buka Dokumen PDF")

    def test_empty_ctf_blog_page(self):
        CTFWriteup.objects.all().delete()
        response = self.client.get(reverse("main:show_ctf_blog"))

        self.assertContains(response, "Belum ada CTF writeup yang dipublikasikan saat ini.")
        self.assertNotContains(response, "Buka Dokumen PDF")

    def test_ctf_writeup_without_pdf(self):
        self.ctf_writeup.pdf_filename = ""
        self.ctf_writeup.save()
        response = self.client.get(reverse("main:show_ctf_blog"))

        self.assertContains(response, "Berkas PDF belum tersedia.")
        self.assertNotContains(response, "Buka Dokumen PDF")