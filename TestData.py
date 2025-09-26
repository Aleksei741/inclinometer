import random
from Truck import TruckBodyType, VehicleAlignmentData

def generate_test_data():
    data = VehicleAlignmentData(TruckBodyType.TRUCK_2_AXLE)

    # --- Информация о компании ---
    data.set_company_name("Test Truck Service")
    data.set_address("г. Москва, ул. Примерная, 1")
    data.set_phone("+7 (495) 123-45-67")

    # --- Информация об автомобиле ---
    data.set_car_brand("КАМАЗ")
    data.set_model("6520")
    data.set_chassis_number("XTC1234567890")
    data.set_mileage(120000)
    data.set_reg_number("А123ВС77")
    data.set_owner("ООО 'Тест-Логистика'")

    # --- Среднее положение руля ---
    data.set_middle_position_steering_wheel("before", 1.2)
    data.set_middle_position_steering_wheel("after", 0.1)

    # --- Заполнение осей ---
    for axle_idx in range(data.body_type.total_axles):
        for side in ["left", "right"]:
            # Давление
            data.set_pressure(axle_idx, side, round(random.uniform(7.5, 8.5), 1))

            # Развал
            data.set_camber(axle_idx, side, "before", round(random.uniform(-1.5, 1.5), 2))
            data.set_camber(axle_idx, side, "after", round(random.uniform(-1.0, 1.0), 2))

            # Схождение
            data.set_toe(axle_idx, side, "before", round(random.uniform(-0.3, 0.3), 2))
            data.set_toe(axle_idx, side, "after", round(random.uniform(-0.2, 0.2), 2))

            # Дополнительные параметры для передней оси (caster, SAI и т.д.)
            if axle_idx == 0:  # только рулевая
                data.set_caster_angle(axle_idx, side, "before", round(random.uniform(2.0, 5.0), 2))
                data.set_caster_angle(axle_idx, side, "after", round(random.uniform(2.5, 5.5), 2))

                data.set_steering_axis_inclination(axle_idx, side, "before", round(random.uniform(8.0, 12.0), 2))
                data.set_steering_axis_inclination(axle_idx, side, "after", round(random.uniform(8.5, 12.5), 2))

        # Общее схождение оси
        data.set_total_toe(axle_idx, "before", round(random.uniform(-0.4, 0.4), 2))
        data.set_total_toe(axle_idx, "after", round(random.uniform(-0.3, 0.3), 2))

    return data