from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired


class videoLinkForm(FlaskForm):
    link = StringField(label='Link')
    download = SubmitField(label='download')
