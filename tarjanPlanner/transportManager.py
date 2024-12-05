#TransportManager.py
import json
from logger import log_function_call
class transportManager:
    def __init__(self, file_name="transportmodes.json"):
        self.file_name = file_name
        #Creates a dictonary with transport modes
        self.modes = [ 
            {"transport": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
            {"transport": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2},
            {"transport": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
            {"transport": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
        ]
        self.save_transport()

    #Saves the transport.json file    
    def save_transport(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.modes, file, indent=4)

    #Lists all the transports
    def listTransport(self):
        for transport in self.modes:
            print(f"transport: {transport['transport']}, speed_kmh: {transport['speed_kmh']}, cost_per_km: {transport['cost_per_km']}, transfer_time_min: {transport['transfer_time_min']}")

    @log_function_call
    #Add transport modes
    def addmode(self, transport, speed_kmh, cost_per_km, transfer_time_min):
        mode = {'transport': transport,
            'speed_kmh': speed_kmh, 
            'cost_per_km': cost_per_km,       
            'transfer_time_min': transfer_time_min 
        }
        self.modes.append(mode)

    @log_function_call
    #removes transport mode if needed
    def remove_mode(self, mode):
        if not self.modes:
            raise ValueError("No modes to remove")
        
        initial_length = len(self.modes)
        #Checks if the mode exists in the dictonary
        self.modes = [c for c in self.modes if c['transport'] != mode]
        if len(self.modes) == initial_length:
            raise ValueError(f"{mode}, not found")   
    
    #Returns the modes
    def get_modes(self):
        return self.modes
