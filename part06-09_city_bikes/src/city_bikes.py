# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    """Reads a file containing location data 
    from the stations for city bikes in Helsinki. 
    Returns a dictionary of names of the sations (key) and
    a tuple of location coordinates (longitude, latitude) (value)."""

    stations = {}
    with open(filename) as station_data:
        for station in station_data:
            station = station.strip()
            station_info = station.split(';')

            if station_info[0].lower() == 'longitude':
                continue
            name = station_info[3]
            longitude = float(station_info[0])
            latitude = float(station_info[1])

            stations[name] = (longitude, latitude)
    return stations

def distance(stations: dict, station1: str, station2: str):
    """Returns the distance (km) between the two stations given
    as arguments. The stations are contained in the dictionary 
    passed as the first argument."""
    from math import sqrt

    longitude1 = (stations[station1])[0]
    longitude2 = (stations[station2])[0]
    latitude1 = (stations[station1])[1]
    latitude2 = (stations[station2])[1]

    x_km = (longitude1 - longitude2)*55.26 #55.26 is a constant.
    y_km = (latitude1 - latitude2)*111.2 #111.2 is a constant.
    
    return sqrt(x_km**2 + y_km**2) 

def greatest_distance(stations: dict):
    """Works out the two stations on the list with the greatest distance
    from each other. Returns a tuple, where the first two elements are the
    names of the two stations, and the third element is the distance between the two.
    """
    names = []

    for station in stations:
        names.append(station)

    j = 1 
    greatest = 0
    result = ""
    for i in range(len(names)):
        k = j
        for k in range(j, len(names)):    
            if distance(stations, f"{names[i]}", f"{names[k]}") > greatest:
                greatest = distance(stations, f"{names[i]}", f"{names[k]}")
                result = (names[i], names[k], greatest)
        j += 1

    return result
    
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)