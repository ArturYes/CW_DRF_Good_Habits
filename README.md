# Трекер полезных привычек

## Описание проекта:

SPA веб-приложения трекер полезных привычек. Проект создан для приобретения полезных привычек. Вы можете создавать привычки, выставлять периодичность и время выполнения и вам будет приходить уведомление в телеграм.

### Описание задач
- Добавлены необходимые модели привычек;
- Реализованы эндпоинты для работы с frontend;
- Создано приложение для работы с Telegram и рассылками напоминаний.

### В проекте имеется:
    - CORS.
    - Интеграция с Telegram.
    - Пагинация.
    - Переменные окружения.
    - Описаны модели, реализованы эндпоинты и настроены валидаторы
    - Описанные права доступа.
    - Отложенные задачи через Celery.
    - Проект покрыт тестами

### Технологии
- Django
- PostgreSQL
- DRF
- Celery
- Redis
- CORS


## Настройка проекта
Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта
Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone https://github.com/ArturYes/CW_DRF_Good_Habits
  ```

### 2. Настройка виртуального окружения и установка зависимостей

#### Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

#### Инструкция для работы через виртуальное окружение - pip:
```text
Команда для Windows:
    - python -m venv venv
    - venv\Scripts\activate
    - pip install -r requirement.txt

Команда для Unix:
    - python3 -m venv venv
    - source venv/bin/activate 
    - pip install -r requirement.txt
```

### 3. Для запуска redis:
Redis официально не поддерживается в Windows: 
- Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
- sudo apt-get update (обновление)
- sudo service redis-server start
- redis-cli
- Проверка работает ли сервер Redis: введите Ping, ответ от сервера: Pong
- в IDE через командную строку установите redis: pip install redis

Команда для Unix:
```text
redis-cli
```


### 4. Для запуска celery:
Команда для Windows:
- при указании обработчика событий необходимо добавить флаг -P eventlet
- celery -A config worker -l INFO -P eventlet
- celery -A my_project beat —loglevel=info

Команда для Unix:
- celery -A config worker --loglevel=info
- celery -A my_project beat —loglevel=info

### 5. Редактирование .env.example:
В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
```text
# Settings database
POSTGRES_ENGINE=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

# Settings Django/DRF
SECRET_KEY=
DEBUG=

# Settings Redis
REDIS_URL=

# Telegram API
TELEGRAM_BOT_API=
```

### 6. Настройте базу данных:
- Создать миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```

### 7. Для создания администратора (createsuperuser)
```text
python manage.py create_su
```

### 8. Для запуска приложения:
```
Команда для Windows:
- python manage.py runserver

Команда для Unix:
- python3 manage.py runserver
```

### Документация проекта:
- http://127.0.0.1:8000/swagger/
