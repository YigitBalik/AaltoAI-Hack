from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Optional
from wtforms import validators,  TextAreaField
from flask_wtf.file import FileField


class RFP(FlaskForm):

    file = FileField(validators=[DataRequired()])