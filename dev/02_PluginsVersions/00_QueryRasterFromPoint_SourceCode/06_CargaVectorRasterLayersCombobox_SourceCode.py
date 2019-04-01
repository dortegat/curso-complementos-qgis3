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
