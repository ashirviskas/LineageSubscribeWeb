from flask import Flask
from flask import render_template




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home(devicenames = ['Unreachable', 'server']):
    return render_template('main.html', devicenames=devicenames)
