from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, url, ValidationError
from shortner.models import Shortner


class ShortForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), url()])
    convert = SubmitField('Convert')
