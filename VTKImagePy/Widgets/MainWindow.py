from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from Widgets.VtkVolumeWidget import VtkVolumeWidget
import vtk
import os

class MainWindow( QMainWindow ):
	
	def __init__( self ):
		super().__init__()
		self.setWindowTitle( 'VTKImagePy' )
		self.setWindowIcon( QIcon( 'Logo.png' ) )
		self.resize( 800, 600 )

		#MenuBar
		self.m_menuBar = self.menuBar()
		self.m_menuFile = self.m_menuBar.addMenu( '&File' )
		
		#SubMenu: import
		self.m_subActionRawData = QAction( 'Raw Data' )
		self.m_subActionRawData.triggered.connect( self.ImportRawData )

		self.m_subActionJpgSeries = QAction( 'Jpg Series' )
		self.m_subActionJpgSeries.triggered.connect( self.ImportJpgSeries )

		self.m_subActionPngSeries = QAction( 'Png Series' )
		self.m_subActionPngSeries.triggered.connect( self.ImportPngSeries )

		self.m_subActionDicomData = QAction( 'Dicom Data' )
		self.m_subActionDicomData.triggered.connect( self.ImportDicomData )

		self.m_subActionDicomSeries = QAction( 'Dicom Series' )
		self.m_subActionDicomSeries.triggered.connect( self.ImportDicomSeries )
		
		self.m_subMenuImport = QMenu( 'Import' )
		self.m_subMenuImport.addAction( self.m_subActionRawData )
		self.m_subMenuImport.addAction( self.m_subActionJpgSeries )
		self.m_subMenuImport.addAction( self.m_subActionPngSeries )
		self.m_subMenuImport.addAction( self.m_subActionDicomData )
		self.m_subMenuImport.addAction( self.m_subActionDicomSeries )

		self.m_actionExit = QAction( 'Exit' )
		self.m_actionExit.triggered.connect( self.close )

		self.m_menuFile.addMenu( self.m_subMenuImport )
		self.m_menuFile.addAction( self.m_actionExit )

		#Central Widget
		self.vtkVRWidget = VtkVolumeWidget()
		self.setCentralWidget( self.vtkVRWidget )
		pass


	def ImportRawData( self ):
		pass


	def ImportJpgSeries( self ):
		pass
		

	def ImportPngSeries( self ):
		dirPngSeries = QFileDialog.getExistingDirectory( self, "选取Png序列文件夹", "" )
		print( dirPngSeries )
		pngFiles = os.listdir( dirPngSeries )
		strArray = vtk.vtkStringArray()
		for pngFi in pngFiles:
			strArray.InsertNextValue( pngFi )
			pass

		pngReader = vtk.vtkPNGReader()
		pngReader.SetFileNames( strArray )		

		print( pngFiles )

		pass


	def ImportDicomData( self ):
		pass


	def ImportDicomSeries( self ):
		pass	