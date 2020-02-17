import sys
import os
from bs4 import BeautifulSoup
from pathlib import Path
from PySide2 import QtWidgets
from PySide2 import QtWebEngineWidgets
from PySide2 import QtWidgets, QtCore, QtGui
from mainwindow import Ui_MainWindow
from datetime import datetime
from medstore import MedStore

class WebView(QtWidgets.QDialog):
    def __init__(self, data, template_path, out_path):
        super(WebView, self).__init__()
        
        view = QtWebEngineWidgets.QWebEngineView(None)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(view)
        self.setLayout(layout)
        
        self.setFixedSize(595*1.3, 842*1.1)
        view.setZoomFactor(1.2)
        
        # 
        with open(template_path, 'r') as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'lxml')
            
            # set stuff
            soup.find(id='name').string = '{} ({})'.format(
                data['patient name'], data['patient age'])
            now = datetime.now()
            # Can be replaced with date.strftime() 
            soup.find(id='date').string = '{}/{}/{}/ {:#02d}:{}:{:#02d}'.format(
                now.year, now.month, now.day, now.hour, now.minute, now.second
            )
            soup.find(id='sex').string = data['patient sex']
            soup.find(id='days').string = data['days']
            soup.find(id='doctor-name').string = data['doctor']
            
            # Fill ingredients
            for _x in data['ingredients']:
                _tag = soup.new_tag('div', **{'class': 'ingredient'})
                _tag.string = '{} {} g'.format(_x[0], _x[1])
                
                soup.find(id='ingredients').append(_tag)
                
        # write file
        with open(out_path, 'w') as f:
            f.write(soup.prettify(formatter='html5'))
            
        # Load
        view.load(QtCore.QUrl.fromLocalFile(str(out_path)) )
        
        print('done export')



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, my_paths):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.set_in_table(my_paths['db'])
        self.set_out_table()
        self.set_search_bar()
        self.set_add_button()
        self.set_export_btn(my_paths['template'], my_paths['out'])
        
    def set_in_table(self, db_path):
        self.db = MedStore(db_path, 'tbl_meds')
        self.in_data = self.db.get_everything()
        
        # Set Columns
        self.column_names = [
            'ID', 'Short Form', 'Custom Name', 'Full Name', 'Price'
            ]
        self.in_table.setColumnCount(len(self.column_names))
        self.in_table.setHorizontalHeaderLabels(self.column_names)
        
        # Set Rows
        self.in_table.setRowCount(self.db.nrows)

        # Disable edit option
        self.in_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.update_in_table()
        
        self.in_table.resizeColumnsToContents()
        
        # Set Signals
        self.in_table.cellActivated.connect(self.add_to_out_table)
    
    def add_to_out_table(self, row, col):
        # Do Not add 'empty' item
        if self.in_table.item(0, 0).text() == '':
            return None
        
        # Do Not add existing item
        for i in range(self.out_table.rowCount()):
            if self.in_table.item(row, 0).text() == self.out_table.item(i, 0).text():
                return None
        
        _last_row = self.out_table.rowCount()
        self.out_table.insertRow(_last_row)

        self.out_table.setItem(_last_row, 0, self.in_table.item(row, 0).clone())
        self.out_table.setItem(_last_row, 1, self.in_table.item(row, 3).clone())
        self.out_table.setItem(_last_row, 2, QtWidgets.QTableWidgetItem('1'))
        self.out_table.setItem(_last_row, 3, self.in_table.item(row, 4).clone())
        
        self.out_table.resizeColumnsToContents()
        
        self.search_bar.clear()
        self.search_bar.setFocus()

    def update_in_table(self):
        # Remove previous content
        for row in range(self.in_table.rowCount()):
            self.in_table.removeRow(0)

        # Set Row Count
        self.in_table.setRowCount(len(self.in_data))
        
        # Fill in content
        for i, v1 in enumerate(self.in_data):
            for j, v2 in enumerate(v1):
                self.in_table.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(v2))
                    )
        pass
    
    def set_out_table(self):
        # Label Columns
        out_table_columns = ['ID', 'Full Name', 'Amount (g)', 'Price']
        self.out_table.setColumnCount(len(out_table_columns))
        self.out_table.setHorizontalHeaderLabels(out_table_columns)
        # 
        
        # Disable edit option
        self.out_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Slots
        # For out table only
        def on_cell_clicked(row, col):
            if col == 2:
                self.out_table.editItem(self.out_table.item(row, col))
            else:
                self.out_table.removeRow(row)
        
        
        # Signals
        self.out_table.cellActivated.connect(on_cell_clicked)
        
    def set_search_bar(self):
        
        # Slot
        def on_search_change(search_string):
            self.in_data = self.db.search(search_string)
  
            # Modify in_table
            self.update_in_table()
        
        # Signal
        self.search_bar.textChanged.connect(on_search_change)
        
    def set_add_button(self):
        self.add_button.clicked.connect(lambda: self.add_to_out_table(0, 0))
        pass
        
    def set_export_btn(self, template_path, out_path):
        self.btn_export.clicked.connect(lambda: self.export(template_path, out_path))
    
    def export(self, template_path, out_path):
        # Prepare data
        
        ingredients = []
        for i in range(self.out_table.rowCount()):
            ingredients.append((
                self.out_table.item(i, 1).text(), 
                float(self.out_table.item(i, 2).text()),
                float(self.out_table.item(i, 3).text()))
                )
        
        data = {
            'patient name': self.patient_name.text(),
            'patient age': self.patient_age.text(),
            'patient sex': self.patient_sex.currentText(),
            'days': self.days_of_meds.text(),
            'doctor': self.doctor_name.text(),
            'ingredients': ingredients
        }
        
        # web view
        web_view = WebView(data, template_path, out_path)
        rv = web_view.exec_()
        if not rv:
            os.remove(out_path)
        
        
        
"""  """
def main(my_paths):
    # 
    
    # 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(my_paths)
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()