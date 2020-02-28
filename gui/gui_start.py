import sys
import os
from bs4 import BeautifulSoup
from pathlib import Path

from datetime import datetime
from PySide2 import QtWebEngineWidgets
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from PySide2.QtCore import Qt

from medindex.gui.mainwindow import Ui_MainWindow
from medindex.gui.spinboxdelegate import SpinBoxDelegate
from medindex.gui.exportdialog import ExportDialog
from medindex.gui.intablemodel import InTableModel
from medindex.gui.sidetablemodel import SideTableModel
from medindex.gui.outtablemodel import OutTableModel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, my_paths):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.my_paths = my_paths
        
        self.in_table_model = InTableModel(self)
        self.out_table_model = OutTableModel(self)
        self.side_table_model = SideTableModel(self)
        
        self.set_up()
        self.info_from_template()
    
    
    # fill main window user inputs with info from template
    def info_from_template(self):
        with open(self.my_paths['template'], 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, features='lxml')
            self.doctor.setText(soup.find(id='doctor-name').string)
            self.organisation.setText(soup.find(id='clinic').string)
            self.instruction_for_meds.setText(soup.find(id='instruction').string)

    # general stuff
    def set_up(self):
        self.setWindowTitle('MedIndex')

        # stuff
        self.patient_name_edit.setPlaceholderText('Some Body')
        self.patient_sex.addItems(['Male', 'Female'])
        self.instruction_for_meds.setPlaceholderText('Just Do it!')

        self.btn_patient.clicked.connect(lambda : self.side_table_model.set_patient(self.patient_name_edit.text()))
        self.patient_name_edit.returnPressed.connect(self.btn_patient.click)
        
        # search_bar
        self.search_bar.textChanged.connect(self.in_table_model.search)
        def search_bar_to_in_table():
            self.in_table_view.setFocus()
            self.in_table_view.selectRow(0)
        self.search_bar.returnPressed.connect(search_bar_to_in_table)
        
        # in_table
        setattr(self.in_table_view, 'parent_receiver', self.event_receiver)
        self.in_table_view.setModel(self.in_table_model)
        self.in_table_view.verticalHeader().hide()

        self.in_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.in_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.in_table_view.resizeColumnsToContents()
        
        self.in_table_view.activated.connect(self.in_table_model.get_row)
        self.in_table_model.shove_dict.connect(self.out_table_model.pull_dict)
        self.in_table_model.shove_dict.connect(self.out_table_view.resizeColumnsToContents)
        
        # out_table
        setattr(self.out_table_view, 'parent_receiver', self.event_receiver)
        self.out_table_view.setModel(self.out_table_model)
        self.out_table_view.verticalHeader().hide()
        
        self.out_table_view.resizeColumnsToContents()
        self.out_table_model.layoutChanged.connect(self.out_table_view.resizeColumnsToContents)
        
        self.out_table_view.setItemDelegate(SpinBoxDelegate(self))
 
        # side_table
        self.side_table_view.setModel(self.side_table_model)
        self.side_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.side_table_view.resizeColumnsToContents()
        self.side_table_model.layoutChanged.connect(self.side_table_view.resizeColumnsToContents)
        self.side_table_view.activated.connect(self.side_table_model.get_row)
        self.side_table_model.shove_dict.connect(self.out_table_model.pull_dict)
        self.side_table_model.shove_dict.connect(self.out_table_view.resizeColumnsToContents)

        # btn_export
        self.btn_export.clicked.connect(self.export)

    def event_receiver(self, sender, key, keyboard_modifier=None, data=None):
        
        # Future: use signals
        if sender == self.search_bar:
            self.in_table_view.setFocus()
        
        elif sender == self.in_table_view:
            if key == Qt.Key_Return and keyboard_modifier == Qt.ShiftModifier:
                self.search_bar.setFocus()
                self.search_bar.selectAll()
            else:
                print('yes query')
        
        # Future: move this part to view
        elif sender == self.out_table_view:
            if key == Qt.Key_Backspace and keyboard_modifier == Qt.NoModifier:
                print('out: backspace')
                _rows = list(
                    map(
                        QtCore.QModelIndex.row, 
                        self.out_table_view.selectedIndexes()
                        )
                    )
                _rows = sorted(list(set(_rows)))
                self.out_table_model.remove_rows(_rows)
                self.out_table_view.selectRow(self.out_table_model.rowCount()-1)

    @QtCore.Slot()
    def export(self):
        _out_data_1 = self.out_table_model.out_data()
        _now = datetime.now()
        
        data_pack = {
            'clinic': self.organisation.text(),
            'name': self.patient_name_edit.text(),
            'age': self.patient_age.value(),
            'sex': self.patient_sex.currentText(),
            'date': '{} {}:{:02}'.format(_now.date(), _now.hour, _now.minute),
            'shots': self.shots_of_meds.value(),
            'ingredients': _out_data_1,
            'instruction' : self.instruction_for_meds.toPlainText(),
            'doctor-name': self.doctor.text(),
            'template': self.my_paths['template'],
            'out': self.my_paths['out']
            }

        print(data_pack)
            
        _rv = ExportDialog(data_pack, self).exec_()

        if not _rv:
            return
        else:
            db = QtSql.QSqlDatabase.database('medindex')
            db.open()
            _query = QtSql.QSqlQuery(db)
            
            # tbl_patient
            _query.prepare("""\
                SELECT patient_id FROM tbl_patient WHERE name = (?)
                """)
            _query.bindValue(0, data_pack['name'])
            _query.exec_()

            if _query.next():
                _patient_id = _query.value(0)
                print(f"'{data_pack['name']}' exist in patient database")
            else:
                _patient_id = None
                print(f"Adding '{data_pack['name']}' to patient database")
                _dob = '{}-01-01'.format(datetime.now().year - data_pack['age'])
                
                _query.prepare("""\
                    INSERT INTO tbl_patient VALUES (?, ?, ?, ?)
                    """)
                _query.bindValue(0, _patient_id)
                _query.bindValue(1, data_pack['name'])
                _query.bindValue(2, _dob)
                _query.bindValue(3, data_pack['sex'][0])

                if _query.exec_():
                    print("Successful add '{}' to patient database".format(data_pack['name']))
                else:
                    print("Failed to add '{}' to patient database".format(data_pack['name']))
                    return
            
            # tbl_doctor
            _query.prepare("""\
                SELECT doctor_id FROM tbl_doctor WHERE name = (?)
                """)
            _query.bindValue(0, data_pack['doctor-name'])
            _query.exec_()

            if _query.next():
                _doctor_id = _query.value(0)
                print(f"'{data_pack['doctor-name']}' exist in doctor database")
            else:
                _doctor_id = None
                print(f"Adding '{data_pack['doctor-name']}' to doctor database")
                
                _query.prepare("""\
                    INSERT INTO tbl_doctor VALUES (?, ?)
                    """)
                _query.bindValue(0, _doctor_id)
                _query.bindValue(1, data_pack['doctor-name'])

                if _query.exec_():
                    print("Successful add '{}' to doctor database".format(data_pack['doctor-name']))
                else:
                    print("Failed to add '{}' to doctor database".format(data_pack['doctor-name']))
                    return
            
            
            # tbl_script
            # get doctor id... again...
            _query.prepare("""SELECT doctor_id FROM tbl_doctor WHERE name = (?) """)
            _query.bindValue(0, data_pack['doctor-name'])
            _query.exec_()

            if _query.next():
                _doctor_id = _query.value(0)
                
            # get patient id... again...
            _query.prepare("""SELECT patient_id FROM tbl_patient WHERE name = (?) """)
            _query.bindValue(0, data_pack['name'])
            _query.exec_()

            if _query.next():
                _patient_id = _query.value(0)

            # the real thing...
            _query.prepare("""\
                INSERT INTO tbl_script VALUES (?, ?, ?, ?, ?)
                """)
            _query.bindValue(0, None)
            _query.bindValue(1, int(_patient_id))
            _query.bindValue(2, int(_doctor_id))
            _query.bindValue(3, data_pack['date'])
            _query.bindValue(4, data_pack['shots'])
            
            for _ in _query.boundValues().values():
                print(_)
            
            if _query.exec_():
                print("Successful add '{}' to script database".format(data_pack['date']))
            else:
                print("Failed to add '{}' to script database".format(data_pack['date']))
                return
            
            # tbl_script_item
            # get patient id... again...
            _query.prepare("""SELECT script_id FROM tbl_script ORDER BY script_id DESC """)
            _query.exec_()

            if _query.next():
                _script_id = _query.value(0)
            
            for _x in data_pack['ingredients']:
                _query.prepare("""\
                    INSERT INTO tbl_script_item VALUES (?, ?, ?)
                    """)
                _query.bindValue(0, _script_id)
                _query.bindValue(1, _x['med_id'])
                _query.bindValue(2, _x['mass'])

                if _query.exec_():
                    print("Successful add '{}' to med database".format(_x['med_id']))
                else:
                    print("Failed to add '{}' to med database".format(_x['med_id']))
                    return
                

            db.close()
            pass

        
        
        
        
        
        
        
        
"""  """
def run(my_paths=None):
    # 
    db1 = QtSql.QSqlDatabase.addDatabase('QSQLITE', 'medindex')
    db1.setDatabaseName(my_paths['db'])
    
    db2 = QtSql.QSqlDatabase.addDatabase('QSQLITE', 'memo')
    db2.setDatabaseName(':memory:')
    
    # 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(my_paths)
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    run()