from flask import Flask, request
from flask import render_template
from pymongo import MongoClient
from pprint import pprint
import configparser

config = configparser.ConfigParser()
config.read("config")

client = MongoClient('localhost')
Releases_col = client.LineageReleases.releases
app = Flask(__name__)

def get_device_names():
    device_names = list(Releases_col.distinct('device', {}))
    return device_names[:-1]


@app.route('/', methods=['GET', 'POST'])
def home(devicenames = ['Unreachable server']):
    return render_template('main.html', devicenames=get_device_names())


@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    device_name = request.form['device']
    user_email = request.form['email']
    pprint(request.form)
    return "Ahoy, subbed " + device_name + " to " + user_email

app.run(host= '0.0.0.0', port=80)