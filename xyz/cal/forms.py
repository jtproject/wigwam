from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from xyz.models import Calendar

#
#
#
# build calendar form
class BuildCalendarForm(FlaskForm):
    pass