"""
5.3.1.1	Añadir nombres de capas vectoriales y raster de la ToC de QGIS en los desplegables
06_CargaVectorRasterLayersCombobox *************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) import PyQGIS classes
from qgis.core import QgsProject, QgsMapLayer, QgsWkbTypes

# b) codigo nuevo metodos
def load_vectors(self):
    """
    Load vectors for QGIS table of contents
    """
    self.dockwidget.comboBox_vectorLayer.clear()
    self.dockwidget.comboBox_vectorLayer.addItem(self.tr("--- Select vector layer ---"))
    for layer in QgsProject.instance().mapLayers().values():
        if layer.type() == QgsMapLayer.VectorLayer:
            if layer.geometryType() == QgsWkbTypes.PointGeometry:
                self.dockwidget.comboBox_vectorLayer.addItem(layer.name())

def load_rasters(self):
    """
    Load monoband rasters for QGIS table of contents
    """
    self.dockwidget.comboBox_rasterLayer.clear()
    self.dockwidget.comboBox_rasterLayer.addItem(self.tr("--- Select raster layer ---"))
    for layer in QgsProject.instance().mapLayers().values():
        if layer.type() == QgsMapLayer.RasterLayer:
            self.dockwidget.comboBox_rasterLayer.addItem(layer.name())

# c) añadir sentencias en el metodo run()
self.load_vectors()
self.load_rasters()

"""
5.3.1.2	Botones de acción abrir capas vectoriales y raster existentes
07_OpenVectorRasterLayers **********************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) añadir en seccion imports
from PyQt5.QtWidgets import QAction, QFileDialog


# b) añadir metodos
def open_vector(self):
    """
    Open vector from file dialog
    """
    str_in_file, str_filter = QFileDialog.getOpenFileName(caption=self.tr("Open shapefile"),
                                                          filter="Shapefiles (*.shp)")
    if len(str_in_file) > 0:
        str_name_layer = str.split(os.path.basename(str_in_file), ".")[0]
        self.iface.addVectorLayer(str_in_file,
                                  str_name_layer,
                                  "ogr")
        self.load_vectors()

def open_raster(self):
    """
    Open raster from file dialog
    """
    str_in_file, str_filter = QFileDialog.getOpenFileName(caption=self.tr("Open raster"),
                                                          filter="GeoTiff (*.tif)")
    if len(str_in_file) > 0:
        str_name_layer = str.split(os.path.basename(str_in_file), ".")[0]
        self.iface.addRasterLayer(str_in_file,
                                  str_name_layer)
        self.load_rasters()

# c) self toolButton connections en el metodo run()
self.dockwidget.toolButton_searchVectorLayer.clicked.connect(self.open_vector)
self.dockwidget.toolButton_searchRasterLayer.clicked.connect(self.open_raster)

"""
5.3.1.3	Botón de acción para seleccionar shapefile de salida
08_BuscaRutaShpSalida **************************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) añadir nuevo metodo
def search_path_output_shp(self):
    """
    Search path output shapefile
    """
    str_path_output_shp, str_filter = QFileDialog.getSaveFileName(caption=self.tr("Search path output shapefile"),
                                                                  filter="Shapefiles (*.shp)")
    if len(str_path_output_shp) > 0:
        self.dockwidget.lineEdit_pathOutputShp.setText(str_path_output_shp)
    else:
        self.dockwidget.lineEdit_pathOutputShp.clear()

# b) añadir signal/slot connection en el metodo run()
self.dockwidget.toolButton_searchPathOutputShp.clicked.connect(self.search_path_output_shp)

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

"""
5.3.3.1	Constantes en Python
11_RefactoringConstantes ***********************************************************************************************
"""

# a) crear nuevo fichero C:\dev_plugins\query_raster_from_point\constants.py con el siguiente contenido
# -*- coding: utf-8 -*-

# general constants
APPLICATION_NAME = u'Query Raster From Point'
APPLICATION_VERSION = "0.1"

# output directory and filenames
STR_NAME_MEMORY_LAYER = "New memory layer"
STR_NEW_VRASTER_FIELDNAME = "v_raster"

# b) import en el modulo que corresponda, en este caso C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# Import self classes and modules
from .constants import *


# c) Buscar los TODO y reemplazar

# d) Añadir en C:\dev_plugins\query_raster_from_point\pb_tool.cfg
# Other files required for the plugin
extras: metadata.txt icon.png constants.py


"""
5.3.3.2	Comunicación con el usuario
12_ComunicacionUsuario *************************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) añadir nuevas classes necesarias para el procesamiento en la seccion de imports

from qgis.gui import QgsMessageBar

from qgis.core import QgsProject, QgsMapLayer, QgsWkbTypes, QgsField, QgsVectorLayer, QgsRaster, QgsVectorFileWriter, Qgis

# b) reemplazar los TODO restantes

self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                    self.tr('Select vector layer'),
                                    Qgis.MessageLevel.Critical,
                                    10)

self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                    self.tr('Select raster layer'),
                                    Qgis.MessageLevel.Critical,
                                    10)

self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                    self.tr('Select path output shapefile'),
                                    Qgis.MessageLevel.Critical,
                                    10)

"""
5.3.3.3	Fix a bug
13_FixBug **************************************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) los return devolveran siempre un booleano False y al final un True

# b) en el metodo get_raster_values_from_vector_layer cambiar la parte final
if msg[0] == QgsVectorFileWriter.WriterError.NoError:
    data_source = self.str_path_output_shp
    layer_name = str.split(os.path.basename(str(self.str_path_output_shp)), ".")[0]
    provider_name = "ogr"
    self.iface.addVectorLayer(data_source,
                              layer_name,
                              provider_name)
else:
    self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                        msg[1],
                                        Qgis.MessageLevel.Critical,
                                        10)

# c) modificar el metodo process
def process(self):
    """
    Controls processing execution
    """
    if self.get_ui_parameters():
        self.get_raster_values_from_vector_layer()

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

"""
5.3.3.5	Qsettings
15_QSettings ***********************************************************************************************************
"""
# a) Crear directorio y fichero C:\dev_plugins\query_raster_from_point\template\qsettings.ini con el siguiente contenido
[General]
default_path_output_directory_shapefile=c:\\temporalc\\queryrasterfromvector_output

# b) En C:\dev_plugins\query_raster_from_point\pb_tool.cfg añadir
# These must be subdirectories under the plugin directory
extra_dirs: icons template

# c) En el constructor de la clase QueryRasterFromPoint, metodo __init__, añadir

# qsettings configuration
path_ini_file_qsettings = self.plugin_dir + '/template/qsettings.ini'
self.my_qsettings = QSettings(path_ini_file_qsettings,
                              QSettings.IniFormat)

# d) reemplazar el metodo siguiente
def search_path_output_shp(self):
    """
    Search path output shapefile
    """
    current_qsettings_directory = os.path.normcase(self.my_qsettings.value("default_path_output_directory_shapefile"))
    str_path_output_shp, str_filter = QFileDialog.getSaveFileName(caption=self.tr("Search path output shapefile"),
                                                                  directory=current_qsettings_directory,
                                                                  filter="Shapefiles (*.shp)")
    if len(str_path_output_shp) > 0:
        self.dockwidget.lineEdit_pathOutputShp.setText(str_path_output_shp)
        # update qsettings.ini
        new_directory = os.path.normcase(os.path.dirname(str_path_output_shp))
        if new_directory != current_qsettings_directory:
            self.my_qsettings.setValue("default_path_output_directory_shapefile",
                                       new_directory)
    else:
        self.dockwidget.lineEdit_pathOutputShp.clear()

"""
5.3.3.6	Mejoras del procesamiento
16_MejorasProcesamiento ************************************************************************************************
"""
# C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# a) 1ra mejora en el metodo load_raster
if layer.type() == QgsMapLayer.RasterLayer and layer.bandCount() == 1

# b) 2da mejora en el metodo get_raster_values_from_vector_layer
# compare CRS vector layer vs CRS raster layer
raster_crs = self.qgs_raster_layer.crs()  # get CRS source raster layer
if source_vl_crs != raster_crs:
    self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                        self.tr("Vector layer and raster layer have different CRSs"),
                                        Qgis.MessageLevel.Critical,
                                        10)
    return False

# c) 3ra mejora en el metodo get_raster_values_from_vector_layer
return + booleano en sentencias finales

# d) cambiar sentencias finales metodo process
def process(self):
    """
    Controls processing execution
    """
    if self.get_ui_parameters():
        if self.dockwidget.checkBox_removePreviousProcessing.isChecked():
            self.remove_previous_memory_layer()
        if self.get_raster_values_from_vector_layer():
            self.iface.messageBar().pushMessage(APPLICATION_NAME + " v." + APPLICATION_VERSION,
                                                self.tr('Processing completed successfully'),
                                                Qgis.MessageLevel.Info,
                                                10)

"""
5.3.3.7	Internacionalizacion
17_Traduccion **********************************************************************************************************
"""
# a) Copiar ficheros query_raster_from_point.pro y query_raster_from_point_es.ts
# a directorio C:\dev_plugins\query_raster_from_point\i18n

# b) Desde consola de Osgeo pasamos de .pro a .ts
cd C:\dev_plugins\query_raster_from_point\i18n
call qt5_env.bat
call py3_env.bat
Pylupdate5 -noobsolete query_raster_from_point.pro

# c) Desde Qt Linguist paso de .ts a .qm

# d) Copiar fichero query_raster_from_point_es.qm a la raiz del plugin

# e) En C:\dev_plugins\query_raster_from_point\pb_tool.cfg añadir
# Other files required for the plugin
extras: metadata.txt icon.png constants.py query_raster_from_point_es.qm

# f) En el metodo __init__ de C:\dev_plugins\query_raster_from_point\query_raster_from_point.py
# initialize locale
locale = QSettings().value('locale/userLocale')[0:2]
locale_path = os.path.join(
    self.plugin_dir,
    'query_raster_from_point_es.qm'.format(locale))