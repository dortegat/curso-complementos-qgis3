"""
5.3.3.4	Eliminación de resultados de procesamientos anteriores
14_EliminaProcesamientosAnteriores *************************************************************************************
"""
# OJO! se actua sobre 3 modulos

# a) crear nuevo metodo en C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

def remove_previous_memory_layer(self):
    """
    Remove previous results
    """
    layers = QgsProject.instance().mapLayers().values()
    for layer in layers:
        layer_name = layer.name()
        if layer_name == str.split(os.path.basename(STR_NAME_MEMORY_LAYER), ".")[0]:
            layer_id = layer.id()
            QgsProject.instance().removeMapLayer(layer_id)
            break
# b) modificar C:\dev_plugins\query_raster_from_point\query_raster_from_point_dockwidget_base.ui
# añadiendo un nuevo checkBox_removePreviousProcessing

# c) En C:\dev_plugins\query_raster_from_point\query_raster_from_point_dockwidget.py añadir estas sentencias
    def push_memory_layer(self):
        """
        Disabled shp QLineEdit & QToolButton enabled memory layer QCheckBox when QRadioButton memory layer is clicked
        """
        self.checkBox_removePreviousProcessing.setEnabled(True)

    def push_rb_shp(self):
        """
        Enabled shp QLineEdit & QToolButton, disabled memory layer QCheckBox when QRadioButton shp is clicked
        """
        self.checkBox_removePreviousProcessing.setEnabled(False)

# d) cambiar metodo process de C:\dev_plugins\query_raster_from_point\query_raster_from_point.py
def process(self):
    """
    Controls processing execution
    """
    if self.get_ui_parameters():
        if self.dockwidget.checkBox_removePreviousProcessing.isChecked():
            self.remove_previous_memory_layer()
        self.get_raster_values_from_vector_layer()