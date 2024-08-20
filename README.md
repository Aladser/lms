# LMS

## Настройки проекта
+ cоздать файл *.env* в корне проекта с настройками, аналогичными *.env.example*
* ``python manage.py createadmin`` - создание суперпользователя

## Модели
+ ``authen_drf``: ``User``, ``Country``
+ ``lms``: ``Course``, ``Lesson``

## Сериализаторы
+ ``authen_drf``: ``UserSerializer``
+ ``lms``: ``CourseSerializer``, ``LessonSerializer``

## Представления
+ ``CourseViewSet``
+ ``LessonListAPIView``, ``LessonRetrieveAPIView``, ``LessonCreateAPIView``, ``LessonUpdateAPIView``, ``LessonDestroyAPIView``
+ ``UserListAPIView``, ``UserRetrieveAPIView``, ``UserUpdateAPIView``


