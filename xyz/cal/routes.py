from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from xyz import _D, _E
from xyz.models import Calendar
from xyz.cal.forms import BuildCalendarForm

cal = Blueprint('cal', __name__)

@cal.route('/calendar')
def calendar():
    wd = ['SUN', 'MON', 'TUES', 'WED', 'THURS', 'FRI', 'SAT']
    mn = [
        'Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec'
    ]
    xx = Calendar.query.filter_by(month='Apr')
    #for x in xx:
    #    x.day = int(x.day)
    return render_template('calendar.html', title='View Calendar', dates=xx, wd=wd)

@cal.route('/data/calendar', methods=['GET', 'POST'])
def add_data():
    form = BuildCalendarForm()
    if form.validate_on_submit():
        date = Calendar(weekday=form.weekday.data, day=form.day.data, month=form.month.data, year=form.year.data)
        #_D.session.add(date)
        print(date)
        #_D.session.commit()
        #flash(f'')
        return redirect(url_for('cal.add_data'))
    return render_template('data/create_calendar.html', title='Add Calendar Data', form=form)

