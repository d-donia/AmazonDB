from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/insert')
def insert():  # put application's code here
    return render_template("insert.html")

@app.route('/delete')
def delete():  # put application's code here
    return render_template("delete.html")

@app.route('/modify')
def modify():  # put application's code here
    return render_template("modify.html")

@app.route('/search')
def search():  # put application's code here
    return render_template("search.html")


if __name__ == '__main__':
    app.run()
