from flask import Flask, render_template             
app = Flask(__name__,template_folder='template')
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('index.html',name=name)
	
if __name__ == "__main__":
    app.run(debug=True)