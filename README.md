# LMS

## Настройки проекта
+ cоздать файл *.env* в корне проекта с настройками, аналогичными *.env.example*
* ``python manage.py createusers`` - создать пользователей
* ``python manage.py seed`` - сидирование таблиц
* JWT - авториазция

## Модели
+ ``authen_drf``: ``User``, ``Country``
+ ``lms``: ``Course``, ``Lesson``
+ ``payment``: 
  * ``PaymentMethod`` 
  * ``Payment`` - Платеж. Каждый платеж имеет обязательное поле курса и необязательное поле урока

## Контроллеры
+ ``CourseViewSet``
+ ``LessonListAPIView``, ``LessonRetrieveAPIView``, ``LessonCreateAPIView``, ``LessonUpdateAPIView``, ``LessonDestroyAPIView``
+ ``UserListAPIView``, ``UserRetrieveAPIView``, ``UserUpdateAPIView``
+ ``PaymentListAPIView``
    * сортировка по дате платежа
    * фильтрация по курсу, уроку, типу платежа

## Сериализаторы
+ ``authen_drf``: 
    * ``UserSerializer``
        + ``payments`` - поле платежей пользователя
+ ``lms``: 
  * ``CourseSerializer``
    + ``lesson`` - уроки курса
    + ``lessons_count`` - число уроков курса
  * ``LessonSerializer``
+ ``payment``: ``PaymentSerializer``

## Права пользователей
+ ``IsModeratorPermission`` - проверка на модератора
+ ``IsOwnerPermission`` - проверка на создателя объекта
+ ``IsPersonalProfilePermission`` - проверка права редактирования своего пользовательского профиля

## Группы пользователей
+ ``moderators`` - могут просматривать все курсы и уроки, не могут  создавать, обновлять, удалять их
+ ``users`` - могут создать, редактировать и удалять свои курсы и уроки

Пользователи могут видеть полную информацию только о своем профиле
