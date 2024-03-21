from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import send_file
from sys import platform
app = Flask(__name__, static_url_path='/static')

import os

#cleaned_code.singleImage3DStl ('uploaded_file.png', 'threeDimFile.stl')
tempPath = "TempFolder/"

#placeholder, value from configuration file will be prioritized,
#these values are used only when there's no configuration file
debug_mode = 0
betterPrecision = 0
thickness = 1.5

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)
with app.test_request_context():
    print(url_for('static', filename='cum.css'))
    print(url_for('static', filename='B450M Pro4-F(L5).png'))
    print(url_for('static', filename='logic.js'))
    
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', debug=True)
else:		
    gunicorn_app = app
