from Window import MainWindow
from Truck import TruckBodyType, VehicleAlignmentData
from TestData import generate_test_data

try:
    vehicle_data = VehicleAlignmentData.load_from_file("vehicle_data.json")
except FileNotFoundError:
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRUCK_2_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRUCK_3_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRUCK_4_AXLE_TWIN_STEER)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.BUS_2_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.BUS_3_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRAILER_1_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRAILER_2_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.TRAILER_3_AXLE)
    vehicle_data = VehicleAlignmentData(TruckBodyType.RIGID_TRAILER_2_AXLE)
    # vehicle_data = VehicleAlignmentData(TruckBodyType.MINIBUS)
    pass

# vehicle_data = generate_test_data()

app = MainWindow(vehicle_data)
app.mainloop()

vehicle_data.save_to_file("vehicle_data.json")

