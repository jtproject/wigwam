from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError

#
#
#
# build calendar form
class BuildCalendarForm(FlaskForm):
    weekday = StringField('Week Day', validators=[DataRequired()])
    day = StringField('Day', validators=[DataRequired()])
    month = StringField('Month', validators=[DataRequired()])
    year = StringField('Year',validators=[DataRequired()])
    submit = SubmitField('Submit')