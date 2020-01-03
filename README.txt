доп. библиотеки:
1. flask
2. flask-sqlalchemy (ORM)
3. flask-migrate (Для обновления таблиц при изменении)
4. psycopg2 !? (Подключение к postgresql)
5. flask-script
6. wtforms (Для работы с html формами)
7. flask-admin (Для установки админки)
8. flask-security (Для защиты админки)
9. flask-ckeditor (Для редактирования теста в постах)

Команды для миграции:
python manage.py db init (Создание файла с миграциями)
python manage.py db migrate (Обновление миграцией)
python manage.py db upgrade (Занесение обновлений в БД)

Для создания новой роли необходимо:
Создается через user_datasroteexit
Пример
import db
import user_datastore
user_datastore.create_role(name='admin', description='administration')
db.session.commit()
user_datastore.add_role_to_user(user, role) (Связывание, где user и rule объекты классов User и Role соотв.)
(Не забыть session())

