from flask import render_template, request, Blueprint
from xyz.models import Calendar
from xyz import _D

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    days = Calendar.query.all()

    return render_template('home.html', days=days)

@main.route('/info')
def info():
    wd = ['SUN', 'MON', 'TUES', 'WED', 'THURS', 'FRI', 'SAT']
    xx = Calendar.query.order_by(Calendar.id.desc()).first()
    for x in wd:
        print(xx.weekday)
        print(x)
        if xx.weekday == x:
            if x == 'SAT':
                cnt = 0
            else:
                cnt = wd.index(x) + 1
            break
    day = 1
    mon = 'June'
    yr = '2020'
    while day < 31:
        wkday = wd[cnt]
        add = Calendar(weekday=wkday, day=day, month=mon, year=yr)
        #_D.session.add(add)
        print(add)
        if cnt == 6:
            cnt = 0
        else:
            cnt += 1
        day += 1

    #_D.session.delete(x)
    #_D.session.commit()
    return render_template('info.html', title='Page Information')