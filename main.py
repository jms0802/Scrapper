from flask import Flask

app = Flask("Scrapper")

@app.route("/")
def home():
  return "Welcome to my site!"

@app.route("/contact")
def contact():
  return "Contact Me!"

app.run(host="0.0.0.0")