from enum import Enum, unique


@unique
class TruckBodyType(Enum):
    """Типы кузовов и прицепов грузовиков/автобусов с числом осей и подруливающих/фиксированных осей."""

    # ------------------- Грузовики -------------------
    TRUCK_2_AXLE = (2, 1, 1, "truck")             # 2 оси, 1 подруливающая, 1 фиксированная
    TRUCK_3_AXLE = (3, 1, 2, "truck")             # 3 оси, 1 подруливающая, 2 фиксированные
    TRUCK_4_AXLE_TWIN_STEER = (4, 2, 2, "truck")  # 4 оси, 2 подруливающие, 2 фиксированные

    # ------------------- Автобусы -------------------
    BUS_2_AXLE = (2, 1, 1, "bus")                 # 2 оси, 1 подруливающая, 1 фиксированная
    BUS_3_AXLE = (3, 1, 2, "bus")                 # 3 оси, 1 подруливающая, 2 фиксированные

    # ------------------- Прицепы -------------------
    TRAILER_1_AXLE = (1, 0, 1, "trailer")         # 1 ось, 0 подруливающих, 1 фиксированная
    TRAILER_2_AXLE = (2, 0, 2, "trailer")         # 2 оси, 0 подруливающих, 2 фиксированные
    TRAILER_3_AXLE = (3, 0, 3, "trailer")         # 3 оси, 0 подруливающих, 3 фиксированные
    RIGID_TRAILER_2_AXLE = (2, 0, 2, "rigid")     # 2 оси, 0 подруливающих, 2 фиксированные (жёсткий прицеп)

    # ------------------- Микроавтобус -------------------
    MINIBUS = (2, 1, 1, "minibus")                # 2 оси, 1 подруливающая, 1 фиксированная

    def __init__(self, total_axles, steerable, fixed, kind: str):
        self._total_axles = total_axles
        self._steerable_axles = steerable
        self._fixed_axles = fixed
        self._kind = kind

    @property
    def total_axles(self):
        return self._total_axles

    @property
    def steerable_axles(self):
        return self._steerable_axles

    @property
    def fixed_axles(self):
        return self._fixed_axles

    @property
    def kind(self):
        return self._kind

    def to_dict(self):
        return {
            "name": self.name,
            "total_axles": self.total_axles,
            "steerable_axles": self.steerable_axles,
            "fixed_axles": self.fixed_axles,
            "kind": self.kind,
        }

    @staticmethod
    def from_name(name: str):
        return TruckBodyType[name]

    def __repr__(self):
        return (f"<TruckBodyType {self.name}: total={self.total_axles}, "
                f"steerable={self.steerable_axles}, fixed={self.fixed_axles}, kind={self.kind}>")
