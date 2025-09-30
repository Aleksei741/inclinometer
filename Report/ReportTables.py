from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from Truck import VehicleAlignmentData

def creatTableSteerableWheelParams(vehicle_data: VehicleAlignmentData, axle_index: int, side: str, place_width) -> Table:
    center_style = ParagraphStyle(
        name='Center',
        alignment=1,  # 0=LEFT, 1=CENTER, 2=RIGHT, 4=JUSTIFY
        fontName='DejaVu',  # твой шрифт с кириллицей
        fontSize=8,
        leading=9
        )

    operations = ["Развал", "Схождение", "Угол продольного наклона шкворня",
                    "Угол поперечного наклона шкворня", "Разность углов в повороте"]
    headers = ["До", "Операция", "После"]

    camber_before = f"{vehicle_data.get_camber(axle_index, side, 'before') or '0'}"
    camber_after  = f"{vehicle_data.get_camber(axle_index, side, 'after') or '0'}"
    toe_before    = f"{vehicle_data.get_toe(axle_index, side, 'before') or '0'}"
    toe_after     = f"{vehicle_data.get_toe(axle_index, side, 'after') or '0'}"
    caster_angle_before  = f"{vehicle_data.get_caster_angle(axle_index, side, 'before') or '0'}"
    caster_angle_after   = f"{vehicle_data.get_caster_angle(axle_index, side, 'after') or '0'}"
    steering_axis_inclination_before = f"{vehicle_data.get_steering_axis_inclination(axle_index, side, 'before') or '0'}"
    steering_axis_inclination_after  = f"{vehicle_data.get_steering_axis_inclination(axle_index, side, 'after') or '0'}"
    turning_angle_difference_before  = f"{vehicle_data.get_turning_angle_difference(axle_index, side, 'before') or '0'}"
    turning_angle_difference_after   = f"{vehicle_data.get_turning_angle_difference(axle_index, side, 'after') or '0'}"
    
    table_data = [
        [Paragraph(headers[0], center_style), Paragraph(headers[1], center_style), Paragraph(headers[2], center_style)],
        [Paragraph(camber_before, center_style), Paragraph(operations[0], center_style), Paragraph(camber_after, center_style)],
        [Paragraph(toe_before, center_style), Paragraph(operations[1], center_style), Paragraph(toe_after, center_style)],
        [Paragraph(caster_angle_before, center_style), Paragraph(operations[2], center_style), Paragraph(caster_angle_after, center_style)],
        [Paragraph(steering_axis_inclination_before, center_style), Paragraph(operations[3], center_style), Paragraph(steering_axis_inclination_after, center_style)],
        [Paragraph(turning_angle_difference_before, center_style), Paragraph(operations[4], center_style), Paragraph(turning_angle_difference_after, center_style)]
    ]
    
    # col_widths = [place_width * 0.2, place_width * 0.6, place_width * 0.2]
    col_widths = [place_width * 0.22, place_width * 0.56, place_width * 0.22]

    table = Table(table_data, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('LEFTPADDING', (0,0), (-1,-1), 1),
    ('RIGHTPADDING', (0,0), (-1,-1), 1),
    ]))
    return table

def creatTableFixedWheelParams(vehicle_data: VehicleAlignmentData, axle_index: int, side: str, place_width, axel_shift=True, axle_twist=True) -> Table:
    center_style = ParagraphStyle(
        name='Center',
        alignment=1,  # 0=LEFT, 1=CENTER, 2=RIGHT, 4=JUSTIFY
        fontName='DejaVu',  # твой шрифт с кириллицей
        fontSize=8,
        leading=8
        )

    operations = ["Развал", "Сдвиг оси", "Перекос оси"]
    headers = ["До", "Операция", "После"]

    camber_before = f"{vehicle_data.get_camber(axle_index, side, "before") or '0'}"
    camber_after = f"{vehicle_data.get_camber(axle_index, side, "after") or '0'}"
    axel_shift_before = f"{vehicle_data.get_axel_shift(axle_index, side, "before") or '0'}"
    axel_shift_after = f"{vehicle_data.get_axel_shift(axle_index, side, "after") or '0'}"
    axle_twist_before = f"{vehicle_data.get_axle_twist(axle_index, side, "before") or '0'}"
    axle_twist_after = f"{vehicle_data.get_axle_twist(axle_index, side, "after") or '0'}"

    table_data = list()
    table_data.append([Paragraph(headers[0], center_style), Paragraph(headers[1], center_style), Paragraph(headers[2], center_style)])
    table_data.append([Paragraph(camber_before, center_style), Paragraph(operations[0], center_style), Paragraph(camber_after, center_style)])
    if axel_shift:
        table_data.append([Paragraph(axel_shift_before, center_style), Paragraph(operations[1], center_style), Paragraph(axel_shift_after, center_style)])    
    if axle_twist:
        table_data.append([Paragraph(axle_twist_before, center_style), Paragraph(operations[2], center_style), Paragraph(axle_twist_after, center_style)])
        
    col_widths = [place_width * 0.2, place_width * 0.6, place_width * 0.2]
    col_widths = [place_width * 0.22, place_width * 0.56, place_width * 0.22]

    table = Table(table_data, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('TOPPADDING', (0,0), (-1,-1), 1),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('LEFTPADDING', (0,0), (-1,-1), 1),
    ('RIGHTPADDING', (0,0), (-1,-1), 1),
    ]))
    return table

def CreateMiddlePositionSteeringWheelTable(vehicle_data: VehicleAlignmentData, width: float) -> Table:
    """Создать таблицу среднего положения рулевого колеса"""
    center_style = ParagraphStyle(
        name='Center',
        alignment=1,  # 0=LEFT, 1=CENTER, 2=RIGHT, 4=JUSTIFY
        fontName='DejaVu',  # твой шрифт с кириллицей
        fontSize=8,
        leading=8
        )
    
    operations = ["Среднее положение рулевого колеса"]
    headers = ["До", "Операция", "После"]

    # Значения
    val_before = f"{vehicle_data.get_middle_position_steering_wheel("before") or '0'}"
    val_after = f"{vehicle_data.get_middle_position_steering_wheel("after") or '0'}"

    table_data = list()
    table_data.append([Paragraph(headers[0], center_style), Paragraph(headers[1], center_style), Paragraph(headers[2], center_style)])
    table_data.append([Paragraph(val_before, center_style), Paragraph(operations[0], center_style), Paragraph(val_after, center_style)])

    col_widths = [width * 0.2, width * 0.6, width * 0.2]

    table = Table(table_data, colWidths=col_widths, hAlign='CENTER')
    table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 1),
        ('RIGHTPADDING', (0,0), (-1,-1), 1),
    ]))

    return table

def creatTotalToeTable(vehicle_data: VehicleAlignmentData, axel_index: int, place_width: float) -> Table:
    """Создать таблицу суммарного схождения"""  
    center_style = ParagraphStyle(
    name='Center',
    alignment=1,  # 0=LEFT, 1=CENTER, 2=RIGHT, 4=JUSTIFY
    fontName='DejaVu',  # твой шрифт с кириллицей
    fontSize=8,
    leading=8
    )
    
    operations = ["Общее схождение оси"]
    headers = ["До", "После"]

    val_before = f"{vehicle_data.get_total_toe(axel_index, "before") or '0'}"
    val_after = f"{vehicle_data.get_total_toe(axel_index, "after") or '0'}"

    table_data = [
        [Paragraph(operations[0], center_style), ""],
        [Paragraph(headers[0], center_style), Paragraph(headers[1], center_style)],
        [Paragraph(val_before, center_style), Paragraph(val_after, center_style)]
    ]

    col_widths = [place_width * 0.5, place_width * 0.5]
    table = Table(table_data, hAlign='CENTER', colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('BACKGROUND', (0,1), (1,1), colors.white),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 1),
        ('RIGHTPADDING', (0,0), (-1,-1), 1),
        ('SPAN', (0, 0), (1, 0)),
    ]))

    return table