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