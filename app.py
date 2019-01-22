from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Deployed to heroku</h1>'
@app.route("/api")
def api():
    return 'this is the api route'
if __name__ == '__main__':
    app.run(port = 9000)
