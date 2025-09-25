import tkinter as tk
from Truck import VehicleAlignmentData

class CarFrame(tk.Frame):
    def __init__(self, master: tk.Tk, vehicle_data: VehicleAlignmentData):
        super().__init__(master)
        self.vehicle_data = vehicle_data
    
    def creatTableSteerableWheelParams(self, parent_frame: tk.Frame, axle_index: int, side: str) -> tk.Frame: 
        operations = ["Развал", "Схождение", "Угол продольного\n наклона шкворня",
                    "Угол поперечного\n наклона шкворня", "Разность углов\n в повороте"]
        headers = ["До", "Операция", "После"]

        table = tk.Frame(parent_frame)
        # Заголовки
        for col, text in enumerate(headers):
            lbl = tk.Label(table, text=text, font=("Arial", 10, "bold"), borderwidth=1, relief="ridge", padx=5, pady=5)
            lbl.grid(row=0, column=col, sticky="nsew")
        
        # Данные
        for row, op in enumerate(operations, start=1):
            if(row == 1):
                val_before = self.vehicle_data.get_camber(axle_index, side, "before")
                val_after = self.vehicle_data.get_camber(axle_index, side, "after")
            elif(row == 2):
                val_before = self.vehicle_data.get_toe(axle_index, side, "before") 
                val_after = self.vehicle_data.get_toe(axle_index, side, "after")
            elif(row == 3): 
                val_before = self.vehicle_data.get_caster_angle(axle_index, side, "before") 
                val_after = self.vehicle_data.get_caster_angle(axle_index, side, "after")
            elif(row == 4):
                val_before = self.vehicle_data.get_steering_axis_inclination(axle_index, side, "before")  
                val_after = self.vehicle_data.get_steering_axis_inclination(axle_index, side, "after")
            elif(row == 5):
                val_before = self.vehicle_data.get_turning_angle_difference(axle_index, side, "before") 
                val_after = self.vehicle_data.get_turning_angle_difference(axle_index, side, "after")
            else:   
                val_before = 0 
                val_after = 0

            val_before = 0 if val_before is None else val_before
            val_after = 0 if val_after is None else val_after

            lbl_before = tk.Label(table, text=f"{val_before}°", borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_before.grid(row=row, column=0, sticky="nsew")

            lbl_op = tk.Label(table, text=op, borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_op.grid(row=row, column=1, sticky="nsew")

            lbl_after = tk.Label(table, text=f"{val_after}°", borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_after.grid(row=row, column=2, sticky="nsew")
        
        # Настройка растяжки
        for i in range(len(operations)+1):
            table.rowconfigure(i, weight=1)

        table.columnconfigure(0, weight=1, uniform="col")
        table.columnconfigure(1, weight=1)
        table.columnconfigure(2, weight=1, uniform="col")
        
        return table
    
    def creatTableFixedWheelParams(self, parent_frame: tk.Frame, axle_index: int, side: str) -> tk.Frame:        
        operations = ["Развал", "Сдвиг оси", "Перекос оси"]
        headers = ["До", "Операция", "После"]

        table = tk.Frame(parent_frame)
        # Заголовки
        for col, text in enumerate(headers):
            lbl = tk.Label(table, text=text, font=("Arial", 10, "bold"), borderwidth=1, relief="ridge", padx=5, pady=5)
            lbl.grid(row=0, column=col, sticky="nsew")

        # Данные
        for row, op in enumerate(operations, start=1):
            if(row == 1):
                val_before = self.vehicle_data.get_camber(axle_index, side, "before")
                val_after = self.vehicle_data.get_camber(axle_index, side, "after")
            elif(row == 2):
                val_before = self.vehicle_data.get_axel_shift(axle_index, side, "before") 
                val_after = self.vehicle_data.get_axel_shift(axle_index, side, "after")
            elif(row == 3): 
                val_before = self.vehicle_data.get_axle_twist(axle_index, side, "before") 
                val_after = self.vehicle_data.get_axle_twist(axle_index, side, "after")
            else:   
                val_before = 0 
                val_after = 0

            val_before = 0 if val_before is None else val_before
            val_after = 0 if val_after is None else val_after

            lbl_before = tk.Label(table, text=f"{val_before}°", borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_before.grid(row=row, column=0, sticky="nsew")

            lbl_op = tk.Label(table, text=op, borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_op.grid(row=row, column=1, sticky="nsew")

            lbl_after = tk.Label(table, text=f"{val_after}°", borderwidth=1, relief="ridge", padx=2, pady=0)
            lbl_after.grid(row=row, column=2, sticky="nsew")

        # Настройка растяжки
        for i in range(len(operations)+1):
            table.rowconfigure(i, weight=1)

        table.columnconfigure(0, weight=1, uniform="col")
        table.columnconfigure(1, weight=1)
        table.columnconfigure(2, weight=1, uniform="col")

        return table

    def creatTableTotalToe(self, parent_frame: tk.Frame, index: int) -> tk.Frame:
        toe_frame = tk.Frame(parent_frame)

        lbl_before = tk.Label(toe_frame, text="До", borderwidth=1, relief="ridge", padx=2, pady=0)
        lbl_before.grid(row=0, column=0, sticky="nsew")
        lbl_after = tk.Label(toe_frame, text="После", borderwidth=1, relief="ridge", padx=2, pady=0)
        lbl_after.grid(row=0, column=1, sticky="nsew")
        
        var_before = tk.DoubleVar()
        var_before.set(self.vehicle_data.get_total_toe(index, "before") or 0.0)        
        spin_before = tk.Spinbox(toe_frame, from_=-20, to=20, increment=0.01, textvariable=var_before, width=8)
        spin_before.grid(row=1, column=0, sticky="nsew")       
        var_before.trace_add("write", lambda *args, v=var_before, 
                             idx=index: self.on_total_toe_update(idx, "before", v)) 

        var_after = tk.DoubleVar()
        var_after.set(self.vehicle_data.get_total_toe(index, "after") or 0.0)        
        val_after = tk.Spinbox(toe_frame, from_=-20, to=20, increment=0.01, textvariable=var_after, width=8)
        val_after.grid(row=1, column=1, sticky="nsew")
        var_after.trace_add("write  ", lambda *args, v=var_after, 
                            idx=index: self.on_total_toe_update(idx, "after", v))
        
        return toe_frame
    
    def on_total_toe_update(self, axle_index: int, position: str, var: tk.DoubleVar):
        """Обновить данные vehicle_data при изменении общего схождения"""
        try:
            value = float(var.get())
            self.vehicle_data.set_total_toe(axle_index, position, value)
        except ValueError:
            pass  # Игнорируем ошибки преобразования