import sys
sys.path.append( '../' )
sys.path.append( '../Filters' )

import vtk
import GlobalDef as gldef
from PyQt5.QtWidgets import QWidget, QGridLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

import VtkFilters as vtk_flt

class VtkVolumeWidget( QWidget ):
	def __init__( self ):
		super().__init__()
		self.vtk_widget = QVTKRenderWindowInteractor( self )
		self.main_layout = QGridLayout()
		self.main_layout.addWidget( self.vtk_widget )
		self.setLayout( self.main_layout )
		
		self.vtk_renderer = vtk.vtkRenderer()
		self.vtk_render_win = self.vtk_widget.GetRenderWindow()
		self.vtk_render_win.AddRenderer( self.vtk_renderer )
		self.vtk_interactor = self.vtk_render_win.GetInteractor()
		self.vtk_interactor.Initialize()

		self.vtk_volume_mapper = vtk.vtkSmartVolumeMapper()
		pass

	def DisplayVolume( self, vtk_image_data ):
		#Save vtk_image_data as global param
		gldefIndex = gldef.GetGlobalDefLen()
		gldef.SetValue( gldefIndex, vtk_image_data )

		#VolumeProperty: Opacity
		vtk_piecewisefunc = vtk.vtkPiecewiseFunction()
		vtk_piecewisefunc.AddPoint( 20, 0.0 )
		vtk_piecewisefunc.AddPoint( 255, 0.2 )

		#VolumeProperty: Color
		vtk_colortransfunc = vtk.vtkColorTransferFunction()
		vtk_colortransfunc.AddRGBPoint( 0.0, 0.0, 0.5, 0.0 )
		vtk_colortransfunc.AddRGBPoint( 60.0, 1.0, 0.0, 0.0 )
		vtk_colortransfunc.AddRGBPoint( 128.0, 0.2, 0.1, 0.9 )
		vtk_colortransfunc.AddRGBPoint( 196.0, 0.27, 0.21, 0.1 )
		vtk_colortransfunc.AddRGBPoint( 255.0, 0.8, 0.8, 0.8 )

		#VolumeProperty
		vtk_volproperty = vtk.vtkVolumeProperty()
		vtk_volproperty.SetColor( vtk_colortransfunc )
		vtk_volproperty.SetScalarOpacity( vtk_piecewisefunc )
		vtk_volproperty.ShadeOn()
		vtk_volproperty.SetInterpolationTypeToLinear()
		vtk_volproperty.SetAmbient( 0.2 )
		vtk_volproperty.SetDiffuse( 0.9 )
		vtk_volproperty.SetSpecular( 0.2 )
		vtk_volproperty.SetSpecularPower( 10 )
		
		self.vtk_volume_mapper.SetInputData( vtk_image_data )

		vtk_volume = vtk.vtkVolume()
		vtk_volume.SetMapper( self.vtk_volume_mapper )
		vtk_volume.SetProperty( vtk_volproperty )
		
		self.vtk_renderer.RemoveAllViewProps(); #Delete All Images
		self.vtk_renderer.AddVolume( vtk_volume )
		self.vtk_renderer.ResetCamera()
		self.vtk_render_win.Render()
		pass


	def GaussFilter( self ):
		vtk_image_data = self.vtk_volume_mapper.GetInput()
		vtk_image_data = vtk_flt.GaussFilter3D( vtk_image_data )
		self.vtk_volume_mapper.SetInputData( vtk_image_data )
		self.vtk_volume_mapper.Modified()
		pass

	def MedianFilter( self ):
		vtk_image_data = self.vtk_volume_mapper.GetInput()
		vtk_image_data = vtk_flt.MedianFilter3D( vtk_image_data )
		self.vtk_volume_mapper.SetInputData( vtk_image_data )
		self.vtk_volume_mapper.Modified()
		pass

	def ConvolveFilter( self ):
		vtk_image_data = self.vtk_volume_mapper.GetInput()
		vtk_image_data = vtk_flt.ConvolveFilter( vtk_image_data )
		self.vtk_volume_mapper.SetInputData( vtk_image_data )
		self.vtk_volume_mapper.Modified()
		pass

	def ThresholdSegment( self ):
		pass