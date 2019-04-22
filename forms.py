from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
    BooleanField, SubmitField, IntegerField, SelectField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email
import os


class LoginForm(FlaskForm):
    """Форма авторизации"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение', validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddCarForm(FlaskForm):
    name = StringField('Название')#, validators=[DataRequired()])
    price = IntegerField('Цена')#, validators=[DataRequired()])
    adress = StringField('Адрес')#, validators=[DataRequired()])
    country = SelectField('Страна', coerce=int)  # , validators=[DataRequired()])
    description = TextAreaField('Описание')#, validators=[DataRequired()])
    image = FileField('Фото отеля')

    submit = SubmitField('Создать')

    def __init__(self):
        super(AddCarForm, self).__init__()

    def save_im(self):
        im = self.image.data
        print(im, "!!!!")
        im_name = os.path.join('static', 'img', im.filename)
        im.save(im_name)


class AddDealerForm(FlaskForm):
    """Добавление дилерского центра"""
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Добавить дилерский центр')


class SearchPriceForm(FlaskForm):
    """Форма поиска по цене"""
    start_price = IntegerField('Минимальная цена', validators=[DataRequired()], default=500000)
    end_price = IntegerField('Максимальная цена', validators=[DataRequired()], default=1000000)
    submit = SubmitField('Поиск')


class SearchDealerForm(FlaskForm):
    """Форма поиска по дилерскому центру"""
    dealer_id = SelectField('Номер дилерского центра', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Поиск')
