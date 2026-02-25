from django.test import TestCase, Client
from django.urls import reverse
from core.models import Presentation, ProjectUpdate
from django.core.files.uploadedfile import SimpleUploadedFile

class ExtendedSiteTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Создание тестовой презентации
        pdf_content = b"%PDF-1.4 test pdf content"
        self.presentation = Presentation.objects.create(
            title="Тестовая презентация",
            description="Описание тестовой презентации",
            file=SimpleUploadedFile("test.pdf", pdf_content, content_type="application/pdf")
        )

        # Создание тестового обновления проекта
        image_content = b"fake image content"
        self.update = ProjectUpdate.objects.create(
            title="Тестовое обновление",
            description="Описание обновления проекта"
        )
        # Для слайдера добавим одно изображение
        self.update_image = self.update.images.create(
            image=SimpleUploadedFile("test_image.png", image_content, content_type="image/png")
        )

    def test_homepage_status(self):
        """Главная страница возвращает 200 и содержит ключевой текст"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Интеллектуальные системы и технологии")

    def test_presentations_page_status_and_content(self):
        """Страница презентаций открывается, PDF отображается и доступен для скачивания"""
        response = self.client.get(reverse('presentations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.presentation.title)
        self.assertContains(response, "Просмотр")
        self.assertContains(response, "Скачать")

    def test_pdf_download_view(self):
        """Файл презентации доступен для скачивания через view"""
        url = reverse('download_presentation', args=[self.presentation.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_project_management_page_status_and_content(self):
        """Страница управления проектом открывается и содержит слайдер с изображением"""
        response = self.client.get(reverse('project_management'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.update.title)
        self.assertContains(response, self.update.description)
        # Проверяем наличие тега img для слайдера
        self.assertContains(response, 'carousel')

    def test_project_update_slider_image(self):
        """Слайдер на странице проекта корректно отображает загруженные изображения"""
        response = self.client.get(reverse('project_management'))
        # Проверяем наличие изображения с файла проекта
        self.assertContains(response, self.update_image.image.name)
# Create your tests here.
