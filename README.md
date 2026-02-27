# Итоговый проект "Интеллектуальные системы и технологии"

Проект демонстрирует принципы управления IT-проектами, работу с Agile/Kanban, интеграцию мультимедийных материалов и разработку адаптивного веб-сайта на Django с использованием Bootstrap.

---

Структура проекта

- `core/` — основное приложение:
  - `migrations` — миграции в БД
  - `models.py` — модели Presentation и ProjectUpdate
  - `templates/` — HTML-шаблоны (base.html, home.html, presentations.html и др.)
  - `static/` — CSS, видео и презентации
- `intelligent_systems_project/` — настройки проекта Django
- `media/` — загружаемые презентации и скриншоты проекта (через админку)
- `db.sqlite3` — база данных SQLite (не хранить в Git для большого проекта)
- `venv/` — виртуальное окружение Python (не хранить в Git)

---

Требования

- Python 3.12+
- Django 6.0+
- Pillow (для ImageField)
- Bootstrap 5 (подключается через CDN)
- Любой современный браузер для просмотра страниц

---

Установка и запуск проекта

1. Клонируем репозиторий

```bash
git clone https://github.com/Danjan2806/intelligent_systems_project.git
cd intelligent_systems_project
```

2. Создаём и активируем виртуальное окружение
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python -m venv venv
source venv/bin/activate
```

3. Устанавливаем зависимости
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Устанавливаем Pillow (если не в requirements.txt)
```bash
pip install Pillow
```

5. Создаём и применяем миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Создаём суперпользователя для админки
```bash
python manage.py createsuperuser
```
7. Проводим тесты работы сайта
```bash
python manage.py test
```

8. Запускаем сервер разработки
```bash
python manage.py runserver
```

9. Открываем проект в браузере
```bash
http://127.0.0.1:8000/
```


Админка Django

- URL: /admin/
- Через админку можно добавлять:
    - Презентации (Presentation)
    - Этапы проекта и скриншоты (ProjectUpdate)
    - Скриншоты GitHub'а и всякое подобное (Git screenshots и Git updates)
Файлы презентаций и скриншоты будут храниться в папке media/.

Статика и мультимедиа
- CSS и JS — core/static/css/style.css и подключённые файлы Bootstrap
- Видео-фон — core/static/videos/background_video.mp4
- Презентации — core/static/presentations/ (для быстрого теста)
- Скриншоты — загружаются через админку в media/project_updates/

