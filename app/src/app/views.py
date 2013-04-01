# To change this template, choose Tools | Templates
# and open the template in the editor.

from app import app
from flask import render_template 

@app.route('/')
@app.route('/index')
def index1():
    return "Hello, World!"


#practica 2
@app.route('/practica2')
def index2():
    user = { 'nickname': 'Stfy' } # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

#practica 3
@app.route('/')
@app.route('/practica3')
def index3():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index2.html",
        title = 'Home',
        user = user)
