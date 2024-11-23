class reliativesManager:
    def __init__(self):
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

    def listRelatives(self):
        for relative in self.relatives:
            print(f"Relative: {relative['Relative']}, Street_name: {relative['Street_name']}, District (Gu): {relative['District (Gu)']}, Latitude: {relative['Latitude']}, Longitude: {relative['Longitude']}")

    def addRelatives(self, latitude, longitude, streetname="-", ditrict="-"):
        
        relative = {'Relative': "Relative_" + str(11),
            'Street_name': streetname, 
            'District (Gu)': ditrict,       
            'Latitude': latitude,
            'Longitude': longitude 
        }
        self.relatives.append(relative)

        
    

relatives = reliativesManager()
relatives.addRelatives(23.2343, 124.232)
relatives.listRelatives()