from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.reserve import Info


app = Flask(__name__)#'__main__'
app.secret_key ="fahim"

#API end points

@app.route('/')# www.mysite.com/API/
def home_method(): #method to access the input
    return render_template('waiter_id.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/reserve', methods=['POST'])# www.mysite.com/API/
def reservation(): #method to access the input
    table = request.form['table_no']
    waitstaff = request.form['waitstaff']

    Info.new_reservation(name, date, time)

    return render_template('last.html', table=session['table_no'], date=session['waitstaff'])


#running the app(a requirement to run the app
if __name__ == '__main__':
    app.run(port=4994, debug=True)