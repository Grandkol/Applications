# Applications

## Запуск сервиса

1. Cкачайте репозиторий к себе на компьютер.

`git clone git@github.com:Grandkol/Applications.git`.

2. Создайте файл `.env` для переменных окружения в той же директории, что и `.env.example`, скопируйте из нее переменные или создайте свои по аналогии.
3. Запустите сборку docker сети контейнеров командой `docker-compose up -d --build`.
4. После запуска вы сможете найти сервисы по следующим адреса:
- FastAPI swagger: `http://localhost:8000/app/openapi`
- Kafka ui: `http://localhost:8080`
- PostgreSQL: необходимо будет скачать dbeaver/pgadmin и ввести там данные БД.

После всех этих шагов вы сможете свободно пользоваться сервисом заявок.

## Пример Запросов.

1. `POST /api/v1/applications` - запрос для добавления заявки. Произовдится загрузка в PostgreSQL и Kafka.

Тело запроса:
```html
{
  "user_name": "Тимофей", - имя пользователя, составившего заявку.
  "description": "Хочу купить рюкзак" - описания заявки.
}

```
Тело ответа:
```html
{
  "id": "1bbfeb94-cc31-41e7-9621-359aab5c12ab", - id заявки.
  "user_name": "Тимофей",
  "description": "Хочу купить рюкзак",
  "created_at": "2025-01-16T13:44:47.898688" - время создания заявки.
}

```

2. `GET /api/v1/applications` - запрос для выдачи заявок. Возможна фильтрация по полю `user_name`. Также реализована пагинация

 - `GET /app/v1/applications?page=1&size=50` - запрос 1 страницы по 50 объектов, без фильтрации по имени.

Тело ответа без фильтра:
```html
{
  "items": [
    {
      "id": "a1a0acc0-5319-434b-9c46-22c839a4c6a9",
      "user_name": "string",
      "description": "string",
      "created_at": "2025-01-15T22:02:45.036845"
    },
    {
      "id": "3bd44b15-c513-47c9-8912-b17172882853",
      "user_name": "adsadwa",
      "description": "stdddring",
      "created_at": "2025-01-15T22:04:22.165864"
    },
    {
      "id": "d555d75c-46b8-49bc-9728-3ae9706bf122",
      "user_name": "adsadwa",
      "description": "stdddring",
      "created_at": "2025-01-15T22:06:01.719038"
    },
    {
      "id": "1bbfeb94-cc31-41e7-9621-359aab5c12ab",
      "user_name": "Тимофей",
      "description": "Хочу купить рюкзак",
      "created_at": "2025-01-16T13:44:47.898688"
    }
  ],
  "total": 4,
  "page": 1,
  "size": 50,
  "pages": 1
}

```

 - `GET /app/v1/applications?user_name=%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9&page=1&size=50` - запрос 1 страницы по 50 объектов, с фильтрацией по имени.

Тело ответа с фильтром:
```html
{
  "items": [
    {
      "id": "1bbfeb94-cc31-41e7-9621-359aab5c12ab",
      "user_name": "Тимофей",
      "description": "Хочу купить рюкзак",
      "created_at": "2025-01-16T13:44:47.898688"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50,
  "pages": 1
}

```