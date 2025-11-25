from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

# --------------------------
# Functions
# --------------------------
def remove_locked_attribute_keys(anim_curves):
    # logic
    return total_deleted

def remove_redundant_keys(anim_curves):
    # detect duplicate values
    return deleted

def reduce_keys(anim_curves, tolerance):
    # use cmds.filterCurve()
    return reduced

# --------------------------
# UI class
# --------------------------
class MayaToolUI(QWidget):

    def __init__(self, parent=None):
        super(MayaToolUI, self).__init__(parent)

        self.setWindowFlags(Qt.Window)

        # Set the object name     
        self.setObjectName('MayaToolUI_uniqueId')

        # Customize some window values
        self.setWindowTitle('Maya UI Tool')
        self.setGeometry(300, 300, 300, 300)

        # Add widgets to your window
        self.build_ui()
        self.connect_ui()

    def build_ui(self):
        pass

    def connect_ui(self):
        pass

    def action(self):
        pass

# --------------------------
# Helper to get Maya main window
# --------------------------
def get_main_window():
    ptr = omui.MQtUtil.mainWindow()
    maya_window = wrapInstance(int(ptr), QWidget)
    return maya_window

# --------------------------
# Launch tool
# --------------------------
maya_window = get_main_window()
tool = MayaToolUI(maya_window)
tool.show()
