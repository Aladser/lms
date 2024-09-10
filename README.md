# LMS
Документация: http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/swagger/

## Настройки проекта
* Создать файл *.env* в корне проекта с настройками, аналогичными *.env.example*.
* ``python manage.py createusers`` - создать пользователей
* ``python manage.py seed`` - сидирование таблиц
* JWT - авториазция
* Запуск отложенных задач: ``celery -A config worker -l INFO``
* запуск периодических задач: ``celery -A config worker --beat --scheduler django --loglevel=info``

## Модели
+ ``authen_drf``: 
  * ``User``:``email``, ``phone``, ``avatar``, ``token``, ``country``
  * ``Country``
+ ``lms``: 
  + ``Course`` 
    * ``name``
    * ``description``
    * ``preview_image``
    * ``owner``
    * ``updated_at`` - дата последнего обновления
  + ``Lesson``: ``name``, ``description``, ``preview_image``, ``video_link``, ``course``, ``owner``
  + ``UserSubscription`` (подписки пользователей на обновления курсов): ``user``, ``course``
+ ``payment``:
  * ``Payment`` - Платеж.
    + ``user``
    + ``course``
    + ``lesson``
    + ``amount``
    + ``session_id`` - id stripe-сессии
    + ``link`` - ссылка на оплату

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

## Асихронные задачи
+ ``lms.send_course_updating_notification`` - Отправляет отложенно почтовые уведомления об обновлении курса
+ ``authen_drf.check_user_activities`` - Периодическая  проверка активности пользователей"
