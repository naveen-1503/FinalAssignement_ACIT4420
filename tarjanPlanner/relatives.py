#relatives.py
from logger import log_function_call
import json
import re 

LATITUDE_PATTERN = r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$"
LONGITUDE_PATTERN = r"^[-+]?((1[0-7]\d|[1-9]?\d)(\.\d+)?|180(\.0+)?)$"

def is_valid_latitude(latitude):
    return bool(re.match(LATITUDE_PATTERN, latitude))

def is_valid_longitude(longitude):
    return bool(re.match(LONGITUDE_PATTERN, longitude))

class reliativesManager:
    def __init__(self, file_name='relatives.json'):
        self.file_name = file_name
        #Creates a dictonary with all relatives we already know
        self.relatives = [
            {"Relative": "Relative_1", "Street_name": "Gangnam-daero", "District (Gu)": "Gangnam-gu", "Latitude": 37.4979, "Longitude": 127.0276},
            {"Relative": "Relative_2", "Street_name": "Yangae-daero", "District (Gu)": "Secho-gu", "Latitude": 37.4833, "Longitude": 127.0322},
            {"Relative": "Relative_3", "Street_name": "Sinsa-daero", "District (Gu)": "Gangnam-gu", "Latitude": 37.5172, "Longitude": 127.0286},
            {"Relative": "Relative_4", "Street_name": "Apgujeong-ru", "District (Gu)": "Gangnam-gu", "Latitude": 37.5219, "Longitude": 127.0411},
            {"Relative": "Relative_5", "Street_name": "Hannam-daero", "District (Gu)": "Yongsan-gu", "Latitude": 37.5340, "Longitude": 127.0026},
            {"Relative": "Relative_6", "Street_name": "Seongsu-daero", "District (Gu)": "Seongdong-gu", "Latitude": 37.5443, "Longitude": 127.0557},
            {"Relative": "Relative_7", "Street_name": "Cheongdam-ro", "District (Gu)": "Gangnam-gu", "Latitude": 37.5172, "Longitude": 127.0391},
            {"Relative": "Relative_8", "Street_name": "Bukhan-ro", "District (Gu)": "Jongno-gu", "Latitude": 37.5800, "Longitude": 126.9844},
            {"Relative": "Relative_9", "Street_name": "Samseong-ro", "District (Gu)": "Gangnam-gu", "Latitude": 37.5100, "Longitude": 127.0590},
            {"Relative": "Relative_10", "Street_name": "Jamsil-ro", "District (Gu)": "Songpa-gu", "Latitude": 37.5133, "Longitude": 127.1028}
        ]
        self.save_relatives()

    #Saves the relatives in the json file
    def save_relatives(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.relatives, file, indent=4)

    #List the relatives in the json files
    def listRelatives(self):
        for relative in self.relatives:
            print(f"Relative: {relative['Relative']}, Street_name: {relative['Street_name']}, District (Gu): {relative['District (Gu)']}, Latitude: {relative['Latitude']}, Longitude: {relative['Longitude']}")

    @log_function_call
    #Function to add the relatives
    def addRelatives(self, streetname, ditrict, latitude, longitude):
        # Validate inputs
        if not is_valid_latitude(latitude):
            raise ValueError(f"Invalid latitude: {latitude}")
        if not is_valid_longitude(longitude):
            raise ValueError(f"Invalid longitude: {longitude}")
        
        relative = {'Relative': "Relative_" + str(len(self.relatives) + 1),
            'Street_name': streetname, 
            'District (Gu)': ditrict,       
            'Latitude': latitude,
            'Longitude': longitude 
        }
        self.relatives.append(relative)

    @log_function_call
    #Function for removing the relative
    def remove_relative(self, relative):
        if not self.relatives:
            raise ValueError("No relatives to remove")
        
        initial_length = len(self.relatives)
        self.relatives = [c for c in self.relatives if c['Relative'] != relative]
        if len(self.relatives) == initial_length:
            raise ValueError(f"Relative that lives in {relative}, not found")   
    
    def get_relatives(self):
        return self.relatives


"""relatives = reliativesManager()
relatives.addRelatives(23.2343, 124.232)
relatives.listRelatives()"""