from flask import render_template, request, Blueprint
from xyz.models import Calendar

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    print('home page')
    return render_template('home.html')

@main.route('/info')
def info():
    return render_template('info.html', title='Page Information')
