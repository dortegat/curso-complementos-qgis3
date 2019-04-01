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