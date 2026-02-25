from django.shortcuts import render
from .models import Presentation, ProjectUpdate

# Главная страница
def home_view(request):
    return render(request, 'home.html')

# Страница презентаций
def presentations_view(request):
    presentations = Presentation.objects.all().order_by('-created_at')
    return render(request, 'presentations.html', {'presentations': presentations})

# Страница управления проектом
def project_management_view(request):
    updates = ProjectUpdate.objects.all().order_by('created_at')
    return render(request, 'project_management.html', {'updates': updates})

# Страница документации
def documentation_view(request):
    return render(request, 'documentation.html')

# Страница тестирования
def testing_view(request):
    return render(request, 'testing.html')
# Create your views here.
