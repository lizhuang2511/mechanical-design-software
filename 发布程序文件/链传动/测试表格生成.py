from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime
import reportlab.pdfbase.ttfonts #导入reportlab的注册字体
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('SimSun', '../数据文件/联想小新黑体 常规.ttf')) #注册字体
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping


def create_pdf(data, title='Table Title', filename='output.pdf'):
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 创建 PDF 文档
    pdf = SimpleDocTemplate(filename, pagesize=A4)

    # 添加表格名称
    styles = getSampleStyleSheet()
    title_text = f'<font size="14">{title}</font>'
    #title_style.fontName = 'SimSun'  # Use SimSun font for Chinese
    title_style = getSampleStyleSheet()['Title']
    title_style.fontName = 'SimSun'  # Use SimSun font for Chinese
    title_paragraph = Paragraph(title_text, title_style)
    #title_paragraph = Paragraph(title_text, styles['Title'])
    #addMapping('SimSun', 0, 0, 'lx.ttf')
    # 将字典数据转换为三列的列表
    table_data = [['Name', 'Value', 'Unit']]
    for key, (value, unit) in data.items():
        if type(value) == float:
            value = round(value, 4)
        table_data.append([key, str(value), unit])

    # 设置表格样式
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 使用中文字体
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # 计算列宽
    col_widths = [pdf.width / len(table_data[0])] * len(table_data[0])

    # 创建表格对象，并设置列宽占满整页
    table = Table(table_data, style=style, colWidths=col_widths)

    # 将表格添加到文档
    pdf.build([title_paragraph, table], onFirstPage=lambda c, d: draw_page_number(c, d, current_time),
              onLaterPages=lambda c, d: draw_page_number(c, d, current_time))


def draw_page_number(canvas, doc, current_time):
    page_num = canvas.getPageNumber()
    text = f"Page {page_num} - Generated on: {current_time}"
    canvas.drawRightString(doc.width - doc.rightMargin, doc.bottomMargin - 10, text)

if __name__ == '__main__':

    # 你的字典数据
    my_dict = {
        '输入参数：': ('', ''),
        '年2': (1.85, 'meters'),
        '年3': (80, 'kg'),
        '年4': (120, '年mmHg'),
        '年5': (30, '年'),
        '年6': (1.85, 'meters'),
        '年7': (80, 'kg'),
        '年8': (120, '年mmHg'),
        '年9': (30, '年'),
        '年10': (1.85, 'meters'),
        '年11': (80, 'kg'),
        '年12': (120, '年mmHg'),
        '年13': (30, '年'),
        '年14': (1.85, 'meters'),
        '年15': (80, 'kg'),
        '年16': (120, '年mmHg'),
        '年17': (30, '年'),
        '年21': (1.85, 'meters'),
        '年319': (80, 'kg'),
        '年420': (120, '年mmHg'),
        '年221': (30, '年'),
        '年222': (1.85, 'meters'),
        '年323': (80, 'kg'),
        '年424': (120, '年mmHg'),
        '年225': (30, '年'),
        '年226': (1.85, 'meters'),
        '年327': (80, 'kg'),
        '年428': (120, '年mmHg'),
        '年229': (30, '年'),
        '年230': (1.85, 'meters'),
        '年331': (80, 'kg'),
        '年432': (120, '年mmHg'),
        '输出参数：': ('', ''),
        '年234': (1.85, 'meters'),
        '年335': (80, 'kg'),
        '年436': (120, '年mmHg'),
        '年237': (30, '年'),
        '年238': (1.85, 'meters'),
        '年339': (80, 'kg'),
        '年440': (120, '年mmHg'),
        '年241': (30, '年'),
        '年242': (1.85, 'meters'),
        '年343': (80, 'kg'),
        '年444': (120, '年mmHg'),
        '年245': (30, '年'),
    }
    #pdfmetrics.registerFont(TTFont('song', 'lx.ttf'))
    # 调用函数创建 PDF
    create_pdf(my_dict, title='计算涡轮', filename='output_with_page_number.pdf')
