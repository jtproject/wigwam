from flask import render_template, request, Blueprint
from xyz.models import Calendar

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    days = Calendar.query.all()
    return render_template('home.html', days=days)

@main.route('/info')
def info():
    return render_template('info.html', title='Page Information')
