from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask import request, redirect, url_for
from flask_admin import AdminIndexView


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminMixin:
    # Является ли пользователь админом
    def is_accessible(self):
        return current_user.has_role('admin')

    # Если не является, то определяется view
    # next определяет куда пользователь направлялся
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


# Ограничивает доступ к админке
class AdminView(AdminMixin, ModelView):
    pass


# Ограничивает таблицу admin полностью
class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminView, BaseModelView):
    form_columns = ['title', 'body', 'tags']


class TagAdminView(AdminView, BaseModelView):
    form_columns = ['name', 'posts']