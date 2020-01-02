from wtforms import Form, TextAreaField, StringField


class PostForm(Form):
    title = StringField('title')
    body = TextAreaField('text')