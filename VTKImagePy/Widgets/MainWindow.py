import os
import vtk

from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from Widgets.VtkVolumeWidget import VtkVolumeWidget


class MainWindow( QMainWindow ):
	
	def __init__( self ):
		super().__init__()
		self.setWindowTitle( 'VTKImagePy' )
		self.setWindowIcon( QIcon( 'Logo.png' ) )
		self.resize( 800, 600 )

		#MenuBar
		self.menuBar = self.menuBar()
		self.menuFile = self.menuBar.addMenu( 'File' )
		self.menuFilter = self.menuBar.addMenu( 'Filter' )
		self.menuSegment = self.menuBar.addMenu( 'Segment' )
		
		#Menu: File
		self.subActionRawData = QAction( 'Raw Data' )
		self.subActionRawData.triggered.connect( self.ImportRawData )

		self.subActionJpgSeries = QAction( 'Jpg Series' )
		self.subActionJpgSeries.triggered.connect( self.ImportJpgSeries )

		self.subActionPngSeries = QAction( 'Png Series' )
		self.subActionPngSeries.triggered.connect( self.ImportPngSeries )

		self.subActionDicomData = QAction( 'Dicom Data' )
		self.subActionDicomData.triggered.connect( self.ImportDicomData )

		self.subActionDicomSeries = QAction( 'Dicom Series' )
		self.subActionDicomSeries.triggered.connect( self.ImportDicomSeries )
		
		self.subMenuImport = QMenu( 'Import' )
		self.subMenuImport.addAction( self.subActionRawData )
		self.subMenuImport.addAction( self.subActionJpgSeries )
		self.subMenuImport.addAction( self.subActionPngSeries )
		self.subMenuImport.addAction( self.subActionDicomData )
		self.subMenuImport.addAction( self.subActionDicomSeries )

		self.actionExit = QAction( 'Exit' )
		self.actionExit.triggered.connect( self.close )

		self.menuFile.addMenu( self.subMenuImport )
		self.menuFile.addAction( self.actionExit )

		#Menu: Filter

		#Menu: Segment

		#Central Widget
		self.m_vtkVRWidget = VtkVolumeWidget()
		self.setCentralWidget( self.m_vtkVRWidget )
		pass

	def GetImageSeries( self ):
		dirImageSeries = QFileDialog.getExistingDirectory( self, '选取序列文件夹', '' )
		print( 'Image Data Path : ' + dirImageSeries )
		pngFiles = os.listdir( dirImageSeries )
		vtkStrArray = vtk.vtkStringArray()
		for pngFile in pngFiles:
			strFilePath = dirImageSeries + '/' + pngFile
			vtkStrArray.InsertNextValue( strFilePath )			
		return vtkStrArray

	def ImportRawData( self ):
		pass


	def ImportJpgSeries( self ):
		imgReader = vtk.vtkJPEGReader()
		imgReader.SetFileNames( self.GetImageSeries() )		
		imgReader.Update()
		self.m_vtkVRWidget.DisplayVolume( imgReader.GetOutputPort() )
		pass
		

	def ImportPngSeries( self ):
		pngReader = vtk.vtkPNGReader()
		pngReader.SetFileNames( self.GetImageSeries( '*.PNG'  ) )		
		pngReader.Update()
		self.m_vtkVRWidget.DisplayVolume( pngReader.GetOutputPort() )
		pass


	def ImportDicomData( self ):
		pass


	def ImportDicomSeries( self ):
		pass	