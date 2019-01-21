import sys
sys.path.append( './Widgets' )
sys.path.append( '../Filters' )

import os
import vtk

from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon

from VtkVolumeWidget import VtkVolumeWidget
import GlobalDef as gldef
from GaussFilter import *


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
		self.subActionGaussFilter = QAction( 'Gauss Filter' )
		self.subActionGaussFilter.triggered.connect( self.GaussFilter )

		self.menuFilter.addAction( self.subActionGaussFilter )
		#Menu: Segment

		#Central Widget
		self.vtk_VR_widget = VtkVolumeWidget()
		self.setCentralWidget( self.vtk_VR_widget )
		pass

	def GetImageSeries( self ):
		dirImageSeries = QFileDialog.getExistingDirectory( self, '选取序列文件夹' )
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
		self.vtk_VR_widget.DisplayVolume( imgReader.GetOutput() )
		pass
		

	def ImportPngSeries( self ):
		pngReader = vtk.vtkPNGReader()
		pngReader.SetFileNames( self.GetImageSeries() )		
		pngReader.Update()
		self.vtk_VR_widget.DisplayVolume( pngReader.GetOutput() )
		pass


	def ImportDicomData( self ):
		pass


	def ImportDicomSeries( self ):
		pass	

	def GaussFilter( self ):
		if gldef.GetGlobalDefLen() > 0:
			vtk_image_data = gldef.GetValue( 0 )
			if None != vtk_image_data:
				GaussFilter3D( vtk_image_data )
		pass