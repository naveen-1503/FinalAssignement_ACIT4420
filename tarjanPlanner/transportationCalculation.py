#transportationCalculation.py

from logger import log_function_call
#Calculating the efficiency score by adding the values together
def calculate_efficiency(distance, modes):
   travel_time = distance / modes['speed_kmh']
   transfer_time = modes['transfer_time_min'] / 60
   total_cost = distance * modes['cost_per_km']

   effiency = travel_time + transfer_time + total_cost

   return effiency

@log_function_call
#Comparing the efficency scores to find the best modes. The lowest score for each distance wins
def transportCalc(distArr, modes):
   results = []
   totalTime = 0
   totalCost = 0
   for distance in distArr: 
      best_mode = None
      best_efficiency = float('inf')
      for mode in modes:
         efficiency = calculate_efficiency(distance, mode)
         if efficiency < best_efficiency:
            best_efficiency = efficiency
            best_mode = mode['transport']
            best_mode_properties = mode 
            
      totalCost += distance * best_mode_properties['cost_per_km']
      totalTime += (distance / best_mode_properties['speed_kmh']) + (best_mode_properties['transfer_time_min'] / 60)
      results.append({"Distance_km": distance, "Mode":best_mode, "Total_Time": round(totalTime,2), "Total_Cost": round(totalCost,2)})
   
   

   for item in results:
      print(item)

   return results
#Calculating the Totaltime used on the trip
def totalTime(arr):
   total_time = sum(arr)

   
   print('Total time:', total_time)
   return total_time

#Calculating the Total cost used on the trip
def totalCost(arr):
   total_cost = sum(arr)

   print('Total cost:', total_cost)
   return total_cost

"""relativeDist=[
   {'From_Relative': 'Relative_1', 'To_Relative': 'Relative_2', 'TotalDistance': 1.67},
   {'From_Relative': 'Relative_2', 'To_Relative': 'Relative_1', 'TotalDistance': 1.67},
   {'From_Relative': 'Relative_3', 'To_Relative': 'Relative_7', 'TotalDistance': 0.93},
   {'From_Relative': 'Relative_4', 'To_Relative': 'Relative_7', 'TotalDistance': 0.55},
   {'From_Relative': 'Relative_5', 'To_Relative': 'Relative_3', 'TotalDistance': 2.96},
   {'From_Relative': 'Relative_6', 'To_Relative': 'Relative_4', 'TotalDistance': 2.8},
   {'From_Relative': 'Relative_7', 'To_Relative': 'Relative_4', 'TotalDistance': 0.55},
   {'From_Relative': 'Relative_8', 'To_Relative': 'Relative_5', 'TotalDistance': 5.35},
   {'From_Relative': 'Relative_9', 'To_Relative': 'Relative_7', 'TotalDistance': 1.93},
   {'From_Relative': 'Relative_10', 'To_Relative': 'Relative_9', 'TotalDistance': 3.89}
]

transport = transportCalc(relativeDist, modes)

totalTime(transport)
totalCost(transport)"""