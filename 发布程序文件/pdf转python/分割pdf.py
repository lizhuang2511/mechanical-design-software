# -*- coding = utf-8 -*-
# @time:2024/8/12 12:00
# Author:lizhuang
# @File:分割pdf.py
# @Software:PyCharm
import fitz
import wx


class PDFExtractor(wx.Frame):
    def __init__(self, parent, title):
        super(PDFExtractor, self).__init__(parent, title=title, size=(400, 200))

        self.panel = wx.Panel(self)
        self.file_picker = wx.FilePickerCtrl(self.panel, style=wx.FLP_DEFAULT_STYLE | wx.FLP_USE_TEXTCTRL)
        self.start_page_input = wx.TextCtrl(self.panel)
        self.end_page_input = wx.TextCtrl(self.panel)
        self.extract_button = wx.Button(self.panel, label="Extract", size=(100, 30))

        self.extract_button.Bind(wx.EVT_BUTTON, self.extract_pages)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.file_picker, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(wx.StaticText(self.panel, label="Start Page:"), 0, wx.LEFT | wx.TOP, 10)
        self.sizer.Add(self.start_page_input, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(wx.StaticText(self.panel, label="End Page:"), 0, wx.LEFT | wx.TOP, 10)
        self.sizer.Add(self.end_page_input, 0, wx.EXPAND | wx.ALL, 10)
        self.sizer.Add(self.extract_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.panel.SetSizerAndFit(self.sizer)
        self.Show()

    def extract_pages(self, event):
        file_path = self.file_picker.GetPath()
        start_page = int(self.start_page_input.GetValue())
        end_page = int(self.end_page_input.GetValue())

        doc = fitz.open(file_path)
        output_doc = fitz.open()

        for page_num in range(start_page - 1, end_page):
            output_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

        output_path = file_path.replace(".pdf", "_extracted.pdf")
        output_doc.save(output_path)
        output_doc.close()
        doc.close()

        wx.MessageBox("Extraction complete!", "Success", wx.OK | wx.ICON_INFORMATION)


app = wx.App()
PDFExtractor(None, title="PDF Extractor")
app.MainLoop()
