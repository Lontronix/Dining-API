"""
An API that displays the hours of operation for dining locations on campus
"""

from flask import Flask
app = Flask(__name__)

# pylint: disable=wrong-import-position
from . import routes
