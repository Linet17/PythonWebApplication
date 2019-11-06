#step1 :creating templates and layouts

from flask import Flask,render_template 
#render_template is a function in Flask class that helps run html files and code in python

app = Flask(__name__)


# a route is a path that you can access a html page,this line creates a path for the app
#by default this will be our 'Home' page/route
@app.route('/')
def hello_world():
    return render_template('index.html') # file rendered should be a string
    # return 'Hello World!'

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/inventories')
def inv_page():
    return render_template('inv.html')
#condition that makes sure that this app only runs if this app is the main app
if __name__ == '__main__':
    app.run()
#ststic - stores css,javascript,images,photos files etc basically the static files eg files on bootstrap
#templates - any and all html files

#Steps done so far
#1.created a flask project
#2.created routes i.e. @app.rout('/') then wrapped a function in that route by defining whatever function that'll run once that route is called
#3.created the html pages,stored them under templates folder
#4.serve the html pages with the use of render_template i.e. displaying the html files as web pages
#5.connect to bootstrap4
#6.copy the navbar code
#7.edit your navbar to suite your app