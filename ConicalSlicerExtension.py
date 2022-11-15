import os.path
from UM.Application import Application
from UM.Extension import Extension
from UM.Logger import Logger
from UM.Resources import Resources


class ConicalSlicerExtension(Extension):

    def __init__(self):
        super().__init__()

        if ConicalSlicerExtension._instance is not None:
            Logger.log("w", "ConicalSlicerExtension object has already been instantiated")
        else:
            ConicalSlicerExtension._instance = self

        self.setMenuName("Conical Slicing")
        self.addMenuItem("Enter Parameters", self._showParameterEntryWindow)
        self._parameter_entry_window = None

        self._application = Application.getInstance()
        self._this_plugin_path = Resources.getStoragePath(Resources.Resources, "plugins", "ConicalSlicer", "ConicalSlicer")

        # slicing parameters
        self.conical_slicing_enabled = False
        self.cone_axis_coords = (0, 0)
        self.cone_tilt_angle = 0
        
    def _showParameterEntryWindow(self):
        """
        show the parameter entry window
        """
        if not self._parameter_entry_window:
            self._parameter_entry_window = self._createDialog("ParameterEntryWindow.qml")
        self._parameter_entry_window.show()

    def _createDialog(self, filename):
        """
        create qml component from specified file. assumes qml file is in the resources\qml folder
        """
        filepath = os.path.join(self._this_plugin_path, "resources", "qml", filename)
        component = self._application.createQmlComponent(filepath, {"main": self})
        return component

    _instance = None

    @classmethod
    def getInstance(cls):
        return cls._instance