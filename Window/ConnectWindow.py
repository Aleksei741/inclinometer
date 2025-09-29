import asyncio
import threading
import tkinter as tk
from tkinter import messagebox, Listbox, END
from Truck import VehicleAlignmentData, TruckBodyType
from BLE import BLEApp


class ConnectWindow(tk.Toplevel):
    def __init__(self, masterself, vehicle_data: VehicleAlignmentData, ble: BLEApp):
        super().__init__(masterself)
        self.title("Подключение BLE")
        self.geometry("400x300")

        self.vehicle_data = vehicle_data
        self.ble_app = ble
        self.devices = []

        # список устройств
        self.device_list = Listbox(self, height=10, width=50)
        self.device_list.pack(pady=5, fill=tk.BOTH, expand=True)

        # кнопки
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        self.scan_button = tk.Button(btn_frame, text="Сканировать", command=self.on_scan_devices)
        self.scan_button.grid(row=0, column=0, padx=5)

        self.connect_button = tk.Button(btn_frame, text="Подключиться", command=self.on_connect_device)
        self.connect_button.grid(row=0, column=1, padx=5)

    def on_scan_devices(self):
        """Сканирование через BLEApp в отдельном потоке"""
        def run():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                devices = loop.run_until_complete(self.ble_app.scan_devices())
                self.devices = devices
                self.device_list.delete(0, END)
                for i, d in enumerate(devices):
                    name = d.name or "Неизвестное устройство"
                    self.device_list.insert(END, f"{i+1}. {name} [{d.address}]")
            except Exception as e:
                messagebox.showerror("Ошибка сканирования", str(e))
            finally:
                loop.close()

        threading.Thread(target=run, daemon=True).start()

    def on_connect_device(self):
        """Подключение через BLEApp в отдельном потоке"""
        index = self.device_list.curselection()
        if not index:
            messagebox.showwarning("Выбор устройства", "Сначала выберите устройство")
            return

        device = self.devices[index[0]]

        def run():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(self.ble_app.connect(device))
                messagebox.showinfo("Успех", f"Подключено к {device.name} [{device.address}]")
                self.destroy()  # закрываем окно после успешного подключения
            except Exception as e:
                messagebox.showerror("Ошибка подключения", str(e))
            finally:
                loop.close()

        threading.Thread(target=run, daemon=True).start()