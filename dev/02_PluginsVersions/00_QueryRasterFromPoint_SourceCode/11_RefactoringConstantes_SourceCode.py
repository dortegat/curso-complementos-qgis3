"""
5.3.3.1	Constantes en Python
11_RefactoringConstantes ***********************************************************************************************
"""

# a) crear nuevo fichero C:\dev_plugins\query_raster_from_point\constants.py con el siguiente contenido
# -*- coding: utf-8 -*-

# general constants
APPLICATION_NAME = u'Query Raster From Point'
APPLICATION_VERSION = "0.1"

# output directory and filenames
STR_NAME_MEMORY_LAYER = "New memory layer"
STR_NEW_VRASTER_FIELDNAME = "v_raster"

# b) import en el modulo que corresponda, en este caso C:\dev_plugins\query_raster_from_point\query_raster_from_point.py

# Import self classes and modules
from .constants import *


# c) Buscar los TODO y reemplazar

# d) Añadir en C:\dev_plugins\query_raster_from_point\pb_tool.cfg
# Other files required for the plugin
extras: metadata.txt icon.png constants.py