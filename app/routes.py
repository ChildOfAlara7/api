# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import AddingForm, ShowForm
from app.database import get_db, init_db

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', title='Welcome')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    bas = init_db()
    return render_template('success.html', var='Database has been successfully reset!')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddingForm()
    if request.method == 'POST' and form.validate_on_submit():
        login = format(form.login.data)
        password = format(form.password.data)
        name = format(form.name.data)
        mail = format(form.mail.data)
        base = get_db()
        res = base.execute("insert into users (login, password, name, mail) values (%s, %s, %s, %s)", (login, password, name, mail))
        return redirect(url_for('success', var = "User has been successfully added!"))
    return render_template('adding.html', title='Add', form=form)

@app.route('/success/<var>')
def success(var):
    return  render_template('success.html', title='success', var=var)

@app.route('/show', methods=['GET', 'POST'])
def show():
    form = ShowForm()
    if request.method == 'POST' and form.validate_on_submit():  
        id = format(form.id.data)
        #bas = init_db()
        base = get_db()
        res = base.execute("SELECT * FROM users WHERE id = %s",(id)).fetchone()

        return redirect(url_for('results', name=res[3], login=res[1], password=res[2],mail=res[4]))
    return render_template('show.html', title='Show', form=form)


@app.route('/results/<name>/<login>/<password>/<mail>', methods=['GET', 'POST'])
def results(name, login, password, mail):
    return render_template('results.html', title='Results', name=name, login=login, password=password, mail=mail)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = ShowForm()
    if request.method == 'POST' and form.validate_on_submit():  
        id = format(form.id.data)
        base = get_db()
        base.execute("DELETE FROM users WHERE id = %s", (id))
        return redirect(url_for("success", var=" User has been successfully deleted!"))
            
    return render_template('del.html', title='Delete', form=form)

@app.route('/showall', methods=['GET'])
def showall():
    base = get_db()
    all = base.execute("SELECT * FROM users")
    return render_template('showall.html', title='All users', all=all)
