from Window import MainWindow
from Truck import TruckBodyType, VehicleAlignmentData

try:
    vehicle_data = VehicleAlignmentData.load_from_file("vehicle_data.json")
except FileNotFoundError:
    vehicle_data = VehicleAlignmentData()

app = MainWindow(vehicle_data)
app.mainloop()

if vehicle_data:
    vehicle_data.save_to_file("vehicle_data.json")