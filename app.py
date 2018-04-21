from flask import Flask, render_template, request, session, flash


from src.common.database import Database
from src.models.Tables import Tables
from src.models.customer import Customer
from src.models.menu import Menu
from src.models.reserve import Info
from src.models.waitstaff import Waitstaff


#Initializing the application
from src.models.table_orders import Table_order

app = Flask(__name__)
app.secret_key ="fahim"



#Routing to the main page of the customer
@app.route('/')#
def home_method():
    return render_template('customerPage_afterLogin.html')






#Before requesting from the database inttializing the database
@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/customer_login', methods=['GET'])#
def customer_login():

    table_no = request.args.get('table_no')
    table_name = request.args.get('table_name')

    table = Tables(table_no= table_no,
                   table_name=table_name,
                   user_email="none",
                   coupon="No coupons")

    table.save_to_mongo()


    return render_template('login.html', table_no = table_no)

#Getting the about page
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/addtips')
def addtips():
    return render_template("addtips.html")


@app.route('/taketips')
def taketips():
    return render_template("taketips.html")

#Getting the games page
@app.route('/games')
def game():
    return render_template("2_games.html")


@app.route('/help', methods=['POST'])# www.mysite.com/API/
def help_customer():
    return render_template("help.html")



#Validating the login username and password
@app.route('/login', methods=['POST' ,'GET'])
def login_user():

    #Getting the email and password from the page
    email = request.form['email']
    password = request.form['password']


    #checking if the customer is registered
    if Customer.login_valid(email, password):
        Customer.login(email)  #if registered login sucessfull
    else:

        return render_template("login.html")

    Database.update_one("tables",{'user_email':"none"}, {"$set":{'user_email':email}})

    date=Database.find('tables')

    for day in date:
        time=day['created_date']
        table_no=day['table_no']
        table_name=day['table_name']



        time = time.weekday()



        if (time==3):
         today="Thursday"
        elif (time==4):
            today="Friday"


    return render_template("profile.html", email=session['email'],table_no=table_no, time=today, table_name=table_name)#returning the home page when the login is sucessfull



@app.route('/profile')
def profile():
    return render_template('profile.html')



#returning the menu page
@app.route('/menu')
def menu_item():

    return render_template('menu.html')




#going to the menu cart
@app.route('/menu/cart')
def checkout(): #method to access the input

    name = request.args.get('item1')
    tips = request.args.get('tips')

    menu = Database.find_one("Menu",{'Item':name})

    dam = menu['price']

    Menu.item_add(name, dam)

    table = Database.find("tables")

    for numbers in table:
        tableNo = numbers['table_no']
        tableName = numbers['table_name']
        userEmail = numbers['user_email']



    table_order = Table_order(table_no=tableNo,
                              table_name=tableName,
                              user_email = userEmail,
                              order_status = "no order",
                              item=name,
                              price=dam

                              )

    if(tableNo == "Table 1"):
     table_order.save_to_table1()

    elif(tableNo == "Table 2"):
     table_order.save_to_table2()

    elif(tableNo == "Table 3"):
     table_order.save_to_table3()

    elif(tableNo == "Table 4"):
     table_order.save_to_table4()

    elif(tableNo == "Table 5"):
     table_order.save_to_table5()

    elif(tableNo == "Table 6"):
     table_order.save_to_table6()

    elif(tableNo == "Table 7"):
     table_order.save_to_table7()

    elif(tableNo == "Table 8"):
     table_order.save_to_table8()

    elif(tableNo == "Table 9"):
     table_order.save_to_table9()

    elif(tableNo == "Table 10"):
     table_order.save_to_table10()

    elif(tableNo == "Table 11"):
     table_order.save_to_table11()

    elif(tableNo == "Table 12"):
     table_order.save_to_table12()

    elif(tableNo == "Table 13"):
     table_order.save_to_table13()

    elif(tableNo == "Table 14"):
     table_order.save_to_table14()

    elif(tableNo == "Table 15"):
     table_order.save_to_table15()

    elif(tableNo == "Table 16"):
     table_order.save_to_table16()

    table_order.save_to_waitstaff_page()


    if(tableNo == "Table 1"):
     i = Database.find("table1_orders")

    elif(tableNo == "Table 2"):
     i = Database.find("table2_orders")

    elif(tableNo == "Table 3"):
     i = Database.find("table3_orders")

    elif(tableNo == "Table 4"):
     i = Database.find("table4_orders")

    elif(tableNo == "Table 5"):
     i = Database.find("table5_orders")

    elif(tableNo == "Table 6"):
     i = Database.find("table6_orders")

    elif(tableNo == "Table 7"):
     i = Database.find("table7_orders")

    elif(tableNo == "Table 8"):
     i = Database.find("table8_orders")

    elif(tableNo == "Table 9"):
     i = Database.find("table9_orders")

    elif(tableNo == "Table 10"):
     i = Database.find("table10_orders")

    elif(tableNo == "Table 11"):
     i = Database.find("table11_orders")

    elif(tableNo == "Table 12"):
     i = Database.find("table12_orders")

    elif(tableNo == "Table 13"):
     i = Database.find("table13_orders")

    elif(tableNo == "Table 14"):
     i = Database.find("table14_orders")

    elif(tableNo == "Table 15"):
     i = Database.find("table15_orders")

    elif(tableNo == "Table 16"):
     i = Database.find("table16_orders")





    count = 0
    price = 0
    for item in i:
        price = float(item['price']) + price



    if(tableNo == "Table 1"):
        items = Database.find("table1_orders")

    elif(tableNo == "Table 2"):
        items = Database.find("table2_orders")

    elif(tableNo == "Table 3"):
        items = Database.find("table3_orders")

    elif(tableNo == "Table 4"):
        items = Database.find("table4_orders")

    elif(tableNo == "Table 5"):
        items = Database.find("table5_orders")

    elif(tableNo == "Table 6"):
        items = Database.find("table6_orders")

    elif(tableNo == "Table 7"):
        items = Database.find("table7_orders")

    elif(tableNo == "Table 8"):
        items = Database.find("table8_orders")

    elif(tableNo == "Table 9"):
        items = Database.find("table9_orders")

    elif(tableNo == "Table 10"):
        items = Database.find("table10_orders")

    elif(tableNo == "Table 11"):
        items = Database.find("table11_orders")

    elif(tableNo == "Table 12"):
        items = Database.find("table12_orders")

    elif(tableNo == "Table 13"):
        items = Database.find("table13_orders")

    elif(tableNo == "Table 14"):
        items = Database.find("table14_orders")

    elif(tableNo == "Table 15"):
        items = Database.find("table15_orders")

    elif(tableNo == "Table 16"):
        items = Database.find("table16_orders")



    return render_template('cart.html', name=name, price=dam, total=price, item=items)



#logging the guest
@app.route('/login/guest')
def guest():

    return render_template('guest.html')


@app.route('/coupon')
def coupon():

    return render_template('coupon.html')


@app.route('/kstaff')
def kitchen_staff():

    return render_template('kitchen_staff_home.html')

# the waitstaff login page
@app.route('/waitstaff')
def wait_staff():

    return render_template("waitstaffLI.html")



@app.route('/receipt')
def receipt():

    return render_template('receipt.html')


@app.route('/waitstaff/tables1', methods=['POST'])
def waitstaff_tables1():
    username = request.form['username']
    password = request.form['password']
    if Waitstaff.valid_login(username, password):
        Waitstaff.login(username)
        staff = Waitstaff.get_by_username(username)
        login = Database.find_one("login", {"username": staff.username})
        if login is None:
            staff.record_login()  # record that staff has logged in for the day
    else:
        return render_template('waitstaffLI.html')

    if (staff.username == "erwin"):
        return render_template('waitstaff_tables1-4.html')
    elif (staff.username == "logan"):
        return render_template('waitstaff_tables5-8.html')
    elif (staff.username == "fahim"):
        return render_template('waitstaff_tables9-12.html')
    elif (staff.username == "rad"):
        return render_template('waitstaff_tables13-16.html')

@app.route('/waitstaff/tables2')
def waitstaff_tables2():
    return render_template('waitstaff_tables5-8.html')


@app.route('/waitstaff/tables3')
def waitstaff_tables3():
    return render_template('waitstaff_tables9-12.html')

@app.route('/waitstaff/tables4')
def waitstaff_tables4():
    return render_template('waitstaff_tables13-16.html')


@app.route('/waitstaff/orders/table1')
def waitstaff_orders_table1():

    table_no=request.args.get('table1')


    items1 = Database.find("table1_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table1_orders")



    return render_template('waitstaff_orders_table1.html', items=items, table_no=table_no, order_status= order_status)




@app.route('/waitstaff/orders/table2')
def waitstaff_orders_table2():
    table_no = request.args.get('table2')

    items1 = Database.find("table2_orders")

    for item1 in items1:
        table_no = item1['table_no']
        order_status = item1['order_status']
        table_name = item1['table_name']
        user_email = item1['user_email']

        items = Database.find("table2_orders")

    return render_template('waitstaff_orders_table2.html', items=items, table_no=table_no, order_status=order_status)

@app.route('/waitstaff/orders/table3')
def waitstaff_orders_table3():

    table_no=request.args.get('table3')


    items1 = Database.find("table3_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table3_orders")



    return render_template('waitstaff_orders_table3.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table4')
def waitstaff_orders_table4():

    table_no=request.args.get('table4')


    items1 = Database.find("table4_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table4_orders")



    return render_template('waitstaff_orders_table4.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table5')
def waitstaff_orders_table5():

    table_no=request.args.get('table5')


    items1 = Database.find("table5_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table5_orders")



    return render_template('waitstaff_orders_table5.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table6')
def waitstaff_orders_table6():

    table_no=request.args.get('table6')


    items1 = Database.find("table6_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table6_orders")



    return render_template('waitstaff_orders_table6.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table7')
def waitstaff_orders_table7():

    table_no=request.args.get('table7')


    items1 = Database.find("table7_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table7_orders")



    return render_template('waitstaff_orders_table7.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table8')
def waitstaff_orders_table8():

    table_no=request.args.get('table8')


    items1 = Database.find("table8_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table8_orders")



    return render_template('waitstaff_orders_table8.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table9')
def waitstaff_orders_table9():

    table_no=request.args.get('table9')


    items1 = Database.find("table9_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table9_orders")



    return render_template('waitstaff_orders_table9.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table10')
def waitstaff_orders_table10():

    table_no=request.args.get('table10')


    items1 = Database.find("table10_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table10_orders")



    return render_template('waitstaff_orders_table10.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table11')
def waitstaff_orders_table11():

    table_no=request.args.get('table11')


    items1 = Database.find("table11_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table11_orders")



    return render_template('waitstaff_orders_table11.html', items=items, table_no=table_no, order_status= order_status)


@app.route('/waitstaff/orders/table12')
def waitstaff_orders_table12():

    table_no=request.args.get('table12')


    items1 = Database.find("table12_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table12_orders")



    return render_template('waitstaff_orders_table12.html', items=items, table_no=table_no, order_status= order_status)

@app.route('/waitstaff/orders/table13')
def waitstaff_orders_table13():

    table_no=request.args.get('table13')


    items1 = Database.find("table13_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table13_orders")



    return render_template('waitstaff_orders_table13.html', items=items, table_no=table_no, order_status= order_status)


@app.route('/waitstaff/orders/table14')
def waitstaff_orders_table14():

    table_no=request.args.get('table14')


    items1 = Database.find("table14_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table14_orders")



    return render_template('waitstaff_orders_table14.html', items=items, table_no=table_no, order_status= order_status)


@app.route('/waitstaff/orders/table15')
def waitstaff_orders_table15():

    table_no=request.args.get('table15')


    items1 = Database.find("table15_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table15_orders")



    return render_template('waitstaff_orders_table15.html', items=items, table_no=table_no, order_status= order_status)


@app.route('/waitstaff/orders/table16')
def waitstaff_orders_table16():

    table_no=request.args.get('table16')


    items1 = Database.find("table16_orders")

    for item1 in items1:
         table_no = item1['table_no']
         order_status=item1['order_status']
         table_name=item1['table_name']
         user_email=item1['user_email']


         items = Database.find("table16_orders")



    return render_template('waitstaff_orders_table16.html', items=items, table_no=table_no, order_status= order_status)


@app.route('/kstaff/orders')
def kitchen_staff_orders():

    items = Database.find("kstaff_orders")

    return render_template('kstaff_orders.html', items = items)


#getting thr checkout page
@app.route('/checkout')
def check():

    table = Database.find("tables")

    for numbers in table:
        tableNo = numbers['table_no']


    if(tableNo == "Table 1"):
     i = Database.find("table1_orders")

    elif(tableNo == "Table 2"):
     i = Database.find("table2_orders")

    elif(tableNo == "Table 3"):
     i = Database.find("table3_orders")

    elif(tableNo == "Table 4"):
     i = Database.find("table4_orders")

    elif(tableNo == "Table 5"):
     i = Database.find("table5_orders")

    elif(tableNo == "Table 6"):
     i = Database.find("table6_orders")

    elif(tableNo == "Table 7"):
     i = Database.find("table7_orders")

    elif(tableNo == "Table 8"):
     i = Database.find("table8_orders")

    elif(tableNo == "Table 9"):
     i = Database.find("table9_orders")

    elif(tableNo == "Table 10"):
     i = Database.find("table10_orders")

    elif(tableNo == "Table 11"):
     i = Database.find("table11_orders")

    elif(tableNo == "Table 12"):
     i = Database.find("table12_orders")

    elif(tableNo == "Table 13"):
     i = Database.find("table13_orders")

    elif(tableNo == "Table 14"):
     i = Database.find("table14_orders")

    elif(tableNo == "Table 15"):
     i = Database.find("table15_orders")

    elif(tableNo == "Table 16"):
     i = Database.find("table16_orders")



    price = 0
    for item in i:
        price = float(item['price']) + price

    tax =((7.25/100) * price)

    tips = request.args.get('tips')

    total_tips = 0

    if tips is not None:
     total_tips=int(tips)
    else:
        tips=0



    total = price + tax + total_tips


    if(tableNo == "Table 1"):
        items = Database.find("table1_orders")

    elif(tableNo == "Table 2"):
        items = Database.find("table2_orders")

    elif(tableNo == "Table 3"):
        items = Database.find("table3_orders")

    elif(tableNo == "Table 4"):
        items = Database.find("table4_orders")

    elif(tableNo == "Table 5"):
        items = Database.find("table5_orders")

    elif(tableNo == "Table 6"):
        items = Database.find("table6_orders")

    elif(tableNo == "Table 7"):
        items = Database.find("table7_orders")

    elif(tableNo == "Table 8"):
        items = Database.find("table8_orders")

    elif(tableNo == "Table 9"):
        items = Database.find("table9_orders")

    elif(tableNo == "Table 10"):
        items = Database.find("table10_orders")

    elif(tableNo == "Table 11"):
        items = Database.find("table11_orders")

    elif(tableNo == "Table 12"):
        items = Database.find("table12_orders")

    elif(tableNo == "Table 13"):
        items = Database.find("table13_orders")

    elif(tableNo == "Table 14"):
        items = Database.find("table14_orders")

    elif(tableNo == "Table 15"):
        items = Database.find("table15_orders")

    elif(tableNo == "Table 16"):
        items = Database.find("table16_orders")


    return render_template('checkout.html', items = items, total = round(total,2), tax=round(tax,2), tips=tips)



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


@app.route('/finish')
def finish():
    return render_template("finish.html")


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


@app.route('/1to5')
def chance():

    Database.delete("order")
    return render_template("1to5.html")


#running the app(a requirement to run the app
if __name__ == '__main__':
    app.run(port=4996, debug=True)
