from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from PySide2.QtCore import Qt

class SideTableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super(SideTableView, self).__init__(parent)
        
        self.entered.connect(self.resizeColumnsToContents)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and event.modifiers() == Qt.NoModifier:
        
            _rows = list(map(QtCore.QModelIndex.row, self.selectedIndexes()))
            _rows = sorted(list(set(_rows)))

            for _r in _rows:
                self.model().get_row(_r)
            print(_rows)
    
    # might be overkill...
    def enterEvent(self, event):
        self.resizeColumnsToContents()
        super(SideTableView, self).enterEvent(event)
        