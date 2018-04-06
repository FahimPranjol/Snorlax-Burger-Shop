from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.customer import Customer
from src.models.reserve import Info
from src.models.waitstaff import Waitstaff


app = Flask(__name__)
app.secret_key ="fahim"

#API end points

@app.route('/')# www.mysite.com/API/
def home_method(): #method to access the input
    return render_template('login.html')

@app.route('/login')
def login_template():
    return render_template('login.html')

@app.route('/stafflogin')
def login_waitstaff_template():
    return render_template('waitstaffLI.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if Customer.login_valid(email, password):
        Customer.login(email)
    else:
        session['email'] = None

    return render_template("hello.html", email=session['email'])

@app.route('/stafflogin', methods=['POST'])
def login_waitstaff():
    username = request.form['username']
    password = request.form['password']

    if Waitstaff.valid_login(username, password):
        Waitstaff.login(username)
    else:
        session['username'] = None

    return render_template("waitstaff_home.html", username=session['username'])

@app.route('/reserve', methods=['POST'])# www.mysite.com/API/
def reservation(): #method to access the input
    name = request.form['firstname']
    date = request.form['date']
    time = request.form['time']

    Info.new_reservation(name, date, time)

    return render_template('last.html', name=session['name'], date=session['date'], time=session['time'])

@app.route('/kstaff1')
def View():

    return render_template('kstaff1.html')


@app.route('/kstaff')
def Order():

    return render_template('kstaff.html')

#running the app(a requirement to run the app
if __name__ == '__main__':
    app.run(port=4990, debug=True)
