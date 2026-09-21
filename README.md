# Yatube API

## Описание:

REST API для блоговой платформы с системой постов, комментариев, подписок и сообществ. Реализовано в соответствии с технической документацией Redoc, поддерживает полный CRUD-функционал с проверкой прав доступа.

## Установка:

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/x3au4ukx/api-final-yatube.git
```

```
cd api-final-yatube
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py migrate
```

### Запустить проект:

```
python manage.py runserver
```

## Примеры:

### Получение публикаций

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
### Список сообществ

```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
### Подписки

```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```

## Планы по доработке

- Добавить аутентификацию через JWT.
- Реализовать систему лайков и рейтингов для постов.
- Добавить кэширование часто запрашиваемых данных.
- Настроить документацию через Swagger.

## Выводы

В ходе работы над проектом я:
- Освоил Django REST Framework для создания RESTful API.
- Научился проектировать модели данных и связи между ними.
- Реализовал полный CRUD-функционал с проверкой прав доступа.
- Настроил пагинацию и фильтрацию для списков объектов.

Проект показал, как важно продумывать архитектуру API на этапе проектирования.
