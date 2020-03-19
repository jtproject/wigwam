from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from xyz import _D, _E
from xyz.models import Calendar

cal = Blueprint('cal', __name__)

@cal.route('/calendar')
def calendar():
    return render_template('calendar.html', title='View Calendar')

@cal.route('/data/calendar')
def add_data():
    return render_template('data/create_calendar.html', title='Add Calendar Data')

