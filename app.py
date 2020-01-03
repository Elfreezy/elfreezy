from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# import psycopg2

from flask_admin import Admin

from flask_security import Security
from flask_security import SQLAlchemyUserDatastore

from flask_ckeditor import CKEditor

from config import Configuration


app = Flask(__name__)

# Импорот всех конфигураций из класса Configuration
app.config.from_object(Configuration)

# Регистрация БД
db = SQLAlchemy(app)

# Разобраться с manager???
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Поключение CKEditor
ckeditor = CKEditor(app)


# ADMIN
from models import Post, Tag, User, Role
from admin import PostAdminView, TagAdminView, HomeAdminView

admin = Admin(app, 'Flask App', url='/', index_view=HomeAdminView('Admin'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

# FLASK-SECURITY
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

