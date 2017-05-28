import pprint
import googlemaps
import time


#------------------------------------------------------------------------------
#
def get_location_coordinates(client, address=None):
    response = client.geocode(address)
    #pprint.pprint(response)
    return response[0]['geometry']['location']

#------------------------------------------------------------------------------
#
def get_places_nearby(client, location, radius, type=None):

    response = client.places_nearby( location,
                                     radius,
                                     type)
    ##pprint.pprint(response)
    found_places = []
    idx = 0

    while (response['status'] == 'OK'):

        results = response['results']
        for result in results:

            print()
            print("---[ %d ]--------------------------------" % idx)
            print("Name:        %s" % result['name'])
            print("Address:     %s" % result['vicinity'])
            print("Work hours:  %s" % result.get('opening_hours', ""))

            found_places.append({'name':result['name'],
                                 'address':result['vicinity'],
                                 'hours':result.get('opening_hours','')})
            idx += 1

        next_page_token = response.get('next_page_token', '')
        if next_page_token:
            print("\nPlease, wait. Fetching next page...")
            time.sleep(2)
            response = client.places_nearby(location,
                                            page_token=next_page_token)
        else:
            response['status'] = 'finished'

    return found_places

#------------------------------------------------------------------------------
#
def google_maps():
    # https://console.developers.google.com/apis/library
    # https://console.developers.google.com/cloud-resource-manager
    # https://developers.google.com/places/web-service/get-api-key
    # https://developers.google.com/products/

    api_key = 'AIzaSyDu-cscl23SX3uxUbid5WyPFI1aDTaq-u0'
    client = googlemaps.Client(key=api_key)

    # current_location = {'lat': 46.60042199999999,
    #                     'lng': 30.8118901}
    current_location = get_location_coordinates(client, "Amsterdam")

    # https://developers.google.com/places/supported_types
    get_places_nearby(client, current_location, 100, 'food')
    get_places_nearby(client, current_location, 100, 'gym')
    get_places_nearby(client, current_location, 100, 'post_office')

    get_places_nearby(client, current_location, 100, 'food|gym|post_office')

###############################################################################
#
if __name__ == "__main__":
    google_maps()