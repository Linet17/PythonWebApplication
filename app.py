# static - stores css,javascript,images,photos files etc basically the static files eg files on bootstrap
# templates - any and all html files
#tailwind - another framework like bootstrap
#scrimba.com - best for learning frontend languages eg html

# step1 :creating templates and layouts
# render_template is a function in Flask class that helps run html files and code in python

#read on http - used for communication and transmission of messages across that internet

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from configs import Developement



#flask object/instance
app = Flask(__name__)
#tell flask which configurations to use,its default configurations or yours
#has to come between flask instance and db instance
app.config.from_object(Developement)
# create a sqlalchemy instance and pass the flask app object
db = SQLAlchemy(app)

#import the models,comes right after instantiating SQLAlchemy object
from models.inventories import InventoryModel
#use a decorator that before any request is made,it looks for specific tables defined in models that  have been created in db,if yes doesnt create any..if no,creates table
@app.before_first_request
def createTable():
    # db.drop_all()
    db.create_all()


# a route is a path that you can access a html page,this line creates a path for the app
# by default this will be our 'Home' page/route

#any route by default answers to a get http request.
@app.route('/')
def hello_world():
    return render_template('index.html')  # file rendered should be a string
    # returns 'Hello World!'


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/about')
def about_page():
    return render_template('about.html')

#GET USED TO RENDER TEMPLATES
@app.route('/inventory',methods=['GET','POST'])
def inv_page():
    #if the request method is post,then
    if request.method =='POST':
        invName = request.form['inventory']
        type = request.form['type']
        buyingPrice = request.form['buyingPrice']

        # create/instantiate a python object of the class(s) that have the form(s) you create
        #call column in table in table class ie InventoryModel class = value gotten from modal form eg inv_name=invName
        me = InventoryModel(inv_name=invName, inv_type=type, buyingPrice=buyingPrice)
        # adding above object to user session not the flask session but the SQLQlchemy session
        db.session.add(me)
        db.session.commit()
        print("Successfully run!")

    #getting all the records in the table in the abcDB DB
    #instantiate an object where you'll run your query
    #query - acts as a select,a class
    #all() is a method,selecting all
    value = InventoryModel.query.all()
    print(value)

        # print(invName)
        # print(type)
        # print(buyingPrice)

    return render_template('inv.html')


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
