from threading import RLock
from typing import List
from Truck.TruckTypes import TruckBodyType
import os
import json

class Wheel():
    """Колесо"""
    def __init__(self):
        self.presure = 2.2  # Давление в шине

class SteerableWheel(Wheel):
    """Колесо с поворотным механизмом."""
    def __init__(self):
        super().__init__()
        self.camber_before = None  # Развал до
        self.camber_after = None   # Развал после
        self.toe_before = None  # Схождение до
        self.toe_after = None   # Схождение после
        self.caster_angle_before = None  # Угол продольного наклона шворня до
        self.caster_angle_after = None   # Угол продольного наклона шворня после
        self.steering_axis_inclination_before = None  # Угол поперечного наклона шкворня до
        self.steering_axis_inclination_after = None   # Угол поперечного наклона шкворня после
        self.turning_angle_difference_before = None  # Разница углов поворота до
        self.turning_angle_difference_after = None   # Разница углов поворота после

class FixedWheel(Wheel):
    """Колесо без поворотного механизма."""
    def __init__(self):
        super().__init__()
        self.camber_before = None       # Развал до
        self.camber_after = None        # Развал после
        self.axel_shift_before = None   # Смещение оси до
        self.axel_shift_after = None    # Смещение оси после
        self.axle_twist_before = None   # Перекос оси до
        self.axle_twist_after = None    # Перекос оси после

class Axle:
    def __init__(self):
        self.total_toe_before = None    # Общее схождение до
        self.total_toe_after = None     # Общее схождение после

class SteerableAxle(Axle):
    """Поворотная ось (с подруливающим механизмом)."""
    def __init__(self):
        super().__init__()
        self.left_wheel = SteerableWheel()
        self.right_wheel = SteerableWheel()

class FixedAxle(Axle):
    """Неповоротная ось."""
    def __init__(self):
        super().__init__()
        self.left_wheel = FixedWheel()
        self.right_wheel = FixedWheel()


class VehicleAlignmentData:
    """Основной класс для хранения данных о развале/схождении."""
    def __init__(self, body_type: TruckBodyType = None):
        self._lock = RLock()
        
        self._steerable_axles: List[SteerableAxle] = []
        self._fixed_axles: List[FixedAxle] = []
        self.clear_data()

        if body_type:
            self.set_body_type(body_type)

    # Очистка данных
    def clear_data(self):
        with self._lock:
            # Поля информации о компании
            self._company_name = None   # Наимение компании
            self._address = None        # Адрес компании
            self._phone = None          # Телефон компании

            # Поля информации о транспортном средстве
            self._car_brand = None      # Марка автомобиля
            self._model = None          # Модель автомобиля
            self._chassis_number = None # номер шасси
            self._mileage = None        # пробег
            self._reg_number = None     # регистрационный номер
            self._owner = None          # владелец

            # Среднее положение рулевого колеса
            self._middle_position_steering_wheel_before = None  # Среднее положение рулевого колеса до
            self._middle_position_steering_wheel_after = None   # Среднее положение рулевого колеса после

            # Оси
            self._steerable_axles.clear()  # Поворотные оси
            self._fixed_axles.clear()      # Неповоротные оси

    # Поля информации о компании -----------------------------------------------
    def get_company_name(self):     # Наименование компании
        with self._lock:
            print(f"Чтение названия компании: {self._company_name}")
            return self._company_name

    def set_company_name(self, value: str):
        with self._lock:
            print(f"Устанавливаем название компании: {value}")
            self._company_name = value

    def get_address(self):          # Адрес компании
        with self._lock:
            print(f"Чтение адреса компании: {self._address}")
            return self._address

    def set_address(self, value: str):
        with self._lock:
            print(f"Устанавливаем адрес компании: {value}")
            self._address = value

    def get_phone(self):            # Телефон компании
        with self._lock:
            print(f"Чтение телефона компании: {self._phone}")
            return self._phone

    def set_phone(self, value: str):
        with self._lock:
            print(f"Устанавливаем телефон компании: {value}")
            self._phone = value

    # Поля информации о транспортном средстве ----------------------------------
    def get_car_brand(self):        # Марка автомобиля
        with self._lock:
            print(f"Чтение марки автомобиля: {self._car_brand}")
            return self._car_brand
        
    def set_car_brand(self, value: str):
        with self._lock:
            print(f"Устанавливаем марку автомобиля: {value}")
            self._car_brand = value

    def get_model(self):            # Модель автомобиля
        with self._lock:
            print(f"Чтение модели автомобиля: {self._model}")
            return self._model
        
    def set_model(self, value: str):
        with self._lock:
            print(f"Устанавливаем модель автомобиля: {value}")
            self._model = value

    def get_chassis_number(self):   # Номер шасси
        with self._lock:
            print(f"Чтение номера шасси: {self._chassis_number}")
            return self._chassis_number
        
    def set_chassis_number(self, value: str):
        with self._lock:
            print(f"Устанавливаем номер шасси: {value}")
            self._chassis_number = value

    def get_mileage(self):          # Пробег
        with self._lock:
            print(f"Чтение пробега: {self._mileage}")
            return self._mileage

    def set_mileage(self, value):
        with self._lock:
            print(f"Устанавливаем пробег: {value}")
            self._mileage = value

    def get_reg_number(self):       # Регистрационный номер
        with self._lock:
            print(f"Чтение регистрационного номера: {self._reg_number}")
            return self._reg_number
        
    def set_reg_number(self, value: str):
        with self._lock:
            print(f"Устанавливаем регистрационный номер: {value}")
            self._reg_number = value

    def get_owner(self):            # Владелец
        with self._lock:
            print(f"Чтение владельца: {self._owner}")
            return self._owner
        
    def set_owner(self, value: str):
        with self._lock:
            print(f"Устанавливаем владельца: {value}")
            self._owner = value

    # Установка количества осей ----------------------------------------------- 
    def set_body_type(self, body_type: TruckBodyType):
        """Устанавливает кузов и инициализирует оси по типу кузова."""
        with self._lock:
            if not isinstance(body_type, TruckBodyType):
                raise ValueError("body_type должен быть экземпляром TruckBodyType")
            
            self._truck_body_type = body_type

            print(f"Устанавливаем тип кузова: {body_type.name}, "
                f"всего осей={body_type.total_axles}, "
                f"подруливающих={body_type.steerable_axles}, "
                f"фиксированных={body_type.fixed_axles}")

            # Очистка осей
            self._steerable_axles.clear()
            self._fixed_axles.clear()

            # Создаем подруливающие оси
            for i in range(body_type.steerable_axles):
                self._steerable_axles.append(SteerableAxle())
                print(f"Создана подруливающая ось #{i+1}")

            # Создаем фиксированные оси
            for i in range(body_type.fixed_axles):
                self._fixed_axles.append(FixedAxle())
                print(f"Создана фиксированная ось #{i+1}")

    @property
    def body_type(self):
        return self._truck_body_type
    
    # ---------- Давление ----------
    def set_pressure(self, axle_index: int, side: str, value: float):
        with self._lock:
            axle, axle_type = self._get_axle(axle_index)
            wheel = self._get_wheel(axle, side)
            wheel.presure = value
            print(f"Установлено давление {value:.1f} бар в {side} шину {axle_type} оси #{axle_index+1}")

    def get_pressure(self, axle_index: int, side: str) -> float:
        with self._lock:
            axle, axle_type = self._get_axle(axle_index)
            wheel = self._get_wheel(axle, side)
            value = wheel.presure
            print(f"Чтение давления {value:.1f} бар в {side} шине {axle_type} оси #{axle_index+1}")
            return value
    
    # ---------- Вспомогательные функции ----------
    def _get_axle(self, axle_index: int):
        total_axles = len(self._steerable_axles) + len(self._fixed_axles)
        if axle_index < 0 or axle_index >= total_axles:
            print(f"Некорректный индекс оси: {axle_index}, всего осей: {total_axles}")
            return None, None

        if axle_index < len(self._steerable_axles):
            return self._steerable_axles[axle_index], "подруливающая"
        else:
            idx = axle_index - len(self._steerable_axles)
            return self._fixed_axles[idx], "фиксированная"

    def _get_wheel(self, axle, side: str):
        if side == "left":
            return axle.left_wheel
        elif side == "right":
            return axle.right_wheel
        else:
            raise ValueError("Сторона должна быть 'left' или 'right'")

    # ---------- Универсальный setter ----------
    def _set_wheel_param(self, axle_index: int, side: str, stage: str, param: str, value):
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            axle, axle_type = self._get_axle(axle_index)

            if side == "both":
                wheels = [axle.left_wheel, axle.right_wheel]
                sides = ["left", "right"]
            else:
                wheels = [self._get_wheel(axle, side)]
                sides = [side]

            for w, s in zip(wheels, sides):
                attr_name = f"{param}_{stage}" if hasattr(w, f"{param}_{stage}") else param
                setattr(w, attr_name, value)
                print(f"Установлено {attr_name}={value} в {s} шину {axle_type} оси #{axle_index+1}")

    # ---------- Универсальный getter ----------
    def _get_wheel_param(self, axle_index: int, side: str, stage: str, param: str):
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            axle, axle_type = self._get_axle(axle_index)
            wheel = self._get_wheel(axle, side)
            attr_name = f"{param}_{stage}" if hasattr(wheel, f"{param}_{stage}") else param
            value = getattr(wheel, attr_name)
            print(f"Чтение {attr_name}={value} в {side} шине {axle_type} оси #{axle_index+1}")
            return value

    # ---------- Развал (camber) ----------
    def set_camber(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "camber", value)

    def get_camber(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "camber")

    # ---------- Схождение (toe) ----------
    def set_toe(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "toe", value)

    def get_toe(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "toe")

    # ---------- Продольный наклон шкворня (caster_angle) ----------
    def set_caster_angle(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "caster_angle", value)

    def get_caster_angle(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "caster_angle")

    # ---------- Поперечный наклон шкворня (steering_axis_inclination) ----------
    def set_steering_axis_inclination(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "steering_axis_inclination", value)

    def get_steering_axis_inclination(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "steering_axis_inclination")

    # ---------- Разница углов поворота (turning_angle_difference) ----------
    def set_turning_angle_difference(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "turning_angle_difference", value)

    def get_turning_angle_difference(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "turning_angle_difference")

    # ---------- Смещение оси (axel_shift) для фиксированных колес ----------
    def set_axel_shift(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "axel_shift", value)

    def get_axel_shift(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "axel_shift")
    
    # ---------- Перекос оси (axle_twist) для фиксированных колес ----------
    def set_axle_twist(self, axle_index: int, side: str, stage: str, value: float):
        self._set_wheel_param(axle_index, side, stage, "axle_twist", value)

    def get_axle_twist(self, axle_index: int, side: str, stage: str) -> float:
        return self._get_wheel_param(axle_index, side, stage, "axle_twist")
    # ---------- Общее схождение (total_toe) для оси ----------
    def set_total_toe(self, axle_index: int, stage: str, value: float):
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            axle, axle_type = self._get_axle(axle_index)
            attr_name = f"total_toe_{stage}"
            setattr(axle, attr_name, value)
            print(f"Установлено {attr_name}={value} в {axle_type} оси #{axle_index+1}")

    def get_total_toe(self, axle_index: int, stage: str) -> float:
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            axle, axle_type = self._get_axle(axle_index)
            attr_name = f"total_toe_{stage}"
            value = getattr(axle, attr_name)
            print(f"Чтение {attr_name}={value} в {axle_type} оси #{axle_index+1}")
            return value
        
    # ---------- Среднее положение рулевого колеса ----------
    def set_middle_position_steering_wheel(self, stage: str, value: float):
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            attr_name = f"_middle_position_steering_wheel_{stage}"
            setattr(self, attr_name, value)
            print(f"Установлено {attr_name}={value}")
    
    def get_middle_position_steering_wheel(self, stage: str) -> float:
        with self._lock:
            if stage not in ("before", "after"):
                raise ValueError("stage должен быть 'before' или 'after'")
            attr_name = f"_middle_position_steering_wheel_{stage}"
            value = getattr(self, attr_name)
            print(f"Чтение {attr_name}={value}")
            return value


    # ---------- Сериализация в словарь ----------
    def _wheel_to_dict(self, wheel):
        return {k: getattr(wheel, k) for k in wheel.__dict__}

    def _axle_to_dict(self, axle):
        return {
            "left_wheel": self._wheel_to_dict(axle.left_wheel),
            "right_wheel": self._wheel_to_dict(axle.right_wheel),
            "total_toe_before": getattr(axle, "total_toe_before", None),
            "total_toe_after": getattr(axle, "total_toe_after", None)
        }
    
    def to_dict(self):
        with self._lock:
            return {
                "truck_body_type": self._truck_body_type.name if self._truck_body_type else None,
                "company_name": self._company_name,
                "address": self._address,
                "phone": self._phone,
                "car_brand": self._car_brand,
                "model": self._model,
                "chassis_number": self._chassis_number,
                "mileage": self._mileage,
                "reg_number": self._reg_number,
                "owner": self._owner,
                "middle_position_steering_wheel_before": self._middle_position_steering_wheel_before,
                "middle_position_steering_wheel_after": self._middle_position_steering_wheel_after,
                "steerable_axles": [self._axle_to_dict(axle) for axle in self._steerable_axles],
                "fixed_axles": [self._axle_to_dict(axle) for axle in self._fixed_axles]
            }

    @staticmethod
    def from_dict(data: dict):
        """Создает объект VehicleAlignmentData из словаря."""
        truck_body_name = data.get("truck_body_type")
        body_type = None
        if truck_body_name:
            try:
                # если у тебя есть метод from_name, используем его
                body_type = TruckBodyType.from_name(truck_body_name)
            except Exception:
                # fallback: попытаться получить по имени enum
                try:
                    body_type = TruckBodyType[truck_body_name]
                except Exception:
                    body_type = None

        # Создаём пустой объект (без автоматической инициализации осей)
        obj = VehicleAlignmentData()

        # Ставим тип кузова, но НЕ вызываем set_body_type — мы построим оси из JSON
        if body_type is not None:
            obj._truck_body_type = body_type

        # Прямо заполняем простые поля
        obj._company_name = data.get("company_name")
        obj._address = data.get("address")
        obj._phone = data.get("phone")
        obj._car_brand = data.get("car_brand")
        obj._model = data.get("model")
        obj._chassis_number = data.get("chassis_number")
        obj._mileage = data.get("mileage")
        obj._reg_number = data.get("reg_number")
        obj._owner = data.get("owner")

        # Среднее положение рулевого колеса
        obj._middle_position_steering_wheel_before = data.get("middle_position_steering_wheel_before")
        obj._middle_position_steering_wheel_after = data.get("middle_position_steering_wheel_after")

        # ----- Восстанавливаем подруливающие оси (создаём новые объекты) -----
        obj._steerable_axles = []
        for axle_data in data.get("steerable_axles", []):
            axle = SteerableAxle()
            # left wheel
            left_data = axle_data.get("left_wheel", {}) or {}
            for k, v in left_data.items():
                # если значение не None, можно попытаться привести тип для presure
                if k == "presure" and v is not None:
                    try:
                        v = float(v)
                    except Exception:
                        pass
                setattr(axle.left_wheel, k, v)
            # right wheel
            right_data = axle_data.get("right_wheel", {}) or {}
            for k, v in right_data.items():
                if k == "presure" and v is not None:
                    try:
                        v = float(v)
                    except Exception:
                        pass
                setattr(axle.right_wheel, k, v)

            axle.total_toe_before = axle_data.get("total_toe_before")
            axle.total_toe_after = axle_data.get("total_toe_after")
            obj._steerable_axles.append(axle)

        # ----- Восстанавливаем фиксированные оси -----
        obj._fixed_axles = []
        for axle_data in data.get("fixed_axles", []):
            axle = FixedAxle()
            left_data = axle_data.get("left_wheel", {}) or {}
            for k, v in left_data.items():
                if k == "presure" and v is not None:
                    try:
                        v = float(v)
                    except Exception:
                        pass
                setattr(axle.left_wheel, k, v)

            right_data = axle_data.get("right_wheel", {}) or {}
            for k, v in right_data.items():
                if k == "presure" and v is not None:
                    try:
                        v = float(v)
                    except Exception:
                        pass
                setattr(axle.right_wheel, k, v)

            axle.total_toe_before = axle_data.get("total_toe_before")
            axle.total_toe_after = axle_data.get("total_toe_after")
            obj._fixed_axles.append(axle)

        return obj

    # ------------------ Сохранение/чтение JSON ------------------
    def save_to_file(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_file(filename: str):        
        if not os.path.exists(filename):
            raise FileNotFoundError
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return VehicleAlignmentData.from_dict(data)

    
