import tkinter as tk
from Window.CarFrame import CarFrame
from Truck import VehicleAlignmentData

class Truck3AxelWindow(CarFrame):
    def __init__(self, master, vehicle_data: VehicleAlignmentData):
        super().__init__(master, vehicle_data)

        # ----------- Основной фрейм с 5 колонками -----------
        main_frame = tk.Frame(master)
        main_frame.pack(pady=0, padx=0)

        # ----------- Спинбокс "Среднее положение рулевого колеса" -----------
        tk.Label(main_frame, text="Среднее положение рулевого колеса", font=("Arial", 10, "bold")).grid(row=0, column=1, pady=0)
        self.creatTableMiddlePositionSteeringWheel(main_frame).grid(row=1, column=1, pady=0)

        # ----------- Надпись "Общее схождение" -----------
        tk.Label(main_frame, text="Общее схождение:", font=("Arial", 10, "bold")).grid(row=2, column=1, pady=0)

        # ----------- Картинка шасси -----------
        self.img = tk.PhotoImage(file="img/TRUCK_3_AXLE.png")
        tk.Label(main_frame, image=self.img).grid(row=3, column=1, rowspan=4, columnspan=1)

        # ----------- Таблицы параметров левого подруливающего колеса -----------
        self.creatTableSteerableWheelParams(main_frame, 0, "left").grid(row=3, column=0, padx=5)

        # ----------- Таблицы параметров правого подруливающего колеса -----------
        self.creatTableSteerableWheelParams(main_frame, 0, "right").grid(row=3, column=2, padx=5)

        # ----------- Таблицы параметров левого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "left", axle_twist=False).grid(row=5, column=0, padx=5) 
        
        # ----------- Таблицы параметров правого фиксированного колеса 1 ----------
        self.creatTableFixedWheelParams(main_frame, 1, "right", axel_shift=False).grid(row=5, column=2, padx=5)

         # ----------- Таблицы параметров левого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 2, "left", axle_twist=False).grid(row=6, column=0, padx=5)         

        # ----------- Таблицы параметров правого фиксированного колеса 2 ----------
        self.creatTableFixedWheelParams(main_frame, 2, "right", axel_shift=False).grid(row=6, column=2, padx=5)

        # ----------- Спинбоксы "Общее схождение" поверх картинки -----------
        # Передня ось
        self.creatTableTotalToe(main_frame, 0).grid(row=3, column=1, padx=1)
        # Задняя ось 1
        self.creatTableTotalToe(main_frame, 1).grid(row=5, column=1, padx=1)
        # Задняя ось 2
        self.creatTableTotalToe(main_frame, 2).grid(row=6, column=1, padx=1)