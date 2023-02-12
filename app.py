from flask import Flask, render_template, request


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
@app.route('/PennyPinch/templates/quiz.html', methods= ['GET', 'POST'])
def quiz():
    splugerTotal = 0
    hoarderTotal = 0
    fomoTotal = 0
    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    email = ""
    password = ""

    if request.method == 'POST':
        #if the user presses submit, we will store their answers in local variables
        answer1 = request.form.get('answer1', '')
        answer2 = request.form.get('answer2', '')
        answer3 = request.form.get('answer3', '')
        answer4 = request.form.get('answer4', '')
        email = request.form.get('emailAddress', '')
        password = request.form.get('password', '')
        return render_template('plan.html')

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


