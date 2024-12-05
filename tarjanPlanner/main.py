#main.py

from relatives import reliativesManager
from transportManager import transportManager
from calculateDistance import calculateDistance, shortestDist
from transportationCalculation import transportCalc, totalCost, totalTime
from tabulate import tabulate
import time

#Calculate the shortest parh
def shortest_path():
    reliatives_manager = reliativesManager()
        
    relatives = reliatives_manager.get_relatives()

    print('These are your existing places')
    
    reliatives_manager.listRelatives()
    
    #All the input for adding a relative and a place
    check = input('Do you want to add places? (Yes or No) ')
    
    if check == "yes" or check == "Yes":
        inpAmount = input('How many places do you want to add? ')
        for x in range(int(inpAmount)):
            inpStreetName = input(f'What is the street name of new place {x+1}? ')
            inpDistrict = input(f'What is the district of new place {x+1}? ')
            inpLatitude = input(f'What is the latitude of the place {x+1}? ')
            inpLongitude = input(f'What is the longitude of the place {x+1}? ')

            reliatives_manager.addRelatives(inpStreetName, inpDistrict, inpLatitude, inpLongitude)

        print("This is your places now: ")
        reliatives_manager.listRelatives()
    
    
    calcDist = calculateDistance(relatives)
    
    sDist = shortestDist(calcDist)


    return sDist

#Calculating the best transports
def transport(sDist):
    transport_manager = transportManager()
    
    print("This is your current possible transports")
    transport_manager.listTransport()

    #All the input for adding a new transport
    moreTransport = input('Do you want to add more transports? (Yes or No) ')
    
    if moreTransport == "yes" or moreTransport == "Yes":
        inpAmount = input('How many transports do you want to add? ')
        for x in range(int(inpAmount)):
            inpTransport = input(f'What is the name of new transport {x+1}? ')
            inpSpeed_kmh = input(f'What is the speed of new transport {x+1} in kmh? ')
            inpCost = input(f'How much is the cost per km of new transport {x+1}? ')
            inpTransfer = input(f'How many minutes are the transfers of new transport {x+1}? ')

            transport_manager.addmode(inpTransport, int(inpSpeed_kmh), int(inpCost), int(inpTransfer))

        print("This is your transports now: ")
        transport_manager.listTransport()
    
    modes = transport_manager.get_modes()
    
    #Input for including and excluding of transports
    inpRoute = input("Do you want to include or exclude any transport modes? ")

    if inpRoute == "exclude" or inpRoute == "Exclude":
        excludeMode = input("What transport modes you want to exclude from the route(seperate with commas)? ").split(",")
        for exclMode in excludeMode:
            for mode in modes:
                if mode["transport"] == exclMode:
                    transport_manager.remove_mode(mode['transport'])
    
    elif inpRoute == "include" or inpRoute == "Include":
        includeMode = input("What transport modes you want to include in the route(seperate with commas)? ").split(",")
        for mode in modes:
            print(includeMode, mode["transport"])
            if mode["transport"] not in includeMode:
                transport_manager.remove_mode(mode['transport'])
    
   
    transport_manager.listTransport()
    rel_dist = []
    modes = transport_manager.get_modes()
    
    for dist in sDist['route_details']:
        rel_dist.append(dist['Distance'])
       
    

    best_transport = transportCalc(rel_dist, modes)

    combined = []
    for path, detail in zip(sDist['route_details'], best_transport):
        combined_entry = {
            'From_Relative': path['From_Relative'],
            'To_Relative': path['To_Relative'],
            'Distance_km': path['Distance'],
            'Mode': detail['Mode'],
            'Time': detail['Total_Time'],
            'Cost': detail['Total_Cost']
        }
        combined.append(combined_entry)

    return combined



def main():

    try:
        # Starting execution timer
        start_time = time.time()
        
        # Calculating the shortest path
        short_path = shortest_path()
        final = transport(short_path)

        # Constructing the table for the most efficient route
        table_data = [[data['From_Relative'], data['To_Relative'], data['Distance_km'], data['Mode']] for data in final]
        header = ["From Relative", "To Relative", "Distance (KM)", "Transport Mode"]

        print("This is your most effective route")
        print(tabulate(table_data, headers=header, tablefmt="grid"))

        # Calculating total distance, time, and cost
        tot_distance = []
        times = []
        costs = []
        for stats in final:
            times.append(stats['Time'])
            costs.append(stats['Cost'])
            tot_distance.append(stats['Distance_km'])

        print("Total distance:", round(sum(tot_distance), 2))
        totalTime(times)
        totalCost(costs)

        # Stopping execution timer
        end_time = time.time()

        # Calculating execution time
        execution_time = end_time - start_time
        print(f"Program Execution Time: {execution_time:.2f} seconds")

        # Log the execution time to a file
        try:
            with open("logger.txt", "a") as log_file:
                log_file.write(f"Program Execution Time: {execution_time:.2f} seconds\n")
        except IOError as e:
            print(f"Failed to write execution time to log file: {e}")

    except ValueError as e:
        print(f"Value error occurred: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':    
    main()