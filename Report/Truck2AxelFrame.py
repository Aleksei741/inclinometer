from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from Truck import VehicleAlignmentData
from reportlab.platypus import Flowable
from Report.ReportTables import creatTableSteerableWheelParams, creatTableFixedWheelParams

class Truck2Axel(Flowable):
    def __init__(self, vehicle_data: VehicleAlignmentData):
        super().__init__()
        self.width = 0
        self.height = 450

        # Таблицы осей
        self.table_axel1_l = creatTableSteerableWheelParams(vehicle_data, 0, "left", 150)
        self.table_axel1_r = creatTableSteerableWheelParams(vehicle_data, 0, "right", 150)
        self.table_axel2_l = creatTableFixedWheelParams(vehicle_data, 1, "left", 150)
        self.table_axel2_r = creatTableFixedWheelParams(vehicle_data, 1, "right", 150)

        self.img_path = "img/TRUCK_2_AXLE.png"

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        #self.height = availHeight
        return self.width, self.height

    def draw(self):
        # Рисуем картинку в центре
        img_width = self.width
        img_x = (self.width - img_width) / 2
        self.canv.drawImage(
            self.img_path,
            img_x, 0,
            width=img_width,
            height=self.height,
            preserveAspectRatio=True,
            mask='auto'
        )

        # Левые таблицы
        table_w, table_h = self.table_axel1_l.wrap(self.width, self.height)
        self.table_axel1_l.wrapOn(self.canv, table_w, table_h)
        self.table_axel1_l.drawOn(self.canv, 0, self.height - table_h)

        table_w, table_h = self.table_axel2_l.wrap(self.width, self.height)
        self.table_axel2_l.wrapOn(self.canv, table_w, table_h)
        self.table_axel2_l.drawOn(self.canv, 0, 20)

        # Правые таблицы
        table_w, table_h = self.table_axel1_r.wrap(self.width, self.height)
        self.table_axel1_r.wrapOn(self.canv, table_w, table_h)
        self.table_axel1_r.drawOn(self.canv, self.width-table_w, self.height-table_h)

        table_w, table_h = self.table_axel2_r.wrap(self.width, self.height)
        self.table_axel2_r.wrapOn(self.canv, table_w, table_h)
        self.table_axel2_r.drawOn(self.canv, self.width-table_w, 20)

