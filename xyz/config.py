import os

class Config:
	#SECRET_KEY = 'e1487f9bb26793dcdf3a8350295aa8c1'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_URI')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_U')
	MAIL_PASSWORD = os.environ.get('EMAIL_P')