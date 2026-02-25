from django.shortcuts import render
from .models import Presentation, ProjectUpdate, TestCaseEntry, GitUpdate
from django.http import FileResponse, Http404
from django.conf import settings

# Главная страница
def home_view(request):
    return render(request, 'home.html')

# Страница презентаций
def presentations_view(request):
    presentations = Presentation.objects.all().order_by('-created_at')
    return render(request, 'presentations.html', {'presentations': presentations})

def download_presentation_view(request, pk):
    try:
        presentation = Presentation.objects.get(pk=pk)
        return FileResponse(presentation.file.open('rb'), as_attachment=True, filename=presentation.file.name)
    except Presentation.DoesNotExist:
        raise Http404("Презентация не найдена")

# Страница управления проектом
def project_management_view(request):
    updates = ProjectUpdate.objects.all().order_by('created_at')
    return render(request, 'project_management.html', {'updates': updates})

# Страница документации
def documentation_view(request):
    return render(request, 'documentation.html', {'MEDIA_URL': settings.MEDIA_URL})

# Страница тестирования
def testing_view(request):
    tests = TestCaseEntry.objects.prefetch_related('images').all()
    git_update = GitUpdate.objects.first()  # берём первую карточку Git (или фильтр по title)
    
    context = {
        'tests': tests,
        'git_update': git_update,  # теперь шаблон сможет получить скриншоты
    }
    return render(request, 'testing.html', context)
# Create your views here.
