from PySide2 import QtWidgets, QtCore, QtGui, QtSql
from PySide2.QtCore import Qt

class OutTableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super(OutTableView, self).__init__(parent)
        self.parent_receiver = None
        
    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Backspace and event.modifiers() == Qt.NoModifier:
                self.parent_receiver(self, event.key(), keyboard_modifier=event.modifiers(), data=None)
            else:
                super(OutTableView, self).keyPressEvent(event)