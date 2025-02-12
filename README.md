# Django Celery Project

Этот проект использует Django с интеграцией Celery и Redis для обработки фоновых задач.

## Функциональность проекта

- **Celery:** Асинхронная обработка задач.
- **Redis:** Используется как брокер сообщений для Celery.
- **Celery Beat:** Планирование и выполнение периодических задач.

## Установка и настройка

### Шаг 1: Клонирование репозитория

```bash
$ git clone <URL_репозитория>
$ cd <название_проекта>
```

### Шаг 2: Создание виртуального окружения

```bash
$ python -m venv .venv
$ source .venv/bin/activate  # Для Windows используйте .venv\Scripts\activate
```

### Шаг 3: Установка зависимостей

```bash
$ pip install -r requirements.txt
```

### Шаг 4: Настройка переменных окружения

Создайте файл `.env` в корне проекта и добавьте следующие настройки:

```env
CELERY_BROKER_URL=redis://127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
```

### Шаг 5: Запуск Redis

Убедитесь, что Redis установлен и запущен локально:

```bash
$ redis-server
```

### Шаг 6: Применение миграций базы данных

```bash
$ python manage.py migrate
```

### Шаг 7: Запуск Celery Worker

```bash
$ celery -A config worker --loglevel=info
```

Если вы используете Windows, рекомендуется использовать режим `solo`:

```bash
$ celery -A config worker --loglevel=info --pool=solo
```

### Шаг 8: Запуск Celery Beat (если используется)

```bash
$ celery -A config beat --loglevel=info
```

### Шаг 9: Запуск сервера Django

```bash
$ python manage.py runserver
```

## Использование

### Запуск задачи вручную
Вы можете запустить задачу, вызвав её из Django Shell:

```bash
$ python manage.py shell
```

```python
from habits.tasks import send_message_to_user
send_message_to_user.delay(123)
```

## Отладка

### Проблемы с подключением
Если Celery не может подключиться к Redis, проверьте, что Redis запущен и что переменная `CELERY_BROKER_URL` настроена правильно.

### Предупреждение о `broker_connection_retry`
Добавьте следующее в настройки проекта, чтобы избежать предупреждения:

```python
broker_connection_retry_on_startup = True
```

## Контакты
Для вопросов и предложений вы можете обратиться к автору проекта.

---

Спасибо за использование проекта!

