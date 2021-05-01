from flask import Flask

app = Flask("Scrapper")

@app.route("/")
def home():
  return "<h1>Job Serch</h1>"

app.run(host="0.0.0.0")
