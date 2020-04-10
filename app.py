from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students2.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    rollno = db.Column(db.String(10))
    gender = db.Column(db.String(100))
    course = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(6))
    


def __init__(self, name,rollno, gender,course,city, addr,pin):
    self.name = name
    self.rollno = rollno
    self.gender = gender
    self.course = course
    self.city = city
    self.addr = addr
    self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(name=request.form['name'],rollno=request.form['rollno'],gender=request.form['gender'],course=request.form['course'], city=request.form['city'],addr=request.form['addr'], pin=request.form['pin'])
        
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
