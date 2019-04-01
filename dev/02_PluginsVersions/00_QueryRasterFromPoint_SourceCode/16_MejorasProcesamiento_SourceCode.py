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