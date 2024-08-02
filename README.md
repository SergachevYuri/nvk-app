# NVK APP project

Запуск проекта
python manage.py runserver

# Миграция

python manage.py makemigrations
python manage.py migrate


docker compose up -d

docker compose run django python manage.py migrate

docker compose run django python manage.py createsuperuser