from flask import Flask
from flask import redirect, url_for, jsonify
from flask import request
import json

app = Flask(__name__)

if not app.debug:
    import logging
    from logging import FileHandler
    from logging import Formatter

    # Create a log file for errors
    file_handler = FileHandler(filename='errors.log')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)
    

@app.route('/')
def home():
    return redirect(url_for('static',filename='index.html'))

@app.route('/save', methods=['PUT','POST'])
def get_events():
    '''
    Function to get nearby events corresponding to a location
    entered by user.

    Input: Expects JSON object containing lat lon of searched 
           location

    Returns: a JSON object containing Event objects
             0 if error is found
    '''  
    # Get JSON object containing lat lon for Event
    coordinates = request.json
    
    if type(content) is not dict:
        app.logger.error('Invalid format of JSON object')
        # Return a specific value?
        return -1
    
    lat = coordinates.get('lat')
    lon = coordinates.get('lon')

    if any((lat, lon)) is None:
        app.logger.error('Invalid lat lon')
        return -1
    
    # TODO
    # Send lat lon to function to get a list of Events from the
    # database

@app.route('/', methods=['PUT', 'POST'])
def put_event():
    '''
    Function to get event details and put in database

    Input: Expects a JSON object with event Name, Location as
           (lat,lon), Address 

    Returns: 0 if success
             -1 if error
    '''
    new_event = request.json

    if type(content) is not dict:
        app.logger.error('Invalid format of JSON object')
        # Return a specific value?
        return -1

    if len(new_event) != 3:
        app.logger.error('Invalid length of JSON object')
        return -1

    event_name = new_event.get('Name')
    event_lat = new_event.get('Location').get('lat')
    event_lon = new_event.get('Location').get('lon')
    event_address = new_event.get('Address')

    if any((event_name, event_lon, event_lat, event_address)) is None:
        app.logger.error("Invalid values in Event Info")
        return -1

    # Create an Event object and store it in the database    
    # TODO


if __name__=='__main__':
    app.run(debug=True)