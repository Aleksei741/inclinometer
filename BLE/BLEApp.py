import asyncio
import threading
from bleak import BleakScanner, BleakClient
from Truck import VehicleAlignmentData, TruckBodyType

class BLEApp:
    def __init__(self):
        self.client = None
        self.device = None

        # Создаём отдельный цикл событий для этого BLEApp
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self._start_loop, daemon=True)
        self.thread.start()

    def _start_loop(self):
        """Запуск цикла событий в отдельном потоке"""
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def run_async(self, coro):
        """
        Запуск асинхронной задачи
        Возвращает concurrent.futures.Future
        """
        return asyncio.run_coroutine_threadsafe(coro, self.loop)

    async def scan_devices(self):
        """Сканирование BLE устройств"""
        devices = await BleakScanner.discover()
        return devices

    async def connect(self, device):
        """Подключение к выбранному устройству"""
        if self.client and self.client.is_connected:
            await self.client.disconnect()
            self.client = None
            self.device = None

        self.client = BleakClient(device)
        await self.client.connect()
        if not self.client.is_connected:
            raise ConnectionError("Не удалось подключиться")
        self.device = device

    async def read_data(self, vehicle_data: VehicleAlignmentData):
        """Чтение данных"""
        # UID = "00002a19-0000-1000-8000-00805f9b34fb"
        # if not self.client or not self.client.is_connected:
        #    raise ConnectionError("Нет активного подключения")
        # data = await self.client.read_gatt_char(UID)
        
        # Сначала обновляем тип кузова
        vehicle_data.set_body_type(TruckBodyType.BUS_2_AXLE)
        
        # Затем заносим данные
        # Ось 1
        # Развал
        vehicle_data.set_camber(0, "left", "before", 15)
        vehicle_data.set_camber(0, "left", "after", 16)
        vehicle_data.set_camber(0, "right", "before", 10)
        vehicle_data.set_camber(0, "right", "after", 11)

        # Продольный шкворень
        vehicle_data.set_caster_angle(0, "left", "before", 17) 
        vehicle_data.set_caster_angle(0, "left", "after", 18)
        vehicle_data.set_caster_angle(0, "right", "before", 12) 
        vehicle_data.set_caster_angle(0, "right", "after", 13)

        # Поперечный шкворень
        vehicle_data.set_steering_axis_inclination(0, "left", "before", 19)
        vehicle_data.set_steering_axis_inclination(0, "left", "after", 20)
        vehicle_data.set_steering_axis_inclination(0, "right", "before", 14)
        vehicle_data.set_steering_axis_inclination(0, "right", "after", 15)

        # ось 2
        # Развал
        vehicle_data.set_camber(1, "both", "before", 5)
        vehicle_data.set_camber(1, "both", "after", 1)

    def is_connected(self):
        return self.client is not None and self.client.is_connected