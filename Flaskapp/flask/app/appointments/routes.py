from flask import Flask, render_template, Blueprint
import requests
import json
import redis

appointments = Blueprint('appointments', __name__)


@appointments.route('/appointments')
def index():
    req = requests.get('https://hr.apografi.gov.gr/api/public/organizations/')
    data = req.content
    json_data = json.loads(data)
    r_server =  redis.Redis(host='redis', port=6379)
    for data in json_data['data']:
        r_server.set(data['code'],data['preferredLabel'])

    return render_template('appointments.html', data = json_data['data'], r = r_server)
    
