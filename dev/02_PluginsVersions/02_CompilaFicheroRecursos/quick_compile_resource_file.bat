SET OSGEO4W_ROOT=C:\Program Files\QGIS 3.4
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
cd C:\dev_plugins\query_raster_from_point
call qt5_env.bat
call py3_env.bat
pyrcc5 -o resources.py resources.qrc