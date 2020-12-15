"""A web scraper that scrapes the RIT dining website"""

import urllib.request as request
from dataclasses import dataclass
from datetime import datetime
from json import JSONEncoder, dumps
from sys import argv
from bs4 import BeautifulSoup
from bs4.element import Tag

@dataclass
class TimeSegment:
    """
    A data class that represents a segment of time for which a dining location
    is open. If a location is open for lunch and dinner the time for those two
    'segments' is in two different tables on the dining website.
    """
    hours: str
    # segment_name: str

@dataclass
class Location:
    """
    A data class that represents a dining location on campus
    """
    name: str
    hours: [TimeSegment]

class LocationEncoder(JSONEncoder):
    """
    A class that serializes a Location dataclass into JSON
    """
    # pylint:disable=inconsistent-return-statements 
    def default(self, o):
        if isinstance(o, Location):
            return {
                'name': o.name,
                'hours': list(map(lambda ts: ts.hours, o.hours))
            }

def pretty_print_locations(locations):
    """
    Pretty prints the hours of a all dining locations in a human readable
    format.
    """
    for location in locations:
        print(location.name)
        print('=====')
        for time_segment in location.hours:
            print(time_segment.hours)
        print('\n')

def new_location(name):
    """Creates a new location dataclass with the specified name"""
    return Location(name, [])

def fetch_locations(day, month, year):
    """ fetches the hours for all dining locations on the given date. """
    # pylint: disable=line-too-long 
    hours_page = 'https://www.rit.edu/fa/diningservices/places-to-eat/hours?date=' + str(year) + '-' + str(month) + '-' + str(day) + '&format=day'
    lst = []

    page = request.urlopen(hours_page)
    soup = BeautifulSoup(page, 'html.parser')
    location_container = soup.find('div', class_='view-content')

    location_name = location_container.contents[3].text.strip()
    location = Location(location_name, [])
    for item in location_container.contents[4:]:
        # Ignoring NavigableStrings, not sure why they are here in the first place
        if isinstance(item, Tag):
            # Tags with hours-title class only have one class
            if item['class'][0] == 'hours-title':
                lst.append(location)
                location_name = item.text.strip()
                location = new_location(location_name)
            else:
                close = item.find('div', class_='col-sm-5')
                if close is not None:
                    hours = str(close.contents[0]).strip()
                else:
                    hours = 'Closed'

                location.hours.append(TimeSegment(hours))
    lst.append(location)
    return lst

def fetch_locations_json(day, month, year):
    """
    fetches the hours for all dining locations on campus in a JSON block.
    """
    return dumps(fetch_locations(day, month, year), cls=LocationEncoder)

def main():
    """
    command line interface for the web scraper.
    """
    if len(argv) > 1:
        month_str = argv[1]
        day_str = argv[2]
        year_str = argv[3]
    else:
        todays_date = datetime.now()
        day_str = str(todays_date.day)
        month_str = str(todays_date.month)
        year_str = str(todays_date.year)

    locations = fetch_locations(day_str, month_str, year_str)
    print('\n==' + month_str + '/' + day_str + '/' + year_str + '==\n')
    pretty_print_locations(locations)

if __name__ == '__main__':
    main()
