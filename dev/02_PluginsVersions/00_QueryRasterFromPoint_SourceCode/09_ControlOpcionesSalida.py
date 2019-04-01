"""
5.3.1.4	Controlando el comportamiento de opciones de salida
09_ControlOpcionesSalida ***********************************************************************************************
"""
# OJO!! en C:\dev_plugins\query_raster_from_point\query_raster_from_point_dockwidget.py

# a) añadir metodos
def push_memory_layer(self):
    """
    Disabled shp QLineEdit & QToolButton enabled memory layer QCheckBox when QRadioButton memory layer is clicked
    """
    self.lineEdit_pathOutputShp.setEnabled(False)
    self.toolButton_searchPathOutputShp.setEnabled(False)


def push_rb_shp(self):
    """
    Enabled shp QLineEdit & QToolButton, disabled memory layer QCheckBox when QRadioButton shp is clicked
    """
    self.lineEdit_pathOutputShp.setEnabled(True)
    self.toolButton_searchPathOutputShp.setEnabled(True)

# b) en el constructor metodo __init__ añadir sentencias de inicializacion
self.radioButton_outputMemoryLayer.setChecked(True)
self.lineEdit_pathOutputShp.setEnabled(False)
self.toolButton_searchPathOutputShp.setEnabled(False)