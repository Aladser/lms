# LMS

## Настройки проекта
+ cоздать файл *.env* в корне проекта с настройками, аналогичными *.env.example*
* ``python manage.py createusers`` - создать пользователей
* ``python manage.py seed`` - сидирование таблиц
* JWT - авториазция

## Модели
+ ``authen_drf``: ``User``, ``Country``
+ ``lms``: 
  + ``Course``, 
  + ``Lesson``, 
  + ``UserSubscription`` - подписки пользователей на обновления курсов
+ ``payment``: 
  * ``PaymentMethod`` 
  * ``Payment`` - Платеж. Каждый платеж имеет обязательное поле курса и необязательное поле урока

## Контроллеры
+ ``CourseViewSet``: ``list`` - пагинация
+ ``LessonListAPIView`` - пагинация
+ ``LessonRetrieveAPIView``, ``LessonCreateAPIView``, ``LessonUpdateAPIView``, ``LessonDestroyAPIView``
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
    + ``is_user_subscription`` - наличие подписки пользователя на обновления курса
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

## Валидаторы
+ ``lms.validators.LinkValidator`` - проверка наличия ссылок на внешний ресурс кроме ютуба

## Тесты
+ ``LessonTestCase`` - CRUD уроков
+ ``CourseTestCase`` - подписка на курсы
coverage.txt - покрытие тестами