import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class Trailer1AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=10, padx=10)

        # ----------- Заголовок -----------
        tk.Label(main_frame, text="Общее схождение оси:", font=("Arial", 12, "bold")).grid(row=0, column=1, pady=0)

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/TRAILER_1_AXLE.png")
        tk.Label(main_frame, image=self.img).grid(row=1, column=1, rowspan=4, columnspan=1)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "left").grid(row=4, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "right").grid(row=4, column=2, padx=5)

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Передня ось 1
        self.creatTableTotalToe(main_frame, 0).grid(row=4, column=1, padx=1)