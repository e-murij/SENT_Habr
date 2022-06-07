# SENT HABR

[https://sent-project.ru/](https://sent-project.ru/)  - pусскоязычный веб-сайт в формате системы тематических коллективных блогов, созданный для публикации новостей, аналитических статей, мыслей, связанных с направлениями обучения в образовательной компании

На сайте реализованы системы регистрации, авторизации пользователей, возможность добавлять информацию о себе, личный кабинет пользователя

Зарегистрированные пользователи могут создавать свои статьи, оценивать и комментировать статьи других авторов

Реализована система уведомлений пользователей об откликах/оценках на их статьи

### Локальный запуск проекта 

Клоноровать репозиторий 

```
git clone https://github.com/e-murij/SENT_Habr.git
```
Установить необходимые для проекта пакеты

```
pip install -r requirements.txt
```

Перейти в папку SENT_HABR, переименовать файл .env.template в .env и заполнить его своими данными

```
EMAIL_HOST='smtp.email-domain.com'
EMAIL_HOST_USER='yourusername@youremail.com'
EMAIL_HOST_PASSWORD='your_password'
SECRET_KEY='your_secret_key'
DOMAIN_NAME='http://localhost:8000'
```

Перейти на уровень выше, в директроию, в которой находится файл manage.py
В терминале выполнить следующие команды

```
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver --settings=SENT_HABR.settings_dev  
```
По умолчанию приложение запуститься на http://localhost:8000
Можно указать другой порт

```
python manage.py runserver 7000
```

## Тестирование

Для проверки работоспособности и доступности страниц приложения можно запустить автотесты

```
python manage.py test
```
