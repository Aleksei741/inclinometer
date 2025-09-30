import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class Trailer2AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=0, padx=0)

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/TRAILER_2_AXLE.png")
        tk.Label(main_frame, image=self.img).grid(row=1, column=1, rowspan=7, columnspan=1)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "left").grid(row=6, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "right").grid(row=6, column=2, padx=5)

        # ----------- Таблицы параметров левого фиксированного колеса 2 ----------
        self.table_l3 = self.creatTableFixedWheelParams(main_frame, 1, "left").grid(row=7, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 2 ----------
        self.table_r3 = self.creatTableFixedWheelParams(main_frame, 1, "right").grid(row=7, column=2, padx=5)

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Задняя ось 1
        self.creatTableTotalToe(main_frame, 0).grid(row=6, column=1, padx=1)
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 1).grid(row=7, column=1, padx=1)