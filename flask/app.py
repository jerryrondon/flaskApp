import os
from flask import Flask

app = Flask(__name__)

@app.route("/about", methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')

    return {'app_version': version}, 200


@app.route("/secrets", methods=['GET'])
def secrets():
    creds = dict()
    creds['db_password'] = os.environ.get('DB_PASSWORD')

    return creds, 200
