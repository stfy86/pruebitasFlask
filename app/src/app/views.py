# To change this template, choose Tools | Templates
# and open the template in the editor.

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
