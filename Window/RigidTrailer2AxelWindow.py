import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class RigidTrailer2AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=10, padx=10)

        self.total_toe = tk.Label(main_frame, text="Общее схождение:", font=("Arial", 12, "bold"))
        self.total_toe.grid(row=0, column=1, pady=0)

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/RIGID_TRAILER_2_AXLE.png")
        self.bg_label = tk.Label(main_frame, image=self.img)
        self.bg_label.grid(row=1, column=1, rowspan=5, columnspan=1)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.table_l3 = self.creatTableFixedWheelParams(main_frame, 0, "left")
        self.table_l3.grid(row=2, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.table_r3 = self.creatTableFixedWheelParams(main_frame, 0, "right")
        self.table_r3.grid(row=2, column=2, padx=5)

        # ----------- Таблицы параметров левого фиксированного колеса 2 ----------
        self.table_l3 = self.creatTableFixedWheelParams(main_frame, 1, "left")
        self.table_l3.grid(row=5, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 2 ----------
        self.table_r3 = self.creatTableFixedWheelParams(main_frame, 1, "right")
        self.table_r3.grid(row=5, column=2, padx=5)

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Задняя ось 1
        self.creatTableTotalToe(main_frame, 0).grid(row=2, column=1, padx=1)
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 1).grid(row=5, column=1, padx=1)