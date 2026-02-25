from django.contrib import admin
from .models import Presentation, ProjectUpdate, ProjectUpdateImage, TestCaseEntry, TestCaseImage, GitUpdate, GitScreenshot

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

class ProjectUpdateImageInline(admin.TabularInline):
    model = ProjectUpdateImage
    extra = 1

@admin.register(ProjectUpdate)
class ProjectUpdateAdmin(admin.ModelAdmin):
    inlines = [ProjectUpdateImageInline]


class TestCaseImageInline(admin.TabularInline):
    model = TestCaseImage
    extra = 1

@admin.register(TestCaseEntry)
class TestCaseEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [TestCaseImageInline]

class GitScreenshotInline(admin.TabularInline):
    model = GitUpdate.screenshots.through  # для ManyToMany
    extra = 3  # сколько пустых полей для добавления сразу
    verbose_name = "Скриншот Git"
    verbose_name_plural = "Скриншоты Git"

@admin.register(GitUpdate)
class GitUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    inlines = [GitScreenshotInline]

@admin.register(GitScreenshot)
class GitScreenshotAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order']
# Register your models here.
