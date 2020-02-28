from PySide2 import QtWebEngineWidgets
from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from PySide2.QtCore import Qt

class OutTableModel(QtSql.QSqlTableModel):
    def __init__(self, parent=None):
        super(OutTableModel, self).__init__(parent)
        self.setEditStrategy(self.OnFieldChange)
        
        self.db = QtSql.QSqlDatabase.database('memo')
        self.db.open()
        self._query = QtSql.QSqlQuery(self.db)
        self.setTable('tbl_memo')
        
        self._heads = ['ID', 'FN1', 'MASS', 'PRICE']
        self._fields = ['med_id', 'f_name_1', 'mass', 'price']
        
        # 
        self.create_db()
        
        self.refresh()
        
    def __del__(self):
        print('freeing memory db')
        self.db.close()
        
    def refresh(self):
        self._query.exec_('SELECT * FROM tbl_memo')
        self.setQuery(self._query)
        
    def create_db(self):
        self._query.prepare("""\
            CREATE TABLE tbl_memo (
                med_id INTEGER NOT NULL UNIQUE,
                f_name_1 TEXT NOT NULL,
                mass REAL NOT NULL default 0,
                price REAL NOT NULL
            )
        """)
        self._query.exec_()
        
    def flags(self, index):
        if index.isValid() and index.column() == 2:
            # return Qt.ItemIsEnabled
            return super(OutTableModel, self).flags(index) | Qt.ItemIsEditable | Qt.ItemIsEnabled

        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
    
    def setData(self, index, value, role=Qt.EditRole):
        if  index.isValid() and index.column() == 2:
            self._query.prepare("""\
                UPDATE tbl_memo 
                SET mass = (?)
                WHERE med_id = (?)
                """)
            id_ = self.record(index.row()).value(0)
            self._query.bindValue(0, value)
            self._query.bindValue(1, id_)
            self._query.exec_()
            self.refresh()
            return True
        
        return False

    @QtCore.Slot(list)
    def remove_rows(self, rows):
        rows.sort(reverse=True)
        print('deleting:', rows)
        for row in rows:
            id_ = self.record(row).value('med_id')
            self._query.prepare("""\
                DELETE FROM tbl_memo WHERE med_id = (?)
                """)
            self._query.bindValue(0, id_)
            self._query.exec_()
            
        self.refresh()
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal and 0 <= section <= len(self._heads):
                return self._heads[section]
            else:
                return None        
    
    @QtCore.Slot(dict)
    def pull_dict(self, row=None):
        if not row:
            return
        # from in_table, does not have mass
        if 'mass' not in row:
            row['mass'] = 1.0
        self._query.prepare("""\
            INSERT INTO tbl_memo VALUES (?, ?, ?, ?)
            """)
        for i, field in enumerate(self._fields):
            self._query.bindValue(i, row[field])
            
        self._query.exec_()
        
        self.refresh()
    
    def out_data(self):
        _ol = []
        self._query.exec_("SELECT * FROM tbl_memo")
        while self._query.next():
            _dic = {}
            for i, v in enumerate(self._fields):
                _dic[v] = self._query.record().value(v)

            _ol.append(_dic)
            
        return(_ol)
