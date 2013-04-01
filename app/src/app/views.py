# To change this template, choose Tools | Templates
# and open the template in the editor.

from app import app

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
