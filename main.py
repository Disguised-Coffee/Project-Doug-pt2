from flask import Flask, render_template, jsonify

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
    "link":"https://www.youtube.com/embed/QR3xhMsk2Ak",
    "id":0,
    "caption":"Hello World!",
    "name":"DOG"
  }
]

@app.route("/")
def hello_world():
    return render_template('index.html',jobs=BS_CODE)

@app.route("/jobs")
def list_jobs():
  return jsonify(BS_CODE)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)