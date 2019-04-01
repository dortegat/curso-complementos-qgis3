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