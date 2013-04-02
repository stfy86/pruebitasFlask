# To change this template, choose Tools | Templates
# and open the template in the editor.
from flask import render_template
from app import app

@app.route('/')
@app.route('/index1')
def index1():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
        

@app.route('/index2')
def index2():
    user = { 'nickname': 'stfy' } # fake user
    return render_template("index2.html",
        title = 'home2',
        user = user)  
        
@app.route('/index3')
def index3():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index3.html",
        title = 'Home',
        user = user,
        posts = posts)
        
@app.route('/index5')
def index5():
    user = { 'nickname': 'Stfy index 5' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index5.html",
        title = 'Home',
        user = user,
        posts = posts)        