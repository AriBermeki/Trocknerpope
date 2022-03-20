from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import psycopg2
from yaml_data_cfg import sequenz




app = Flask(__name__)
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SECRET_KEY'] = SECRET_KEY
#app.config['SQLALCHEMY_DATABASE_URI'] = sequenz

db = SQLAlchemy(app)




class User(db.Model):
    __tablename__= 'SYSTEM'
    id=db.Column( db.Integer, primary_key = True)
    vorname = db.Column( db.String())
    nachname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    create_data = db.Column(db.DateTime, default=datetime.utcnow)



    def __init__(self, vorname, nachname, email, password):
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.password = password



class Regester(FlaskForm):
    vorname = StringField('Vorname', validators=[InputRequired(), Length(max=10)])
    nachname = StringField('Nachname', validators=[InputRequired(), Length(max=10)])
    email = StringField('Email', validators=[InputRequired(), Length(max=200)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=200)])





class Login(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=200)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=200)])
    submit = SubmitField('Regester')

    




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard', methods=['POST', 'GET'])
def office():
    return render_template('office.html')




@app.route('/log', methods=['POST', 'GET'])
def user():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        if user:
            if password:
                return redirect(url_for('office'))
        else:
            return '<h1> The user is not exested<h1>'

    return render_template('log.html', form=form)





@app.route('/regester', methods=['POST', 'GET'])
def regist():
    form = Regester()
    if form.validate_on_submit():
        user = User(
            vorname = form.vorname.data,
            nachname = form.nachname.data,
            email= form.email.data,
            password = form.password.data
            )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('user'))

    return render_template('regester.html', form=form)

