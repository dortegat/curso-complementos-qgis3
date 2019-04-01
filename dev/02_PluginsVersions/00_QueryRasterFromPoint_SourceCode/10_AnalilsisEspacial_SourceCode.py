"""
5.3.2	Operaciones de análisis espacial
10_AnalilsisEspacial ***************************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) Crear signal/slot connection tootButton process
self.dockwidget.toolButton_process.clicked.connect(self.process)

# 5.3.2.1	Obtención de la información necesaria para el procesamiento

# b) Nuevo metodo para controlar el procesamiento
def process(self):
    """
    Controls processing execution
    """
    self.get_ui_parameters()
    self.get_raster_values_from_vector_layer()

# c) añadir nuevos metodos
def get_vector_layer(self):
    """
    Gets vector layer specified in combo box
    """
    layer = None
    layername = self.dockwidget.comboBox_vectorLayer.currentText()
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == layername:
            layer = lyr
            break
    return layer

def get_raster_layer(self):
    """
    Gets raster layer specified in combo box
    """
    layer = None
    layername = self.dockwidget.comboBox_rasterLayer.currentText()
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == layername:
            layer = lyr
            break
    return layer

# d) añadir nuevos para recopilar parametros de la ui
def get_ui_parameters(self):
    """
    Get and set all variables from UI
    """
    # get QgsVectorLayer from comboBox
    if self.dockwidget.comboBox_vectorLayer.currentIndex() == 0:
        # TODO: msg
        return
    self.qgs_vector_layer = self.get_vector_layer()

    # get QgsRasterLayer from comboBox
    if self.dockwidget.comboBox_rasterLayer.currentIndex() == 0:
        # TODO: msg
        return
    self.qgs_raster_layer = self.get_raster_layer()

    # get path output shapefile from lineEdit
    if self.dockwidget.radioButton_outputShapefile.isChecked():
        self.str_path_output_shp = self.dockwidget.lineEdit_pathOutputShp.text()
        if len(self.str_path_output_shp) == 0:
            # TODO: msg
            return

# 5.3.2.2	Implementación del procesamiento

# e) añadir nuevas classes necesarias para el procesamiento en la seccion de imports
# import PyQt5 classes
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt, QVariant

# import PyQGIS classes
from qgis.core import QgsProject, QgsMapLayer, QgsWkbTypes, QgsField, QgsVectorLayer, QgsRaster, QgsVectorFileWriter

# f) añadir metodo principal de procesamiento
def get_raster_values_from_vector_layer(self):
    """
    Brief: Obtains raster layer values from point vector layer. Create memory layer or shapefile with source layer
            fields, adding new field with obtained raster value. Finally, add layer result in QGIS
    """
    # create target datamodel (fields)
    source_fields = self.qgs_vector_layer.fields()  # get QgsFields source vector layer
    str_new_fieldname = "v_raster"  # TODO: value raster, pass to constant file
    new_qgsfield = QgsField(str_new_fieldname,
                            QVariant.Double)  # new QgsField to add
    source_fields.append(new_qgsfield)  # append new QgsField to QgsFields vector source layer

    # create new vector memory layer
    source_crs = self.qgs_vector_layer.crs()  # get CRS source vector layer
    wkt_source_crs = source_crs.toWkt()  # get CRS WKT string

    str_name_memory_layer = "New memory layer"  # TODO: name memory layer, pass to constant file

    data_source = "Point?crs=" + wkt_source_crs
    layer_name = str_name_memory_layer
    provider_name = "memory"
    memory_layer = QgsVectorLayer(data_source,
                                  layer_name,
                                  provider_name)

    # add source layer fields to new memory layer
    pr_memory_layer = memory_layer.dataProvider()
    pr_memory_layer.addAttributes(source_fields)  # add datamodel to memory layer
    memory_layer.updateFields()  # tell the vector layer to fetch changes from the provider

    # add source features to new memory layer
    for feature in self.qgs_vector_layer.getFeatures():
        pr_memory_layer.addFeatures([feature])

    # gets raster value of each point in vector layer and updates the corresponding attribute in target memory layer
    memory_layer.startEditing()
    for feature in memory_layer.getFeatures():
        qgs_raster_id_result = self.qgs_raster_layer.dataProvider().identify(feature.geometry().asPoint(),
                                                                             QgsRaster.IdentifyFormatValue)
        dict_value_raster = qgs_raster_id_result.results()
        feature.setAttribute(str_new_fieldname,
                             dict_value_raster[1])
        memory_layer.updateFeature(feature)
    memory_layer.commitChanges()

    if self.dockwidget.radioButton_outputMemoryLayer.isChecked():
        QgsProject.instance().addMapLayer(memory_layer)

    if self.dockwidget.radioButton_outputShapefile.isChecked():
        # Save memory layer to file
        msg = QgsVectorFileWriter.writeAsVectorFormat(memory_layer,
                                                      self.str_path_output_shp,
                                                      "CP1250",
                                                      source_crs,
                                                      "ESRI Shapefile")
        if msg[0] == 0:  # If not error in write as vector format, add new shapefile in QGIS
            data_source = self.str_path_output_shp
            layer_name =str.split(os.path.basename(str(self.str_path_output_shp)), ".")[0]
            provider_name = "ogr"
            self.iface.addVectorLayer(data_source,
                                      layer_name,
                                      provider_name)
        else:
            print(msg)