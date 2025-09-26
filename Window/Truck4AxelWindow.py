import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class Truck4AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=0, padx=0)

        self.total_toe = tk.Label(main_frame, text="Общее схождение:", font=("Arial", 12, "bold"), padx=0, pady=0)
        self.total_toe.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/TRUCK_4_AXLE_TWIN_STEER.png")
        self.bg_label = tk.Label(main_frame, image=self.img)
        self.bg_label.grid(row=1, column=1, rowspan=4)

        # ----------- Таблицы параметров левого подруливающего колеса 1 ----------
        self.creatTableSteerableWheelParams(main_frame, 0, "left").grid(row=1, column=0, padx=10, pady=1)

        # ----------- Таблицы параметров правого подруливающего колеса 1 ---------
        self.creatTableSteerableWheelParams(main_frame, 0, "right").grid(row=1, column=2, padx=10, pady=1)

        # ----------- Таблицы параметров левого подруливающего колеса 2 ----------
        self.creatTableSteerableWheelParams(main_frame, 1, "left").grid(row=2, column=0, padx=10, pady=1)

        # ----------- Таблицы параметров правого подруливающего колеса 2 ---------
        self.creatTableSteerableWheelParams(main_frame, 1, "right").grid(row=2, column=2, padx=10, pady=1)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 2, "left", axle_twist=False).grid(row=3, column=0, padx=10, pady=1) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 2, "right", axel_shift=False).grid(row=3, column=2, padx=10, pady=1)

         # ----------- Таблицы параметров левого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 3, "left", axle_twist=False).grid(row=4, column=0, padx=10, pady=1) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 3, "right", axel_shift=False).grid(row=4, column=2, padx=10, pady=1)

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Передня ось 1
        self.creatTableTotalToe(main_frame, 0).grid(row=1, column=1, padx=1, pady=0)
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 1).grid(row=2, column=1, padx=1, pady=0, sticky="n")
        # Задняя ось 1
        self.creatTableTotalToe(main_frame, 2).grid(row=3, column=1, padx=1, pady=0, sticky="n")
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 3).grid(row=4, column=1, padx=1, pady=0, sticky="n")

        