# LMS

## Настройки проекта
+ cоздать файл *.env* в корне проекта с настройками, аналогичными *.env.example*
* ``python manage.py initusers`` - создать пользователей
* ``python manage.py initlms`` - сидирование таблиц

## Модели
+ ``authen_drf``: ``User``, ``Country``
+ ``lms``: ``Course``, ``Lesson``
+ ``payment``: 
  * ``PaymentMethod`` 
  * ``Payment`` - Платеж. Каждый платеж имеет обязательное поле курса и необязательное поле урока

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

## Представления
+ ``CourseViewSet``
+ ``LessonListAPIView``, ``LessonRetrieveAPIView``, ``LessonCreateAPIView``, ``LessonUpdateAPIView``, ``LessonDestroyAPIView``
+ ``UserListAPIView``, ``UserRetrieveAPIView``, ``UserUpdateAPIView``
+ ``PaymentListAPIView``
    * сортировка по дате платежа
    * фильтрация по курсу, уроку, типу платежа


