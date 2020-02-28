import sys
from PySide2 import QtWidgets
from PySide2 import QtCore, QtSql
from PySide2.QtCore import Qt

class SideTableModel(QtSql.QSqlQueryModel):
    shove_dict = QtCore.Signal(dict)
    def __init__(self, parent=None):
        super(SideTableModel, self).__init__(parent)
        self._heads = ['Date', 'id', 'FN1', 'mass(g)', 'price', 'shot']
        
        self._fields = ['created_at', 'med_id', 'f_name_1', 'mass',  'price', 'shot']

        self.patient_name = None
        self.created_at_s = []

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal and (0 <= section < len(self._heads)):
                return self._heads[section]
            else:
                return None
    
    @QtCore.Slot(str)
    def set_patient(self, name):
        self.patient_name = name
        self.patient_id = None
        self.created_at_s = []
        print(self.patient_name)
        # self.created_at_s = None
        
        db = QtSql.QSqlDatabase.database('medindex')
        db.open()
        _query = QtSql.QSqlQuery(db)
        
        # get patient id
        _query.prepare("""\
            SELECT patient_id
            FROM tbl_patient
            WHERE name = (?)
            """)
        _query.bindValue(0, self.patient_name)
        _query.exec_()
        _query.first()
        self.patient_id = _query.value(0)
        if not self.patient_id:
            return
        print('patient id:', self.patient_id)
        

        # get available dates
        _query.prepare("""\
            SELECT
                created_at
            FROM
                tbl_script
            INNER JOIN 
                tbl_patient
            ON 
                tbl_script.patient_id = tbl_patient.patient_id
            WHERE 
                tbl_patient.name = (?)
            ORDER BY
                created_at DESC
            """)
        _query.bindValue(0, self.patient_name)
        _query.exec_()
        
        while _query.next():
            self.created_at_s.append(_query.value(0))
        
        print(self.created_at_s)

        # get script
        _query.prepare("\
            select\
                tbl_script.created_at,\
                tbl_script_item.med_id,\
                tbl_med.f_name_1,\
                tbl_script_item.mass,\
                tbl_med.price,\
                tbl_script.shot\
            from tbl_script\
            LEFT JOIN tbl_script_item ON tbl_script.script_id = tbl_script_item.script_id\
            LEFT JOIN tbl_med ON tbl_script_item.med_id = tbl_med.med_id\
            WHERE\
                tbl_script.patient_id = (?) and tbl_script.created_at = (?)\
            ")
        _query.bindValue(0, self.patient_id)
        _query.bindValue(1, self.created_at_s[0])
        _query.exec_()
        
        while _query.next():
            print([_query.value(_) for _ in self._fields])
            
        self.setQuery(_query)
        
        db.close()
    
    def pre(self):
        db = QtSql.QSqlDatabase.database('medindex')
        db.open()
        _query = QtSql.QSqlQuery(db)
        _query.exec_("")

        self.setQuery(_query)

        db.close()


    # Future: rewrite this to bulk emit/selection
    @QtCore.Slot(QtCore.QModelIndex)
    def get_row(self, index):
        db = QtSql.QSqlDatabase.database('medindex')
        db.open()
        _od = {}
        
        if type(index) == QtCore.QModelIndex:
            row = index.row()
        elif type(index) == int:
            row = index
        else:
            print('Error at side model get row')
        
        _od['med_id'] = self.record(row).value('med_id')
        _od['f_name_1'] = self.record(row).value('f_name_1')
        _od['mass'] = self.record(row).value('mass')
        _od['price'] = self.record(row).value('price')


        # print('row from side:', _od)
        
        db.close()
        self.shove_dict.emit(_od)