from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"type": 100, "link": "http://localhost:5000/file.tgz"}

@app.route("/file.tgz")
def download():
    return send_file("file.tgz", as_attachment=True)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
