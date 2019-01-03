from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QToolTip, QPushButton, QApplication, QLabel, QMenu, QToolButton, QToolBar
from Widgets.VtkVolumeWidget import VtkVolumeWidget


class MainWindow( QMainWindow ):
	
	def __init__( self ):
		super().__init__()
		self.setWindowTitle( 'MedicalImagePro' )
		self.resize( 800, 600 )
		self.InitWidget()
		pass

	def InitWidget( self ):
		self.vtkVRWidget = VtkVolumeWidget()
		self.setCentralWidget( self.vtkVRWidget )
		pass