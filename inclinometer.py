from Window import MainWindow
from Truck import TruckBodyType, VehicleAlignmentData
import json

# Сохранить
def save_vehicle_data(obj: VehicleAlignmentData, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj.to_dict(), f, ensure_ascii=False, indent=4)


# Загрузить
def load_vehicle_data(filename: str) -> VehicleAlignmentData:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return VehicleAlignmentData.from_dict(data)


try:
    vehicle_data = load_vehicle_data("vehicle_data.json")
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

app = MainWindow(vehicle_data)

app.on_truck_body_change(vehicle_data.body_type)

app.mainloop()

save_vehicle_data(vehicle_data, "vehicle_data.json")

