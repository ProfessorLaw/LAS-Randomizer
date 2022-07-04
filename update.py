from PyQt6 import QtCore
import urllib.request as lib
import urllib.error as urlERROR


currentVersion = 0.144



class UpdateProcess(QtCore.QThread):
    
    canUpdate = QtCore.pyqtSignal(bool)
    
    
    # initialize
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    
    
    def run(self):
        try:
            updateFile = lib.urlopen("https://raw.githubusercontent.com/OSmart32/LAS-Randomizer/master/version.txt")
            webVersion = float(updateFile.read())
            
            if webVersion > currentVersion:
                self.canUpdate.emit(True)
            else:
                self.canUpdate.emit(False)
        
        except urlERROR.URLError: # when users use this app while not connected to the internet
            self.canUpdate.emit(False)
