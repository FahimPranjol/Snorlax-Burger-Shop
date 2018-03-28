from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.reserve import Info
from src.models.user import User

app = Flask(__name__)
app.secret_key ="fahim"

#API end points

@app.route('/')# www.mysite.com/API/
def home_method(): #method to access the input
    return render_template('Home_1.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/reserve', methods=['POST'])# www.mysite.com/API/
def reservation(): #method to access the input
    name = request.form['firstname']
    date = request.form['date']
    time = request.form['time']

    Info.new_reservation(name, date, time)

    return render_template('last.html', name=session['name'], date=session['date'], time=session['time'])


#running the app(a requirement to run the app
if __name__ == '__main__':
    app.run(port=4996, debug=True)
