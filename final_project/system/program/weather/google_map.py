import googlemaps

# 위치 정보 입력
def where(text):
    api_key = 'AIzaSyBZ-JL8XVJVBUBdDHOaE6NSf-vaE0NoCIQ'
    maps = googlemaps.Client(key=api_key)

    results = maps.geocode(text)
    for result in results:
        lat = result['geometry']['location']['lat']
        lon = result['geometry']['location']['lng']
    return lat, lon