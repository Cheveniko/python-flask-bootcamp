from flask import Flask, render_template

app2 = Flask(__name__)

nums = list(range(1, 101))

@app2.route("/")
def hola():
    return render_template("fizzbuzz.html", nums=nums)
