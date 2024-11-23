from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime


def create_pdf(data, title='Table Title', filename='output.pdf'):
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 创建 PDF 文档
    pdf = SimpleDocTemplate(filename, pagesize=A4)

    # 定义表格的Frame
    table_frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height - 2 * inch)

    # 添加表格名称
    styles = getSampleStyleSheet()
    title_text = f'<font size="14">{title}</font>'
    title_paragraph = Paragraph(title_text, styles['Title'])
    title_paragraph.wrapOn(pdf, pdf.width, pdf.topMargin)

    # 计算表格名称高度
    title_height = title_paragraph.height

    # 将字典数据转换为三列的列表
    table_data = [['Name', 'Value', 'Unit']]
    for key, (value, unit) in data.items():
        table_data.append([key, str(value), unit])

    # 设置表格样式
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # 创建表格对象，并设置列宽占满整页
    table = Table(table_data, style=style, colWidths=[pdf.width / 3.0] * 3)

    # 将表格添加到文档
    pdf.build([title_paragraph, table], onFirstPage=lambda c, d: draw_page_number(c, d, current_time),
              onLaterPages=lambda c, d: draw_page_number(c, d, current_time))


def draw_page_number(canvas, doc, current_time):
    page_num = canvas.getPageNumber()
    text = f"Page {page_num} - Generated on: {current_time}"
    canvas.drawRightString(doc.width - doc.rightMargin, doc.bottomMargin - 10, text)


# 你的字典数据
my_dict = {
    'Name1': (30, 'years'),
    'Name2': (1.85, 'meters'),
    'Name3': (80, 'kg'),
    'Name4': (120, 'mmHg')
}

# 调用函数创建 PDF
create_pdf(my_dict, title='My Data Table with Page Number', filename='output_with_page_number.pdf')

