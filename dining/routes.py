from dining import app
from .scraper import fetch_locations_json
from datetime import datetime
from flask import request

@app.route('/api/v1/hours', methods=['GET'])
def fetch_hours():
    if len(request.args) > 0:
        day = int(request.args['day'])
        month = int(request.args['month'])
        year = int(request.args['year'])
    else:
        todays_date = datetime.now()
        day = todays_date.day
        month = todays_date.month
        year = todays_date.year
    return fetch_locations_json(day, month, year) 

