from flask import Flask
from ejemplo import hi
from utils.functions import segmentar
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Deployed to heroku</h1>'
@app.route("/api")
def api():
    return hi()
@app.route("/api/segmentation")
def segmentation():
    return '<h1>here is where segmentation goes</h1>', segmentar(1)
@app.route("/api/post", methods = ['POST'])
def post():
    if request.method == 'POST':
        post = request.form['nm']
        return 'The post is ', post
if __name__ == '__main__':
    app.run(port = 9000)
