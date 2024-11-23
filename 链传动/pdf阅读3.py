import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QWidget, QLabel, QFileDialog, QAction, QScrollBar, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtCore import Qt
import fitz  # PyMuPDF
from PyQt5.QtPrintSupport import QPrintDialog

class PdfViewer(QMainWindow):
    def __init__(self, default_file_path="E:\mechanical-calculation-4\程序文件\涡轮蜗杆计算\output_with_page_number.pdf"):
        super().__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100,700, 800)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.label = QLabel(self.scroll_area)
        self.label.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.label)

        self.scrollbar = QScrollBar(Qt.Vertical)
        self.scrollbar.valueChanged.connect(self.scrollbar_value_changed)
        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.scrollbar)

        self.current_page_label = QLabel(self)
        self.layout.addWidget(self.current_page_label)

        self.current_page = 0
        self.doc = None
        self.zoom_factor = 1.0

        self.create_actions()
        self.create_toolbar()
        self.lujing = default_file_path
        self.open_pdfdf(self.lujing)

    def create_actions(self):
        self.open_action = QAction('打开', self)
        self.open_action.triggered.connect(self.open_pdf)

        self.prev_page_action = QAction('上一页', self)
        self.prev_page_action.triggered.connect(self.prev_page)

        self.next_page_action = QAction('下一页', self)
        self.next_page_action.triggered.connect(self.next_page)

        self.save_action = QAction('保存', self)
        self.save_action.triggered.connect(self.save_pdf)

        self.zoom_in_action = QAction('放大', self)
        self.zoom_in_action.triggered.connect(self.zoom_in)

        self.zoom_out_action = QAction('缩小', self)
        self.zoom_out_action.triggered.connect(self.zoom_out)

        self.print_action = QAction('打印', self)
        self.print_action.triggered.connect(self.print_pdf)

    def create_toolbar(self):
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.prev_page_action)
        toolbar.addAction(self.next_page_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.zoom_in_action)
        toolbar.addAction(self.zoom_out_action)
        toolbar.addAction(self.print_action)

    def open_pdf(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "打开PDF文件", "", "PDF Files (*.pdf)")
        self.lujing = file_path
        if file_path:
            self.doc = fitz.open(file_path)
            self.show_page(0)

    def open_pdfdf(self, file_path):
        self.doc = fitz.open(file_path)
        self.show_page(0)

    def print_pdf(self):
        if self.doc is not None:
            printer = QPrintDialog(self)
            if printer.exec_() == QPrintDialog.Accepted:
                painter = QPainter()
                painter.begin(printer.printer())
                pixmap = self.label.pixmap()
                painter.drawPixmap(0, 0, pixmap)
                painter.end()

    def show_page(self, page_num):
        if self.doc is not None and 0 <= page_num < len(self.doc):
            page = self.doc.load_page(page_num)
            pixmap = self.render_page(page)
            qt_image = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap)

            # Adjust label size to fit content
            self.label.setFixedSize(pixmap.width(), pixmap.height())
            self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            # Center the label within the scroll area
            scroll_width = self.scroll_area.width()
            label_width = self.label.width()
            self.label.setGeometry((scroll_width - label_width) // 2, 0, label_width, self.label.height())

            # Set scrollbar range and position
            self.scrollbar.setRange(0, pixmap.height() - self.scroll_area.height())
            self.scrollbar.setValue(0)

            self.current_page = page_num
            self.update_page_label()

    def render_page(self, page):
        matrix = fitz.Matrix(self.zoom_factor, self.zoom_factor)
        pixmap = page.get_pixmap(matrix=matrix)
        return pixmap

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Center the label both horizontally and vertically
        scroll_width = self.scroll_area.width()
        label_width = self.label.width()

        scroll_height = self.scroll_area.height()
        label_height = self.label.height()

        self.label.setGeometry((scroll_width - label_width) // 2, (scroll_height - label_height) // 2, label_width,
                               label_height)
        self.scrollbar.setGeometry(scroll_width - self.scrollbar.width(), 0, self.scrollbar.width(), scroll_height)

    def scrollbar_value_changed(self, value):
        self.label.setGeometry((self.scroll_area.width() - self.label.width()) // 2, value, self.label.width(), self.label.height())

    def update_page_label(self):
        total_pages = len(self.doc) if self.doc else 0
        file_info = f'文件: {self.lujing}' if self.lujing else '文件未打开'
        self.current_page_label.setText(f'{file_info} | 页数: {self.current_page + 1} / {total_pages}')

    def prev_page(self):
        if self.current_page > 0:
            self.show_page(self.current_page - 1)

    def next_page(self):
        if self.current_page < len(self.doc) - 1:
            self.show_page(self.current_page + 1)

    def save_pdf(self):
        if self.doc is not None:
            save_path, _ = QFileDialog.getSaveFileName(self, "保存PDF文件", "", "PDF Files (*.pdf)")
            if save_path:
                self.doc.save(save_path)

    def zoom_in(self):
        if self.doc is not None:
            self.zoom_factor *= 1.2
            self.show_page(self.current_page)

    def zoom_out(self):
        if self.doc is not None:
            self.zoom_factor /= 1.2
            self.show_page(self.current_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    default_file_path = "..\涡轮蜗杆计算\output_with_page_number.pdf"
    viewer = PdfViewer(default_file_path)
    viewer.show()
    sys.exit(app.exec_())
