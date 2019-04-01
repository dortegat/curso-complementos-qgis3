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