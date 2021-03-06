from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime


app = Flask(__name__)
manager =Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'IT IS A BUG'

class NameForm(Form):
    name = StringField("what is your name?", validators=[InputRequired()])
    submit =SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have change your name !')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(),
                           form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()





