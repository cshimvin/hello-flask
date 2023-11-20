# Import OS from Python library
import os

# Import Flask class and the HTML template renderer
from flask import Flask, render_template

# Create an instance of the Flask class and assign it to the app variable
app = Flask(__name__)

# Decorator function
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True   # Only use debug=true when testing. Use debug=false in production
    )
