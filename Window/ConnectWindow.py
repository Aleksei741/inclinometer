import threading
import tkinter as tk
from tkinter import Listbox, messagebox
from BLE import BLEApp  # твой новый класс BLEApp

class ConnectWindow(tk.Toplevel):
    def __init__(self, master, ble: BLEApp):
        super().__init__(master)
        self.title("Подключение BLE")
        self.geometry("400x300")

        self.ble_app = ble
        self.devices = []

        # Список устройств
        self.device_list = Listbox(self, height=10, width=50)
        self.device_list.pack(pady=5, fill=tk.BOTH, expand=True)

        # Кнопки
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        self.scan_button = tk.Button(btn_frame, text="Сканировать", command=self.on_scan_devices)
        self.scan_button.grid(row=0, column=0, padx=5)
        self.connect_button = tk.Button(btn_frame, text="Подключиться", command=self.on_connect_device)
        self.connect_button.grid(row=0, column=1, padx=5)

    def on_scan_devices(self):
        """Сканирование через BLEApp"""
        self.scan_button.config(state=tk.DISABLED)
        self.connect_button.config(state=tk.DISABLED)

        def run():
            future = self.ble_app.run_async(self.ble_app.scan_devices())
            try:
                devices = future.result()  # ждём завершения
                self.devices = devices
                self.device_list.delete(0, tk.END)
                for i, d in enumerate(devices):
                    name = d.name or "Неизвестное устройство"
                    self.device_list.insert(tk.END, f"{i+1}. {name} [{d.address}]")
            except Exception as e:
                messagebox.showerror("Ошибка сканирования", str(e))
            finally:
                self.scan_button.config(state=tk.NORMAL)
                self.connect_button.config(state=tk.NORMAL)

        threading.Thread(target=run, daemon=True).start()

    def on_connect_device(self):
        """Подключение через BLEApp"""
        index = self.device_list.curselection()
        if not index:
            messagebox.showwarning("Выбор устройства", "Сначала выберите устройство")
            return

        device = self.devices[index[0]]

        # блокируем кнопки сразу
        self.scan_button.config(state=tk.DISABLED)
        self.connect_button.config(state=tk.DISABLED)

        def run():
            future = self.ble_app.run_async(self.ble_app.connect(device))
            try:
                future.result()  # ждём завершения подключения
                messagebox.showinfo("Успех", f"Подключено к {device.name} [{device.address}]")
                self.destroy()  # закрываем окно после успешного подключения
            except Exception as e:
                messagebox.showerror("Ошибка подключения", str(e))
            finally:
                # разблокируем кнопки если окно не закрылось
                try:
                    self.scan_button.config(state=tk.NORMAL)
                    self.connect_button.config(state=tk.NORMAL)
                except tk.TclError:
                    # окно уже уничтожено
                    pass

        threading.Thread(target=run, daemon=True).start()