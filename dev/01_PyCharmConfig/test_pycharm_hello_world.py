from qgis.core import QgsApplication
from PyQt5.QtWidgets import QDialog

GUIEnabled=True
app = QgsApplication([], GUIEnabled)

dlg = QDialog()
dlg.exec_()

app.exit(app.exec_())