from geopy.geocoders import Nominatim
import csv

class MapModel:
    def __init__(self):
        self.location_suggestions = 'locations.csv'
        pass

    def get_data(self, file_path):
        data = []
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                contents = row[0].split(';')
                data.append(contents)
        return data

    def find_location(self, lat, lon):
        geolocator = Nominatim(user_agent="MapApp")

        coordinates = f"{lat}, {lon}"

        location = geolocator.reverse(coordinates)

        return location.address

    def find_suggestions(self, text):
        text = text.lower()
        data = []
        location_dict = dict()

        with open(self.location_suggestions, 'r', newline='', encoding='utf-8') as csvfile:  # Retrieve saved locations from the csv file (each row has a location, hence no need for string manipulation)
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for word in row:
                    data.append(word)
                    location_dict[word.lower()] = 0

        characters = [*text]
        for i, location in enumerate(data):  # Compare each character and add points for similar characters
            location = location.lower()
            location_characters = [*location]

            for j, character in enumerate(characters):
                if j < len(location_characters):
                    if characters[j] == location_characters[j]:
                        location_dict[location] += 1
                    else:
                        break
                else:
                    break

        sorted_locations = sorted(location_dict, key=lambda x: location_dict[x], reverse=True)  # returns a list of keys, with descending order, hence highest val location is at [0] index
        highest_val = location_dict.get(sorted_locations[0])

        suggestions = []
        for location, value in location_dict.items():
            if value == highest_val:  # no need to check for the > condition, since we are using the highest value
                suggestions.append(location)

        if highest_val >= 1:
            return suggestions
        else:
            return []

