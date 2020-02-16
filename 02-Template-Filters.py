from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a book name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /book/name </h1>'

@app.route('/book/<name>')
def book_name(name):
    # Pass in a book name
    # We insert it to the html with jinja2 templates!
    return render_template('02-Template-Filters.html',name=name)



if __name__ == '__main__':
    app.run(debug=True)
