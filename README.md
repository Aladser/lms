# LMS
Документация: http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/swagger/

## Настройки проекта
* Создать файл *.env* в корне проекта с настройками, аналогичными *.env.example*.
* ``python manage.py createusers`` - создать пользователей
* ``python manage.py seed`` - сидирование таблиц
* JWT - авториазция
* Запуск отложенных задач: ``celery -A config worker -l INFO``

## Модели
+ ``authen_drf``: ``User``, ``Country``
+ ``lms``: 
  + ``Course``, 
  + ``Lesson``, 
  + ``UserSubscription`` - подписки пользователей на обновления курсов
+ ``payment``:
  * ``Payment`` - Платеж.
    + user - пользователь
    + course - курс
    + lesson - урок
    + amount - стоимость
    + session_id - id stripe-сессии
    + link - ссылка на оплату

## Контроллеры
+ lms
  + ``CourseViewSet``: ``list`` - пагинация
  + ``LessonListAPIView`` - пагинация
  + ``LessonRetrieveAPIView``, ``LessonCreateAPIView``, ``LessonUpdateAPIView``, ``LessonDestroyAPIView``
+ payment
  + ``PaymentListAPIView`` - список всех платежей
  + ``PaymentCreateAPIView`` - создание оплаты курса
  + ``show_success_payment`` - страница уведомления об успешной оплате
  + ``PaymentStatusAPIView`` - информация о статусе платежа
+ authen_drf
  + ``UserListAPIView``, ``UserRetrieveAPIView``, ``UserUpdateAPIView``

## Сериализаторы
+ ``authen_drf``: 
    * ``UserSerializer``
    * ``UserDetailSerializer``
+ ``lms``: 
  * ``CourseSerializer``
  * ``LessonSerializer``
+ ``payment``: 
  * ``PaymentSerializer``

## Права пользователей
+ ``IsModeratorPermission`` - проверка на модератора
+ ``IsOwnerPermission`` - проверка на создателя объекта
+ ``IsPersonalProfilePermission`` - проверка права редактирования своего пользовательского профиля
