from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required, login_user, logout_user
from xyz import _D, _E
from xyz.models import Guy
from xyz.guy.forms import AddGuyForm, LoginForm, RegGuy

guy = Blueprint('guy', __name__)

@guy.route('/view/guy/all', methods=['GET'])
#@login_required
def guys():
    g = Guy.query.all()
    return render_template('guys.html', title='Employee List', guy=g)

@guy.route('/add/guy', methods=['GET', 'POST'])
#@login_required
def add_data():
    form = AddGuyForm()
    if form.validate_on_submit():
        hsh = _E.generate_password_hash('password').decode('utf-8')
        g = Guy(fname=form.fname.data, lname=form.lname.data, email=form.email.data, num=form.num.data, pw=hsh)
        print(g)
        #_D.session.add(g)
        #_D.session.commit()
        return redirect(url_for('main.home'))
    return render_template('data/create_guy.html', title='Add Employee Data', form=form)

@guy.route('/register', methods=['GET', 'POST'])
def register():
    form = RegGuy()
    if form.validate_on_submit():
        hsh = _E.generate_password_hash(form.pw.data).decode('utf-8')
        g = Guy(fname=form.fname.data, lname=form.lname.data, email=form.email.data, num=form.num.data, pw=hsh)
        #_D.session.add(g)
        print(g, g.pw)
        #_D.session.commit()
        #flash(f'')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)

@guy.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        g = Guy.query.filter_by(email=form.email.data).first()
        if g and _E.check_password_hash(g.pw, form.pw.data):
            login_user(g, remember=form.remember.data)
            return redirect(url_for('cal.calendar'))
        else:
            flash('You don\'t belong here.', 'danger')
    return render_template('login.html', title='Login', form=form)

@guy.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))