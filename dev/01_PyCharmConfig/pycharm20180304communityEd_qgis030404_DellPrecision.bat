:: PyCharm version: 2018.3.4 Community Edition
:: QGIS version: 3.4.4
:: PC: NausicaA
@echo off
SET QGIS_ROOT=C:\Program Files\QGIS 3.4
call "%QGIS_ROOT%"\bin\o4w_env.bat

@echo off
SET QGISNAME=qgis
path %PATH%;%QGIS_ROOT%\apps\%QGISNAME%\bin
path %PATH%;%QGIS_ROOT%\bin
path %PATH%;%QGIS_ROOT%\apps\Python37\Scripts

SET PYTHONPATH=%PYTHONPATH%;%QGIS_ROOT%\apps\%QGISNAME%\python
SET PYTHONHOME=%QGIS_ROOT%\apps\Python37

SET PYCHARM="C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.4\bin\pycharm.exe"
start "PyCharm aware of QGIS" /B %PYCHARM% %*