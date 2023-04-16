from flask import Flask, render_template, jsonify
from replit import db


app = Flask(__name__)

"""
 Sample 
  {
    "link":"https://www.youtube.com/embed/QR3xhMsk2Ak",
    "id":0,
    "caption":"Hello World!",
    "name":"DOG"
  }
"""

BS_CODE = [
  {
    "link": "https://www.youtube.com/embed/0DPZ9b9ZZr4",
    "id": 0,
    "caption": "Video of dogs doing cute and funny things",
    "name": "Cute Dog Complimation"
  }, 
  {
    "link": "https://www.youtube.com/embed/Sg4hFC9rrzI",
    "id": 1,
    "caption": "Silly cats and dogs",
    "name": "Cat and Dogs Video"
  }, 
  {
    "link": "https://www.youtube.com/embed/PDj0gR_xsYE",
    "id": 0,
    "caption": "Proof that German Shepards are fantastic dogs",
    "name": "German Shepards"
  },
]

@app.route("/")
def hello_world():
    return render_template('index.html',jobs=BS_CODE)

@app.route("/jobs")
def list_jobs():
  return jsonify(BS_CODE)

"""
@app.route("/", method=['POST','GET'])
def hello_world():
    return render_template('index.html',jobs=BS_CODE)
"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)