# LMS
Документация: http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/swagger/

+ LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы.
+ SPA веб-приложение - бэкенд-сервер, который возвращает клиенту JSON-структуры. 
+ JWT-авторизация.
+ Тесты 
+ Работае приложения проверялась через Postman

## Настройки проекта
* Создать файл *.env* в корне проекта с настройками, аналогичными *.env.example*.
* ``python manage.py createusers`` - создать пользователей
* ``python manage.py seed`` - сидирование таблиц
* JWT - авторизация
* Запуск отложенных задач: ``celery -A config worker -l INFO``
* запуск периодических задач: ``celery -A config worker --beat --scheduler django --loglevel=info``

```
docker network create lmsnet
docker-compose up --build
```

## Права пользователей:
+ ``IsModeratorPermission`` - проверка модератора: могут работать с любыми курсами и уроками, но не могут создавать и удалять
+ ``IsOwnerPermission`` - проверка создателя объекта: могут работать только со своими курсами и уроками
+ ``IsPersonalProfilePermission`` - проверка права редактирования своего пользовательского профиля

## Модели
+ ``authen_drf``: 
  * ``User``: почта, телефон, аватар, страна
  * ``Country``
+ ``lms``: 
  + ``Course``: название, описание, превью-изображение, владелец, дата последнего обновления
  + ``Lesson``: название, описание, превью-изображение, видеоссылка, курс, владелец
  + ``UserSubscription`` (подписки пользователей на обновления курсов): пользователь, курс
+ ``payment``:
  * ``Payment``: пользователь, курс, урок, сумма, id stripe-сессии, ссылка на оплату

## Контроллеры
+ lms
  + ``CourseViewSet`` - вьюсет: 
    * ``list`` - список всех курсов. Пагинация 
    * ``create`` - создание курса. Отправка почтовых уведомлений об изменении курса
  + ``LessonListAPIView`` - генерик списка уроков. Пагинация
  + ``LessonRetrieveAPIView`` - генерик одного курса 
  + ``LessonCreateAPIView`` - генерик создания курса
  + ``LessonUpdateAPIView`` - генерик обновления курса
  + ``LessonDestroyAPIView`` - генерик удаления курса
+ payment
  + ``PaymentListAPIView`` - генерик списка всех платежей. Пагинация, сортировка по дате оплаты, фильтрация по курсу, уроку, способу оплаты
  + ``PaymentCreateAPIView`` - генерик создания оплаты курса
  + ``show_success_payment`` - страница уведомления об успешной оплате
  + ``PaymentStatusAPIView`` - генерик информации о статусе платежа
+ authen_drf
  + ``UserListAPIView`` - генерик списка пользователей
  + ``UserRetrieveAPIView`` - генерик одного пользователя
  + ``UserUpdateAPIView`` - генерик обновления пользователя
  + ``LoginView``- генерик авторизации. Обновление даты последней авторизации

## Сериализаторы
+ ``authen_drf``: 
    * ``UserSerializer``
    * ``UserDetailSerializer``
      + ``payment (PaymentSerializer)`` - платежи пользователя
+ ``lms``: 
  * ``CourseSerializer``
    + ``lesson (LessonSerializer)``: информация по всем урокам.
    + ``get_lessons_count()`` - количество уроков
    + ``get_is_user_subscription()`` - проверка подписи на курс авторизованного пользователя
  * ``LessonSerializer``
    + валидатор проверки наличия видеоссылок
+ ``payment``: 
  * ``PaymentSerializer``

## Асихронные задачи
+ ``lms.send_course_updating_notification`` - Отправляет отложенно почтовые уведомления об обновлении курса c помощью celery
+ ``authen_drf.check_user_activities`` - celery-beat периодическая проверка активности пользователей. Если пользователей не заходил больше 7 дней, аккаунт деактивируется.
