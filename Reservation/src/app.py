from flask import Flask, render_template, request, session, flash


from src.common.database import Database
from src.models.customer import Customer
from src.models.menu import Menu
from src.models.reserve import Info


#Initializing the application
app = Flask(__name__)
app.secret_key ="fahim"



#Routing to the main page of the customer
@app.route('/')#
def home_method():
    return render_template('login.html')


#Getting the about page
@app.route('/about')
def about():
    return render_template("about.html")

#Getting the games page
@app.route('/games')
def game():
    return render_template("2_games.html")

#Before requesting from the database inttializing the database
@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/help', methods=['POST'])# www.mysite.com/API/
def help_customer():
    return render_template("help.html")

#Validating the login username and password
@app.route('/login', methods=['POST'])
def login_user():

    #Getting the email and password from the page
    email = request.form['email']
    password = request.form['password']

    #checking if the customer is registered
    if Customer.login_valid(email, password):
        Customer.login(email)#if registered ogin sucessfull
    else:

        return render_template("login.html")

    return render_template("profile.html", email=session['email'])#returning the home page when the login is sucessfull

#returning the menu page
@app.route('/menu')
def menu_item():

    return render_template('menu.html')


#going to the menu cart
@app.route('/menu/cart')
def checkout(): #method to access the input

    name = request.args.get('item1')

    menu = Database.find_one("Menu",{'Item':name})

    dam = menu['price']

    Menu.item_add(name, dam)



    return render_template('cart.html', name=name, price=dam)


#logging the guest
@app.route('/login/guest')
def guest():
    return render_template('guest.html')

#getting thr checkout page
@app.route('/checkout')
def check():
    return render_template('checkout.html')


#returning the register page
@app.route('/register', methods=['POST'])
def register_user():
    return render_template("register.html")



#authorizing the registration
@app.route('/auth/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    Customer.register(email, password)

    return render_template("login.html")

#opening the reservation page
@app.route('/reserve', methods=['POST'])# www.mysite.com/API/
def reserve():
    return render_template("reserve.html")

@app.route('/logout', methods=['POST'])
def logout():
    return render_template("login.html")



#checking for previous reservations at the same date and time
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
