from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


#hello.html の中に値を渡す。
@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name = name )

@app.route("/omikuji")
def hello(name):
    return render_template("hello.html", name = name )


if __name__ == '__main__':
    app.run(debug=True)
