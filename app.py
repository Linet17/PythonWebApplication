# static - stores css,javascript,images,photos files etc basically the static files eg files on bootstrap
# templates - any and all html files
# tailwind - another framework like bootstrap
# scrimba.com - best for learning frontend languages eg html

# step1 :creating templates and layouts
# render_template is a function in Flask class that helps run html files and code in python

# read on http - used for communication and transmission of messages across that internet

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from configs import Developement
import pygal
import psycopg2

# flask object/instance
app = Flask(__name__)
# tell flask which configurations to use,its default configurations or yours
# has to come between flask instance and db instance
app.config.from_object(Developement)
# create a sqlalchemy instance and pass the flask app object
db = SQLAlchemy(app)

# import the models,comes right after instantiating SQLAlchemy object
# from models.inventories import InventoryModel

from models.inventories import InventoryModel
from models.sales import SalesModel


# use a decorator that before any request is made,it looks for specific tables defined in models that  have been created in db,if yes doesnt create any..if no,creates table
@app.before_first_request
def createTable():
    # db.drop_all()
    db.create_all()


# a route is a path that you can access a html page,this line creates a path for the app
# by default this will be our 'Home' page/route

# any route by default answers to a get http request.
@app.route('/')
def hello_world():
    return render_template('index.html')  # file rendered should be a string
    # returns 'Hello World!'


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/about')
def about_page():
    if request.method == 'POST':
        invName = request.form['inventory']
        type = request.form['type']
        buyingPrice = request.form['buyingPrice']
    return render_template('about.html')


# GET USED TO RENDER TEMPLATES
@app.route('/inventory', methods=['GET', 'POST'])
def inv_page():
    # if the request method is post,then
    if request.method == 'POST':
        invName = request.form['inventory']
        type = request.form['type']
        buyingPrice = request.form['buyingPrice']

        # create/instantiate a python object of the class(s) that have the form(s) you create
        # call column in table in table class ie InventoryModel class = value gotten from modal form eg inv_name=invName
        me = InventoryModel(inv_name=invName, inv_type=type, buyingPrice=buyingPrice)
        # adding above object to user session not the flask session but the SQLQlchemy session
        db.session.add(me)
        db.session.commit()
        print("Successfully run!")

        # getting all the records in the table in the abcDB DB
        # instantiate an object where you'll run your query
        # query - acts as a select,a class
        # all() is a method,selecting all
        value = InventoryModel.query.all()
        print(value)
        for i in value:
            print(i.inv_name, i.inv_type, i.buyingPrice)

            # print(invName)
            # print(type)
            # print(buyingPrice)

        return render_template('inv.html', inventories=value)


@app.route('/dashboard')
def pie_chart():
    conn = psycopg2.connect("dbname='salesDemo',user='postgres',host='localhost',password='0000'")
    cur = conn.cursor()
    cur.execute("""SELECT extract(year from created_at)as exactYear, sum(quantity)over(partition by created_at,inventory_id)totQuantity
	FROM public.sales
	order by created_at""")

    rows = cur.fetchall()
    print(type(rows))
    for each in rows:
        print(each)
    # a = []
    # b = []
    # for each in rows:
    #     a.append(each[0])
    #     b.append(each[1])
    #
    # print(a)
    # print(b)

    # ratios = {'Gentlemen': '8', 'ladies': 4}
    ratios = [('Gentlemen', 5), ('Ladies', 9)]

    pie_chart = pygal.pie()
    # pie_chart = pie_chart.title('My first piechart represeting ratio of male and remale in our python class')
    pie_chart.title = ('My first piechart represeting ratio of male and remale in our python class')

    # pie_chart = pie_chart.add('Getlemen', data.gentlemen)
    # pie_chart = pie_chart.add('Ladies', data.ladies)

    pie_chart = pie_chart.add(ratios[0][0], ratios[0][1])
    pie_chart = pie_chart.add(ratios[0][0], ratios[0][1])

    pie_data = pie_chart.render_data_uri()

    data = [
        {'month': 'January', 'total': 22},
        {'month': 'February', 'total': 27},
        {'month': 'March', 'total': 23},
        {'month': 'April', 'total': 20},
        {'month': 'May', 'total': 12},
        {'month': 'June', 'total': 32},
        {'month': 'July', 'total': 42},
        {'month': 'August', 'total': 72},
        {'month': 'September', 'total': 52},
        {'month': 'October', 'total': 42},
        {'month': 'November', 'total': 92},
        {'month': 'December', 'total': 102}
    ]

    # month[0][month]

    x = []
    y = []

    for each in data:
        x.append(each.month)
        y.append(each.total)

    line_graph = pygal.line()
    # line_graph = line_graph.title('My first piechart represeting ratio of male and remale in our python class')
    line_graph.title = ('My first line graph represeting ratio of male and remale in our python class')
    line_graph = line_graph.labels = x
    line_graph = line_graph.add('Total monthly sale', y)
    line_data = line_graph.render_data_uri()

    return render_template('dashboard.html', pie_data=pie_data,line_data=line_data)


@app.route('/sales', methods=['POST'])
def sales():
    # if the request method is post,then
    if request.method == 'POST':
        qnty = request.form['quantity']
        print(qnty)
        return redirect(url_for('inv_page'))


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


# condition that makes sure that this app only runs if this app is the main app
if __name__ == '__main__':
    app.run()

# Steps done so far
# 1.created a flask project
# 2.created routes i.e. @app.rout('/') then wrapped a function in that route by defining whatever function that'll run once that route is called
# 3.created the html pages,stored them under templates folder
# 4.serve the html pages with the use of render_template i.e. displaying the html files as web pages
# 5.connect to bootstrap4
# 6.copy the navbar code
# 7.edit your navbar to suite your app
