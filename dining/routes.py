"""Routes"""

from datetime import datetime
from flask import request, Response
# pylint: disable=cyclic-import
from . import app
from .scraper import fetch_locations_json

@app.route('/api/v1/hours', methods=['GET'])
def fetch_hours():
    """
    fetches hours of operation for all dining locations on campus either today
    or on a given date.
    """
    if len(request.args) > 0:
        day = int(request.args['day'])
        month = int(request.args['month'])
        year = int(request.args['year'])
    else:
        todays_date = datetime.now()
        day = todays_date.day
        month = todays_date.month
        year = todays_date.year

    return Response(fetch_locations_json(day, month, year), mimetype='application/json')
