import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class Trailer3AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=0, padx=10)

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/TRAILER_3_AXLE.png")
        tk.Label(main_frame, image=self.img).grid(row=0, column=1, rowspan=5, columnspan=1)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "left").grid(row=1, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 0, "right").grid(row=1, column=2, padx=5)

        # ----------- Таблицы параметров левого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "left").grid(row=2, column=0, padx=5, pady=(15, 0), sticky="n") 
        
        # ----------- Таблицы параметров правого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "right").grid(row=2, column=2, padx=5, pady=(15, 0), sticky="n")

        # ----------- Таблицы параметров левого фиксированного колеса 3 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "left").grid(row=3, column=0, padx=5, pady=(0, 0), sticky="n") 
        
        # ----------- Таблицы параметров правого фиксированного колеса 3 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "right").grid(row=3, column=2, padx=5, pady=(0, 0), sticky="n")

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Задняя ось 1
        self.creatTableTotalToe(main_frame, 0).grid(row=1, column=1, padx=1)
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 1).grid(row=2, column=1, padx=1, pady=(20, 0), sticky="n")
        # Задняя ось 3
        self.creatTableTotalToe(main_frame, 2).grid(row=3, column=1, padx=1, pady=(5, 0), sticky="n")

        main_frame.grid_rowconfigure(0, weight=1, minsize=180)
        main_frame.grid_rowconfigure(1, weight=1, minsize=120)
        main_frame.grid_rowconfigure(2, weight=1, minsize=120)
        main_frame.grid_rowconfigure(3, weight=1, minsize=120)