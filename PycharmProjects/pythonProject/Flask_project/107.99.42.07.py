from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("107.99.42.07.html")


if __name__ == "__main__":
    app.run(debug=True)

app.route(port=8000)
