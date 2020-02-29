import sys
from bs4 import BeautifulSoup
from pathlib import Path
from PySide2 import QtWidgets
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt
from PySide2 import QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView

import time

class ExportDialog(QtWidgets.QDialog):

    settings = {}
    settings['rect'] = QtCore.QRect(50, 50, 850, 800)
    

    def __init__(self, data, pdf_callback, parent=None):
        super(ExportDialog, self).__init__(parent)
        self.setGeometry(ExportDialog.settings['rect'])
        self.setSizeGripEnabled(True)
        self.webview = QWebEngineView()
        self.page = QtWebEngineWidgets.QWebEnginePage()
        self.data = data
        self.btn_pdf = QtWidgets.QPushButton('To PDF')
        self.btn_save = QtWidgets.QPushButton('Save')
        self.btn_close = QtWidgets.QPushButton('Close')
        
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_pdf)
        btn_layout.addWidget(self.btn_close)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.webview)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        
        self.btn_save.clicked.connect(self.accept)
        self.btn_pdf.clicked.connect(self.to_pdf)
        self.btn_close.clicked.connect(self.reject)
        self.page.pdfPrintingFinished.connect(lambda _1, _2: self.printing_result(_1, _2))
        self.page.pdfPrintingFinished.connect(lambda _1, _2: print(_1, _2))
        
        self.webview.show()
        self.fill_page()
        

    def done(self, arg__1):
        ExportDialog.settings['rect'] = self.geometry()
        
        super(ExportDialog, self).done(arg__1)
    
    def fill_page(self):
        
        with open(self.data['template'], encoding='utf-8') as f:
            soup = BeautifulSoup(f, features='lxml')
            
        soup.find(id='clinic').string = self.data['clinic']
        soup.find(id='name').string = self.data['name']
        
        _age_tag = soup.new_tag('span', id='age')
        _age_tag.string = f"({self.data['age']})"
        soup.find(id='name').append(_age_tag)
        
        soup.find(id='sex').string = self.data['sex']
        soup.find(id='date').string = self.data['date']
        soup.find(id='shots').string = str(self.data['shots'])
        soup.find(id='instruction').string = self.data['instruction']
        soup.find(id='doctor-name').string = self.data['doctor-name']
        
        # set ingredients
        for _x in self.data['ingredients']:
            _tag = soup.new_tag('div', **{'class': 'ingredient'})
            _tag.string = '{} {} {}'.format(_x['f_name_1'], _x['mass'], 'g')
            
            soup.find(id='ingredients').append(_tag)
                
        
        with open(self.data['out'], 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
            
        self.webview.setUrl(QtCore.QUrl.fromLocalFile(str(self.data['out'])))
    

    @QtCore.Slot()
    def to_pdf(self):
        _date = self.data['date'].replace(':', ' ')
        _pdf_path = Path( Path.home(), 'MedIndex', f"{self.data['name']} {_date}.pdf" )
        _pdf_path.parent.mkdir(exist_ok=True)
        # print(_pdf_path)

        if not self.data['name']:
            _mb = QtWidgets.QMessageBox()
            _mb.setText('Please enter name')
            _mb.exec_()
            
            print('Cannot PDF: no name')
            self.reject()
        else:
            self.page = self.webview.page()
            self.page.printToPdf(str(_pdf_path))            
    
    @QtCore.Slot(str, bool)
    def printing_result(filePath, success):
        print('Location:', filePath, '\nStatus', success)
        self.reject()


        


