import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, Flowable
from reportlab.lib.styles import ParagraphStyle
from Truck import VehicleAlignmentData, TruckBodyType
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime

from Report.Truck2AxelFrame import Truck2Axel
from Report.Truck3AxelFrame import Truck3Axel
from Report.Truck4AxelFrame import Truck4Axel
from Report.Trailer1AxelFrame import Trailer1Axel
from Report.Trailer2AxelFrame import Trailer2Axel
from Report.Trailer3AxelFrame import Trailer3Axel
from Report.RigidTrailer2AxelFrame import RigidTrailer2Axel

def create_style():
    # Регистрируем шрифт с поддержкой кириллицы
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVu-Italic', 'DejaVuSans-Oblique.ttf'))

    # Создаем стиль для заголовков
    title_style = ParagraphStyle(
        name='TitleDejaVu',
        fontName='DejaVu',
        fontSize=18,
        leading=22,
        alignment=1  # Выравнивание по центру
    )

    # Создаем стиль для обычного текста
    normal_style = ParagraphStyle(
        name='NormalDejaVu',
        fontName='DejaVu',
        fontSize=12,
        leading=14
    )
    return title_style, normal_style

def CreateTableCompanyInfo(vehicle_data: VehicleAlignmentData, place_width: float, normal_style) -> Table:
    # Информация о компании
    company_info = [
        [Paragraph("Наименование компании:", normal_style), Paragraph(vehicle_data.get_company_name() or "-", normal_style)],
        [Paragraph("Адрес:", normal_style), Paragraph(vehicle_data.get_address() or "-", normal_style)],
        [Paragraph("Телефон:", normal_style), Paragraph(vehicle_data.get_phone() or "-", normal_style)]
    ]
    # Разбиваем ширину таблицы на колонки (например, 30% и 70%)
    col_widths = [place_width * 0.35, place_width * 0.65]

    table = Table(company_info, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),  # внешняя рамка
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),      # выравнивание по вертикали
    ]))
    return table

def CreateTableCarInfo(vehicle_data: VehicleAlignmentData, place_width: float, normal_style) -> Table:
    
    left_pressure = ""
    right_pressure = ""    
    for i in range(vehicle_data.body_type.total_axles):       
        left_pressure = f"{left_pressure} {vehicle_data.get_pressure(i, 'left'):.1f}"
        right_pressure = f"{right_pressure} {vehicle_data.get_pressure(i, 'right'):.1f}"
    
    car_info = [
        [Paragraph("Марка", normal_style), Paragraph(vehicle_data.get_car_brand() or "-", normal_style),
         Paragraph("Модель", normal_style), Paragraph(vehicle_data.get_model() or "-", normal_style)],
        [Paragraph("№ шасси", normal_style), Paragraph(vehicle_data.get_chassis_number() or "-", normal_style),
         Paragraph("Пробег, км", normal_style), Paragraph(str(vehicle_data.get_mileage() or "-"), normal_style)],
        [Paragraph("Гос. номер", normal_style), Paragraph(vehicle_data.get_reg_number() or "-", normal_style),
         Paragraph("Давление в шинах (атм)", normal_style), Paragraph(f"Прав. {right_pressure}", normal_style)],
        [Paragraph("Владелец", normal_style), Paragraph(vehicle_data.get_owner() or "-", normal_style),
            Paragraph("", normal_style), Paragraph(f" Лев. {left_pressure}", normal_style)]
    ]
    
    col_widths = [place_width * 0.15, place_width * 0.35, place_width * 0.25, place_width * 0.25]

    table = Table(car_info, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),   # только внешняя рамка
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBEFORE', (0,0), (-1,-1), 0.5, colors.black),  # вертикальная линия
        ('LINEABOVE', (0,0), (-1,2), 0.5, colors.black), # горизонтальная линия 
        ('LINEABOVE', (0,2), (1,3), 0.5, colors.black), # горизонтальная линия 
        ('SPAN', (2,2), (2,3)),
    ]))
    return table

def createTitle(title_style) -> Paragraph:
    return Paragraph("Протокол измерений транспортного средства", title_style)

def CreateMeasurementInfoBox(width: float, normal_style) -> Table:
    text = (
        "<b>измеряются в [°]</b> <font name='DejaVu-Italic'>Развал, Углы продольного и поперечного наклона шкворня, "
        "Разн. углов в повороте, Центральное положение рулевого колеса, Перекос оси.</font><br/>"
        "<b>измеряются в [мм]</b> <font name='DejaVu-Italic'>Общее схождение, Индивидуальное схождение, Сдвиг оси.</font>"
    )

    # Таблица из одной ячейки
    table = Table(
        [[Paragraph(text, normal_style)]],
        colWidths=[width]
    )

    # Рамка
    table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))

    return table

# Табличка исполнитель, дата, примечания
def createTableEnd(width: float, normal_style) -> Table:
    mail_style = ParagraphStyle(
        name='NormalDejaVu',
        fontName='DejaVu',
        fontSize=12,
        leading=14,
        alignment=2  # Выравнивание по правому краю
    )

    today_str = datetime.now().strftime("%d.%m.%Y")

    img_path = "img/lasertruck.png"
    footer_data = [
        [Paragraph("Исполнитель:", normal_style), Paragraph(f"Дата: {today_str}", normal_style), ""],
        [Paragraph("Примечания:", normal_style), "", Paragraph("www.lasertruck.ru<br/>info@lasertruck.ru", mail_style)],
        ["", "", Image(img_path, width=120, height=20)]
    ]

    col_widths = [width * 0.4, width * 0.3, width * 0.3]

    table = Table(footer_data, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
        # Общая рамка и сетка
        ('BOX', (0, 0), (1, 2), 1, colors.black),   # рамка вокруг первых 2х колонок
        ('GRID', (0, 0), (1, 0), 0.5, colors.black), # линии только в первой строке

        # Объединение ячеек "Примечания"
        ('SPAN', (0, 1), (1, 2)),
        ('VALIGN', (0, 1), (1, 2), 'TOP'),
        ('ALIGN', (0, 1), (1, 2), 'LEFT'),

        ('ALIGN', (2, 1), (2, 1), 'RIGHT'),
        ('ALIGN', (2, 2), (2, 2), 'RIGHT')
    ]))
    return table

def save_to_pdf(vehicle_data: VehicleAlignmentData, pdf_path: str):

    title_style, normal_style = create_style()

    margin = 20          # отступ слева и справа
    place_width = A4[0] - 2 * margin    # ширина таблицы с учетом отступов
    
    if os.path.exists(pdf_path):
        try:
            os.remove(pdf_path)
        except PermissionError:
            raise PermissionError(f"Не удалось удалить {pdf_path}, файл занят или нет прав")
        except OSError as e:
            raise OSError(f"Ошибка при удалении {pdf_path}: {e}")


    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            rightMargin=margin, leftMargin=margin,
                            topMargin=20, bottomMargin=20)
    
    elements = []

    table = CreateTableCompanyInfo(vehicle_data, place_width, normal_style)
    elements.append(table)
    
    table = CreateTableCarInfo(vehicle_data, place_width, normal_style)
    elements.append(Spacer(1, 5))
    elements.append(table)

    Title = createTitle(title_style)
    elements.append(Spacer(1, 5))
    elements.append(Title)

    table = CreateMeasurementInfoBox(place_width, normal_style)
    elements.append(Spacer(1, 5))
    elements.append(table)

    if vehicle_data.body_type == TruckBodyType.TRUCK_2_AXLE:
        flow = Truck2Axel(vehicle_data) 
    elif vehicle_data.body_type == TruckBodyType.TRUCK_3_AXLE:
        flow = Truck3Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.TRUCK_4_AXLE_TWIN_STEER:
        flow = Truck4Axel(vehicle_data) 
    elif vehicle_data.body_type == TruckBodyType.BUS_2_AXLE:
        flow = Truck2Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.BUS_3_AXLE:
        flow = Truck3Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.TRAILER_1_AXLE:
        flow = Trailer1Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.TRAILER_2_AXLE:
        flow = Trailer2Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.TRAILER_3_AXLE:
        flow = Trailer3Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.RIGID_TRAILER_2_AXLE:
        flow = RigidTrailer2Axel(vehicle_data)
    elif vehicle_data.body_type == TruckBodyType.MINIBUS:
        flow = Truck2Axel(vehicle_data) 
    else:
        raise ValueError(f"Неподдерживаемый тип кузова: {vehicle_data.body_type}")
        
    elements.append(Spacer(1, 5))
    elements.append(flow)

    table = createTableEnd(place_width, normal_style)
    elements.append(Spacer(1, 5))
    elements.append(table)

    doc.build(elements) 