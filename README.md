# Job_life
1. Склонируйте себе проект, если нужно через ssh это делать, сбросьте ssh ключ Братчикову.
2. Создайте файл .env и скопируйте в него содержимое .env.example
3. Сгенерируйте secret_key с помощью следующего кода:
```python
    from django.core.management.utils import get_random_secret_key  
    get_random_secret_key()
```
4. Скопируйте сгенерированный ключ в переменную SECRET_KEY в ваш .env файл.
5. Если необходимо, поменяйте в .env файле SQL_USER и SQL_PASSWORD.
6. Поменяйте логин и пароль админа для Grafana.
7. В терминале запустите команду docker-compose up -d --build
8. После успешного создания контейнеров и запуска серверов создайте суперюзера через терминал.
```

    docker ps
    # скопируйте id контейреа web
    docker exec -it container_id python manage.py createsuperuser
    # где container_id - это id контейнера web, который вы скопировали
```