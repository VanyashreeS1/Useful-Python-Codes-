from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Jhon!</h1>'

@app.route('/information')
def info():
    return '<h1>Jhon is doing well!</h1>'

@app.route('/index/<name>')
def index(name):
    # Page for an individual Name.
    return '<h1>This is a page for {}</h1>'.format(name)

if __name__ == '__main__':
    # Never have debug=True for production apps!
    app.run(debug=True)
