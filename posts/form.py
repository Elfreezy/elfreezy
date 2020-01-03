from wtforms import Form, StringField
from flask_ckeditor import CKEditorField


class PostForm(Form):
    title = StringField('title')
    body = CKEditorField('text')