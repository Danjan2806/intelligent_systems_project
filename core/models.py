from django.db import models

class Presentation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='presentations/')
    preview_image = models.ImageField(upload_to='presentations/previews/', blank=True, null=True)  # превью первого слайда
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectUpdate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProjectUpdateImage(models.Model):
    update = models.ForeignKey(ProjectUpdate, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_updates/')
    order = models.PositiveIntegerField(default=0)  # Для сортировки

    def __str__(self):
        return f"{self.update.title} - Image {self.order}"

class TestCaseEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TestCaseImage(models.Model):
    test_case = models.ForeignKey(TestCaseEntry, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="test_cases/")

    def __str__(self):
        return f"Image for {self.test_case.title}"

class GitScreenshot(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)  # опциональный заголовок
    image = models.ImageField(upload_to='git_screenshots/')
    order = models.PositiveIntegerField(default=0)  # для сортировки

    def __str__(self):
        return f"{self.title or 'Screenshot'} ({self.order})"

class GitUpdate(models.Model):
    title = models.CharField(max_length=100, default="Контроль версий Git")
    description = models.TextField(blank=True, null=True)
    repository_link = models.URLField(blank=True, null=True)
    screenshots = models.ManyToManyField(GitScreenshot, blank=True, related_name='git_updates')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
