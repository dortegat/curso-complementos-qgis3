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
