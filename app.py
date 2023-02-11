from flask import Flask, render_template

app = Flask(__name__) # __name__ refers to the module name

#@app.route('/') # Python decorator, new syntax
@app.get('/')
def index():
    return render_template('index.html')

#def about():
    #return '<h1>about</h1>'

# @app.get('/about')
# def about():
#     return render_template('about.html')

# @app.get('/home')
# def about():
#     return render_template('index.html')

# @app.get('/plan')
# def about():
#     return render_template('plan.html')

# @app.get('/quiz')
# def about():
#     return render_template('quiz.html')

@app.get('/PennyPinch/templates/resources.html')
def resources():
    return render_template('resources.html')