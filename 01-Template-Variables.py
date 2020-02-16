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
    return render_template('01-Template-Variables.html',name=name)

@app.route('/advbook/<name>')
def adv_book_name(name):
    letters = list(name)
    book_dict = {'book_name':name}
    return render_template('01-Template-Variables.html',
                           name=name,mylist=letters,mydict=book_dict)


if __name__ == '__main__':
    app.run(debug=True)
