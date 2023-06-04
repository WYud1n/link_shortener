from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Home(FlaskForm):
    link = StringField('Введите полную ссылку', validators=[DataRequired()])
    submit = SubmitField('Получить короткую')

