import tkinter as tk
from tkinter import ttk
from Truck import VehicleAlignmentData, TruckBodyType
from Window.Truck2AxelWindow import Truck2AxelWindow
from Window.Truck3AxelWindow import Truck3AxelWindow
from Window.Truck4AxelWindow import Truck4AxelWindow
from Window.Trailer1AxelWindow import Trailer1AxelWindow
from Window.Trailer2AxelWindow import Trailer2AxelWindow
from Window.Trailer3AxelWindow import Trailer3AxelWindow
from Window.RigidTrailer2AxelWindow import RigidTrailer2AxelWindow

# Фрейм для схемы автомобиля
class CarFrame(tk.Frame):
    def __init__(self, parent, car_brand, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        label = tk.Label(self, text=f"Схема автомобиля: {car_brand}", bg="lightgray")
        label.pack(fill="both", expand=True, padx=10, pady=10)


class MainWindow(tk.Tk):
    def __init__(self, vehicle_data: VehicleAlignmentData):
        super().__init__()

        self.vehicle_data = vehicle_data
 
        self.title("Диагностика автомобиля")
        self.geometry("900x600")

        # ---------- Скрол ----------
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Canvas + Scrollbar
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Внутренний фрейм, в который помещается всё содержимое
        self.scrollable_frame = tk.Frame(canvas)

        # Обновляем scrollregion при изменении размеров
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # ---------- Кнопки ----------
        button_frame = tk.Frame(self.scrollable_frame)
        button_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(button_frame, text="Загрузить данные с прибора", command=self.load_data).pack(side="left", padx=5)
        tk.Button(button_frame, text="Сохранить отчет (PDF)", command=self.save_pdf).pack(side="left", padx=5)
        tk.Button(button_frame, text="Сохранить сессию", command=self.save_session).pack(side="left", padx=5)
        tk.Button(button_frame, text="Открыть сессию", command=self.load_session).pack(side="left", padx=5)

        # ---------- Данные компании ----------
        company_frame = ttk.LabelFrame(self.scrollable_frame, text="Данные компании")
        company_frame.pack(fill="x", padx=10, pady=5)

        self.company_name = self._add_labeled_entry(company_frame, "Наименование компании:", self.vehicle_data.get_company_name(), 0, 0, 100, self.on_company_update)
        self.company_address = self._add_labeled_entry(company_frame, "Адрес:", self.vehicle_data.get_address(), 1, 0, 100, self.on_company_update)
        self.company_phone = self._add_labeled_entry(company_frame, "Телефон:", self.vehicle_data.get_phone(), 2, 0, 100, self.on_company_update)

        # ---------- Данные автомобиля ----------
        car_frame = ttk.LabelFrame(self.scrollable_frame, text="Данные автомобиля")
        car_frame.pack(fill="x", padx=10, pady=5)

        self.car_brand = self._add_labeled_entry(car_frame, "Марка авто:", self.vehicle_data.get_car_brand(), 0, 0, 50, self.on_car_update)
        self.car_model = self._add_labeled_entry(car_frame, "Модель:", self.vehicle_data.get_model(), 1, 0, 50, self.on_car_update)
        self.car_chassis = self._add_labeled_entry(car_frame, "№ шасси:", self.vehicle_data.get_chassis_number(), 2, 0, 50, self.on_car_update)
        self.car_mileage = self._add_labeled_entry(car_frame, "Пробег (км):", self.vehicle_data.get_mileage(), 3, 0, 50, self.on_car_update)

        self.car_regnum = self._add_labeled_entry(car_frame, "Рег. номер:", self.vehicle_data.get_reg_number(), 0, 2, 50, self.on_car_update)
        self.car_owner = self._add_labeled_entry(car_frame, "Владелец:", self.vehicle_data.get_owner(), 1, 2, 50, self.on_car_update)

        label_car_tires = tk.Label(car_frame, text="Давление в шинах:")
        label_car_tires.grid(row=2, column=2, sticky="e", padx=5, pady=2)
        self.car_tires = tk.Frame(car_frame)
        self.car_tires.grid(row=2, column=3, rowspan=2, padx=5, pady=2)
        self.tire_vars = []

        # Настройка сетки (чтобы оба столбца растягивались)
        car_frame.columnconfigure(1, weight=1)
        car_frame.columnconfigure(3, weight=1)

        # ---------- Схема автомобиля ----------
        self.scheme_frame = ttk.LabelFrame(self.scrollable_frame, text="Схема автомобиля и сход-развал")
        self.scheme_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # ---------- Вспомогательные методы ----------
    def _add_labeled_entry(self, parent, text, value, row, col, width, callback):
        """Создание поля ввода с StringVar и привязкой обработчика"""
        label = tk.Label(parent, text=text)
        label.grid(row=row, column=col, sticky="e", padx=5, pady=2)

        var = tk.StringVar()    # создаём пустую переменную
        var.set(value or "")    # присваиваем value, если None — ставим пустую строку
        entry = tk.Entry(parent, textvariable=var, width=width)
        entry.grid(row=row, column=col + 1, sticky="w", padx=5, pady=2)

        var.trace_add("write", lambda *args: callback(text, var.get()))
        return var
 
    # ---------- методы обновления рабочей области ----------
    def on_truck_body_change(self, new_body: TruckBodyType):
        """Меняем кузов и пересоздаём поля шин"""
        self.truck_body = new_body
        self._update_tire_fields(self.truck_body)
        self._update_scheme_fields(self.truck_body)

    def _update_tire_fields(self, truck_body: TruckBodyType):
        """Обновить количество полей шин в зависимости от TruckBodyType"""
        # Удаляем старые виджеты
        for widget in self.car_tires.winfo_children():
            widget.destroy()

        # Очищаем список переменных
        self.tire_vars.clear()

        if not truck_body:
            return

        self.truck_body = truck_body

        for i in range(self.truck_body.total_axles):
            # Читаем текущее давление из VehicleAlignmentData, если есть
            left_value = self.vehicle_data.get_pressure(i, "left") or 2.2
            right_value = self.vehicle_data.get_pressure(i, "right") or 2.2

            # Левая шина
            var_left = tk.DoubleVar()       # создаем без значения
            var_left.set(left_value)        # задаем значение до trace
            spin_left = tk.Spinbox(
                self.car_tires, from_=0.1, to=20.0, increment=0.1,
                textvariable=var_left, format="%.1f", width=5
            )
            spin_left.grid(row=1, column=i, padx=2)
            # trace добавляем **после установки начального значения**
            var_left.trace_add("write", lambda *args, v=var_left, idx=i: self.on_tire_update(idx, "left", v))
            self.tire_vars.append(var_left)

            # Правая шина
            var_right = tk.DoubleVar()
            var_right.set(right_value)
            spin_right = tk.Spinbox(
                self.car_tires, from_=0.1, to=20.0, increment=0.1,
                textvariable=var_right, format="%.1f", width=5
            )
            spin_right.grid(row=0, column=i, padx=2)
            var_right.trace_add("write", lambda *args, v=var_right, idx=i: self.on_tire_update(idx, "right", v))
            self.tire_vars.append(var_right)

    def _update_scheme_fields(self, truck_body: TruckBodyType):
        """ Обновить схему автомобиля """
        # Удаляем старые виджеты
        for widget in self.scheme_frame.winfo_children():
            widget.destroy()

        if truck_body == TruckBodyType.TRUCK_2_AXLE:
            self.truck_window = Truck2AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.TRUCK_3_AXLE:
            self.truck_window = Truck3AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.TRUCK_4_AXLE_TWIN_STEER:
            self.truck_window = Truck4AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.BUS_2_AXLE:
            self.truck_window = Truck2AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.BUS_3_AXLE:
            self.truck_window = Truck3AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.TRAILER_1_AXLE:
            self.truck_window = Trailer1AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.TRAILER_2_AXLE:
            self.truck_window = Trailer2AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.TRAILER_3_AXLE:
            self.truck_window = Trailer3AxelWindow(self.scheme_frame, self.vehicle_data)
        elif truck_body == TruckBodyType.RIGID_TRAILER_2_AXLE:
            self.truck_window = RigidTrailer2AxelWindow(self.scheme_frame, self.vehicle_data)

        self.truck_window.pack(fill="both", expand=True)


    # ---------- Обработчики ----------
    def on_tire_update(self, axle_index: int, side: str, var: tk.DoubleVar):
        """Обновить данные vehicle_data при изменении давления в шине"""
        try:
            self.vehicle_data.set_pressure(
                axle_index=axle_index,
                side=side,
                value=var.get()
            )
        except Exception as e:
            print("Ошибка при обновлении давления:", e)

    def on_company_update(self, field, value):
        if( field == "Наименование компании:"):
            self.vehicle_data.set_company_name(value)
        elif( field == "Адрес:"):
            self.vehicle_data.set_address(value)
        elif( field == "Телефон:"):
            self.vehicle_data.set_phone(value)        

    def on_car_update(self, field, value):
        if field == "Марка авто:":
            self.vehicle_data.set_car_brand(value)
        elif field == "Модель:":
            self.vehicle_data.set_model(value)
        elif field == "№ шасси:":
            self.vehicle_data.set_chassis_number(value) 
        elif field == "Пробег (км):":
            self.vehicle_data.set_mileage(value)
        elif field == "Рег. номер:":    
            self.vehicle_data.set_reg_number(value)
        elif field == "Владелец:":
            self.vehicle_data.set_owner(value)

    def load_data(self):
        print("Загрузка данных с прибора...")

    def save_pdf(self):
        print("Сохранение отчета в PDF...")

    def save_session(self):
        print("Сохранение сессии...")

    def load_session(self):
        print("Открытие сессии...")