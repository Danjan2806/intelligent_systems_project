from django.contrib import admin
from .models import Presentation, ProjectUpdate, ProjectUpdateImage, TestCaseEntry, TestCaseImage

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
# Register your models here.
