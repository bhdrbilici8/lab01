from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
                     TextAreaField, SelectField)
from wtforms.validators import (DataRequired, Email, Length,
                                EqualTo, ValidationError)
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=80)])
    email    = StringField('Email',
                           validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6)])
    confirm  = PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('password',
                             message='Passwords must match.')])
    submit   = SubmitField('Create Account')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken. Please choose another.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered. Please log in.')


class LoginForm(FlaskForm):
    email    = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit   = SubmitField('Log In')


class BookForm(FlaskForm):
    title       = StringField('Title',
                              validators=[DataRequired(), Length(max=200)])
    author      = StringField('Author',
                              validators=[DataRequired(), Length(max=150)])
    description = TextAreaField('Description (optional)')
    submit      = SubmitField('Add Book')


class ReviewForm(FlaskForm):
    rating      = SelectField('Rating', coerce=int,
                              choices=[(1, '⭐ 1 – Poor'),
                                       (2, '⭐⭐ 2 – Fair'),
                                       (3, '⭐⭐⭐ 3 – Good'),
                                       (4, '⭐⭐⭐⭐ 4 – Very Good'),
                                       (5, '⭐⭐⭐⭐⭐ 5 – Excellent')],
                              validators=[DataRequired()])
    review_text = TextAreaField('Your Review',
                                validators=[DataRequired(), Length(min=10, max=2000)])
    submit      = SubmitField('Submit Review')
