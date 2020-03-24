# users
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from xyz.models import Guy

class RegGuy(FlaskForm):
	fname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	lname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	num = StringField('Cell #', validators=[DataRequired()])
	pw = PasswordField('Password', validators=[DataRequired()])
	confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('pw')])
	submit = SubmitField('Insert')

	def validate_email(self, email):
		g = Guy.query.filter_by(email=email.data).first()
		if g:
			print(g)
			raise ValidationError('This email belongs to ' + g.fname + ' ' + g.lname + '.')

class AddGuyForm(FlaskForm):
	fname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	lname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	num = StringField('Cell #', validators=[DataRequired()])
	submit = SubmitField('Insert')

	#def validate_username(self, username):
	#	user = Guy.query.filter_by(username=username.data).first()
	#	if user:
	#		raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		g = Guy.query.filter_by(email=email.data).first()
		if g:
			print(g)
			raise ValidationError('This email belongs to ' + g.fname + ' ' + g.lname + '.')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	pw = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')