from geopy.distance import geodesic

def calculateDistance(x):
    distArr = []
    for relative_x in x:
        for relative_y in x:
            if relative_x['Relative'] != relative_y['Relative']:
                distance1 = (relative_x['Latitude'], relative_x['Longitude'])    
                distance2 = (relative_y['Latitude'], relative_y['Longitude'])    
                totalDistance = geodesic(distance1,distance2).km

                distArr.append({"From_Relative": relative_x['Relative'], "To_Relative": relative_y['Relative'], "TotalDistance": round(totalDistance,2)})
    
    return distArr    

def shortestDist(distArr):
        
    sDistArr={}
    for relative in distArr:
        if relative['From_Relative'] not in sDistArr or relative['TotalDistance'] < sDistArr[relative['From_Relative']]['TotalDistance']:
            sDistArr[relative['From_Relative']] = {
                "To_Relative": relative['To_Relative'],
                "TotalDistance": relative['TotalDistance']
            }      
            
           
        shortDist = [
            {"From_Relative": relative['From_Relative'], "To_Relative": data['To_Relative'], "TotalDistance": data['TotalDistance']}
            for relative['From_Relative'], data in sDistArr.items()
        ]
            
                
    
    for item in shortDist:
        print(item)
        

x = [
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

dist = calculateDistance(x)
shortestDist(dist)