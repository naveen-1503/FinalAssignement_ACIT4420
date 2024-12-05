#calculateDistance.py

from geopy.distance import geodesic
from logger import log_function_call

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

@log_function_call
def shortestDist(distArr):
    
    sDistArr= list({dist['From_Relative'] for dist in distArr}.union({dist['To_Relative'] for dist in distArr}))
    sDistArr.sort()
    num_relatives = len(sDistArr)

    dist_matrix = {rel: {rel: float('inf') for rel in sDistArr} for rel in sDistArr}
    for entry in distArr:
        dist_matrix[entry['From_Relative']][entry['To_Relative']] = entry['TotalDistance']    
        dist_matrix[entry['From_Relative']][entry['To_Relative']] = entry['TotalDistance']    

    current = sDistArr[0]
    path = [current]
    total_distance = 0
    route_details = []

    while len(path) < num_relatives:
        next_relative = None
        shortestDist = float('inf')
        
        for neighbor, dist in dist_matrix[current].items():
            if neighbor not in path and dist < shortestDist:
                next_relative = neighbor
                shortestDist = dist
        path.append(next_relative)
        total_distance += shortestDist
        route_details.append({
            "From_Relative": current,
            "To_Relative": next_relative,
            "Distance": shortestDist
        })     
        current = next_relative   

        

    total_distance += dist_matrix[current][path[0]]
    path.append(path[0]) 
    route_details.append({
        "From_Relative": current,
        "To_Relative": path[0],
        "Distance": total_distance
    })       
    return {'Path': path, 'Total_Distance': total_distance, 'route_details': route_details}
        

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