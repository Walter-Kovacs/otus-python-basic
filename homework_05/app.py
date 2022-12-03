from flask import Flask, render_template

app = Flask(__name__)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
