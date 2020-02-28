import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import Qt


class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(SpinBoxDelegate, self).__init__(parent)
        
        
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(1000)
        return editor

    def setEditorData(self, editor, index):
        _v = index.model().data(index)
        editor.setValue(float(_v))
        pass
    
    def setModelData(self, editor, model, index):
        _v = float(editor.value())
        model.setData(index, _v, Qt.EditRole)
        pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        pass
    