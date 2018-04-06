from flask import Flask, render_template, request, session, flash

from src.common.database import Database
from src.models.customer import Customer
from src.models.menu import Menu
from src.models.reserve import Info


app = Flask(__name__)
app.secret_key ="fahim"

#API end points

@app.route('/')# www.mysite.com/API/
def home_method(): #method to access the input
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template("about.html")

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

        return render_template("login.html")

    return render_template("profile.html", email=session['email'])

@app.route('/menu')
def menu_item():

    return render_template('menu.html')


@app.route('/menu/cart', methods=['GET'])# www.mysite.com/API/
def checkout(): #method to access the input

    name = request.args.get('item1')
    if Menu.item_valid(name):
        return render_template('cart.html', name=name)
    else:
        return render_template('menu.html')

@app.route('/login/guest')
def guest():
    return render_template('guest.html')



@app.route('/register', methods=['POST'])
def register_user():
    return render_template("register.html")




@app.route('/auth/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    Customer.register(email, password)

    return render_template("login.html")


@app.route('/reserve', methods=['POST'])# www.mysite.com/API/
def reserve():
    return render_template("reserve.html")

@app.route('/logout', methods=['POST'])# www.mysite.com/API/
def logout():
    return render_template("login.html")




@app.route('/auth/reserve', methods=['POST'])# www.mysite.com/API/
def reservation(): #method to access the input
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']

    if Info.new_reservation(name, date, time):
        return render_template('last.html', name=session['name'], date=session['date'], time=session['time'])

    else:
        return render_template('reserve.html')

#running the app(a requirement to run the app
if __name__ == '__main__':
    app.run(port=4990, debug=True)
