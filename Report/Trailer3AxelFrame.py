from Truck import VehicleAlignmentData
from reportlab.platypus import Flowable
from reportlab.lib import colors
from Report.ReportTables import creatTableFixedWheelParams
from Report.ReportTables import creatTotalToeTable


class Trailer3Axel(Flowable):
    def __init__(self, vehicle_data: VehicleAlignmentData):
        super().__init__()
        self.width = 0
        self.height = 450

        # Таблицы осей
        self.table_axel1_l = creatTableFixedWheelParams(vehicle_data, 0, "left", 150)
        self.table_axel1_r = creatTableFixedWheelParams(vehicle_data, 0, "right", 150)
        self.table_axel2_l = creatTableFixedWheelParams(vehicle_data, 1, "left", 150)
        self.table_axel2_r = creatTableFixedWheelParams(vehicle_data, 1, "right", 150)
        self.table_axel3_l = creatTableFixedWheelParams(vehicle_data, 2, "left", 150)
        self.table_axel3_r = creatTableFixedWheelParams(vehicle_data, 2, "right", 150)

        self.toe_table_axel1 = creatTotalToeTable(vehicle_data, 0, 75)
        self.toe_table_axel2 = creatTotalToeTable(vehicle_data, 1, 75)
        self.toe_table_axel3 = creatTotalToeTable(vehicle_data, 2, 75)

        self.img_path = "img/TRAILER_3_AXLE.png"

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        #self.height = availHeight
        return self.width, self.height

    def draw(self):   
        # Рисуем изображение грузовика     
        img_width = self.width * 0.4
        img_height = self.height
        img_x = (self.width - img_width) / 2
        img_y = (self.height - img_height) / 2 - 20

        self.canv.drawImage(
            self.img_path,
            img_x, img_y,
            width=img_width,
            height=img_height,
            preserveAspectRatio=True,
            mask='auto'
        )

        # Левые таблицы
        # Ост 1
        table_w, table_h = self.table_axel1_l.wrap(self.width, self.height)
        table_x = 0
        table_y = 205
        self.table_axel1_l.wrapOn(self.canv, table_w, table_h)
        self.table_axel1_l.drawOn(self.canv, table_x, table_y)

        # Ось 2
        table_w, table_h = self.table_axel2_l.wrap(self.width, self.height)
        table_x = 0
        table_y = 120
        self.table_axel2_l.wrapOn(self.canv, table_w, table_h)
        self.table_axel2_l.drawOn(self.canv, table_x, table_y)

        # Ось 3
        table_w, table_h = self.table_axel3_l.wrap(self.width, self.height)
        table_x = 0
        table_y = 40
        self.table_axel3_l.wrapOn(self.canv, table_w, table_h)
        self.table_axel3_l.drawOn(self.canv, table_x, table_y)


        # Правые таблицы
        # Ось 1
        table_w, table_h = self.table_axel1_r.wrap(self.width, self.height)
        table_x = self.width - table_w
        table_y = 205
        self.table_axel1_r.wrapOn(self.canv, table_w, table_h)
        self.table_axel1_r.drawOn(self.canv, table_x, table_y)

        # Ось 2
        table_w, table_h = self.table_axel2_r.wrap(self.width, self.height)
        table_x = self.width - table_w
        table_y = 120
        self.table_axel2_r.wrapOn(self.canv, table_w, table_h)
        self.table_axel2_r.drawOn(self.canv, table_x, table_y)

        # Ось 3
        table_w, table_h = self.table_axel3_r.wrap(self.width, self.height)
        table_x = self.width - table_w
        table_y = 40
        self.table_axel3_r.wrapOn(self.canv, table_w, table_h)
        self.table_axel3_r.drawOn(self.canv, table_x, table_y)

        # Надпись по центру сверху
        self.canv.setFont("DejaVu", 12)   # шрифт и размер
        self.canv.setFillColor(colors.black)  # цвет текста
        text_x = self.width / 2
        text_y = self.height - 40
        self.canv.drawCentredString(text_x, text_y, "Общее схождение оси:")

        # Таблицы суммарного схождения
        # Ось 1
        table_w, table_h = self.toe_table_axel1.wrap(self.width, self.height)
        table_x = (self.width - table_w) / 2 - 3 
        table_y = 220
        self.toe_table_axel1.wrapOn(self.canv, table_w, table_h)
        self.toe_table_axel1.drawOn(self.canv, table_x, table_y)

        # Ось 2
        table_w, table_h = self.toe_table_axel2.wrap(self.width, self.height)
        table_x = (self.width - table_w) / 2 - 3 
        table_y = 137
        self.toe_table_axel2.wrapOn(self.canv, table_w, table_h)
        self.toe_table_axel2.drawOn(self.canv, table_x, table_y)

        #Ось 3
        table_w, table_h = self.toe_table_axel3.wrap(self.width, self.height)
        table_x = (self.width - table_w) / 2 - 3 
        table_y = 55
        self.toe_table_axel3.wrapOn(self.canv, table_w, table_h)
        self.toe_table_axel3.drawOn(self.canv, table_x, table_y)
        

