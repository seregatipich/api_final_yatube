### Описание проекта API для Yatube:

REST API для социальной сети Yatube. 
Социальная сеть и API разработаны в рамках учебного проекта Яндекс. Практикума.

Позволяет делать запросы к моделям проекта: Посты, Группы, Комментарии, Подписчики.

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

### Технологии
Python 3.7, Django 3.2, DRF, JWT + Djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Dreesdree/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```
### Примеры запросов:

Пример POST-запроса для аутентифицированного пользователя: добавление нового поста.
POST .../api/v1/posts:

```
{
    "text": "Тестовый пост 1",
    "group": 1
}
```

Пример ответа:

```
{
    "id": 1,
    "author": "Alina",
    "text": "Тестовый пост 1",
    "pub_date": "2021-12-22T16:11:54.331905Z",
    "image": null,
    "group": 1
}
```

Пример POST-запроса для аутентифицированного пользователя: отправляем новый комментарий к посту с id=1.
POST .../api/v1/posts/1/comments/

```
{
    "text": "Тестовый комментарий к посту",
}
```

Пример ответа:

```
{
    "id": 1,
    "author": "Alina",
    "post": 1,
    "text": "Тестовый комментарий к посту",
    "created": "2021-12-22T16:14:15.159786Z"
}
```

Пример GET-запроса для любого пользователя: получаем информацию о группе.
GET .../api/v1/groups/1/

Пример ответа:

```
{
    "id": 1,
    "title": "Тестовая группа",
    "slug": "test",
    "description": "Тестовое описание группы"
}
```

Запустить проект:

```
python3 manage.py runserver
```