import os.path
from UM.Application import Application
from UM.Extension import Extension
from UM.Resources import Resources


class ConicalSlicingExtension(Extension):
    def __init__(self):
        super().__init__()

        self.setMenuName("Conical Slicing")
        self.addMenuItem("Enter Parameters", self._showParameterEntryWindow)
        self._parameter_entry_window = None

        self._application = Application.getInstance()
        self._this_plugin_path = os.path.join()
    
    def _showParameterEntryWindow(self):
        if not self._parameter_entry_window:
            self._parameter_entry_window = self._createDialog("ParameterEntryWindow.qml")
        self._parameter_entry_window.show()
    
    def _createDialog(self, filename):
        filepath = os.path.join(self._this_plugin_path, "resources", "QML", filename)
        component = self._application.createQMLComponent(filepath, {"main": self})
        return component