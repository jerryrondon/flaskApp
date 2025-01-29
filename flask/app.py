from flask import Flask

app = Flask(__name__)

@app.route("/about", methods=['GET'])
def about():
    version = '0.0.1'

    return {'version': version}, 200