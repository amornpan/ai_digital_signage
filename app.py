from flask import Flask

# app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



# @app.route('/')
# def hello():
#     return 'Hello, World!'
#
# if __name__ == '__main__':
#     app.run(host='113.53.253.40', port='5001', debug=True)