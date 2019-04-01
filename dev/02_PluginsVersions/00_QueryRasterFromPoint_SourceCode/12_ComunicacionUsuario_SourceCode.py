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