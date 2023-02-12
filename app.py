from flask import Flask, render_template

app = Flask(__name__) # __name__ refers to the module name

#@app.route('/') # Python decorator, new syntax
@app.get('/')
def index():
    return render_template('index.html')

#page to resources
@app.get('/PennyPinch/templates/resources.html')
def resources():
    return render_template('resources.html')

#page to about
@app.get('/PennyPinch/templates/about.html')
def about():
    return render_template('about.html')

#page to quiz
@app.get('/PennyPinch/templates/quiz.html')
def quiz():
    return render_template('quiz.html')

#page to plan
@app.get('/PennyPinch/templates/plan.html')
def plan():
    return render_template('plan.html')

#page to splurger
@app.get('/PennyPinch/templates/splurger.html')
def splurger():
    return render_template('splurger.html')

#page to hoarder 
@app.get('/PennyPinch/templates/hoarder.html')
def hoarder():
    return render_template('hoarder.html')

#page to fomo
@app.get('/PennyPinch/templates/fomo.html')
def fomo():
    return render_template('fomo.html')