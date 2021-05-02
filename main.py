from flask import Flask, render_template, request

app = Flask("Scrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", searchingBy=word)

app.run(host="0.0.0.0")
