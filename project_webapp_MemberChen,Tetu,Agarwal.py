def get_json(url):
   import urllib.request
   import json
   from pprint import pprint
   f = urllib.request.urlopen(url)
   response_text = f.read().decode('utf-8')
   response_data = json.loads(response_text)
   return response_data

   # """
   # Given a properly formatted URL for a JSON web API request, return
   # a Python JSON object containing the response to that request.
   # """
   # pass


def get_lat_long(place_name):
   """
   Given a place name or address, return a (latitude, longitude) tuple
   with the coordinates of the given place.
   See https://developer.mapquest.com/documentation/geocoding-api/address/get/
   for Mapquest Geocoding  API URL formatting requirements.
   """
   url='http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}'.format(MAPQUEST_API_KEY, place_name)
   response_data=get_json(url)
   result = response_data['results'][0]['locations'][0]["latLng"]['lat'], response_data['results'][0]['locations'][0]["latLng"]['lng']
   return result

# print(get_lat_long('BabsonCollege,MA'))




def get_nearest_station(latitude, longitude):

   """
   Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
   tuple for the nearest MBTA station to the given coordinates.
   See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
   formatting requirements for the 'GET /stops' API.
   """
   url = '{}?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_BASE_URL, MBTA_API_KEY,
                                                                                       latitude, longitude)
   response_data=get_json(url)
   # print(response_data)
   result=response_data['data'][0]['attributes']['name'], response_data['data'][0]['attributes']['wheelchair_boarding']
   return result

# print(get_nearest_station(*get_lat_long('Boston+Common,MA')))



def find_stop_near(place_name):
   """
   Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
   """
   stop = get_nearest_station(*get_lat_long(place_name))
   return stop

