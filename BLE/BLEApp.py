import asyncio
import tkinter as tk
from bleak import BleakScanner, BleakClient
from Truck import VehicleAlignmentData, TruckBodyType
from TestData import generate_test_data

class BLEApp:
    def __init__(self):
        self.client = None
        self.device = None

    async def scan_devices(self):
        """Сканирование BLE устройств"""
        devices = await BleakScanner.discover()
        return devices

    async def connect(self, device):
        """Подключение к выбранному устройству"""
        # если уже есть подключение — разрываем
        if self.client and self.client.is_connected:
            await self.client.disconnect()
            self.client = None
            self.device = None
            return "disconnected"
        
        # Подключаемся
        self.client = BleakClient(device)
        await self.client.connect()
        if not self.client.is_connected:
            raise ConnectionError("Не удалось подключиться")
        self.device = device

    async def read_data(self):
        """Чтение данных"""
        UID = "00002a19-0000-1000-8000-00805f9b34fb"
        # if not self.client or not self.client.is_connected:
        #    raise ConnectionError("Нет активного подключения")
        # data = await self.client.read_gatt_char(UID)

        # test
        return generate_test_data()


    def is_connected(self):
        return self.client is not None and self.client.is_connected