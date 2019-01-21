import sys
sys.path.append( '../' )

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QWidget, QGridLayout
import GlobalDef as gldef

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
		#self.TestDisplay()

		pass

	def DisplayVolume( self, vtk_image_data ):
		#Save vtk_image_data as global param
		gldefIndex = gldef.GetGlobalDefLen()
		gldef.SetValue( 0, vtk_image_data )

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
		
		vtk_volmapper = vtk.vtkSmartVolumeMapper()
		vtk_volmapper.SetInputData( vtk_image_data )

		vtk_volume = vtk.vtkVolume()
		vtk_volume.SetMapper( vtk_volmapper )
		vtk_volume.SetProperty( vtk_volproperty )
		
		self.vtk_renderer.AddVolume( vtk_volume )
		self.vtk_renderer.ResetCamera()
		self.vtk_render_win.Render()
		pass

	def TestDisplay( self ):
		#test
		src_sphere = vtk.vtkSphereSource()
		src_sphere.SetCenter( 0, 0, 0 )
		src_sphere.SetRadius( 5.0 )
		poly_mapper = vtk.vtkPolyDataMapper()
		poly_mapper.SetInputConnection( src_sphere.GetOutputPort() )
		poly_actor = vtk.vtkActor()
		poly_actor.SetMapper( poly_mapper )
		self.vtk_renderer.AddActor( poly_actor )
		self.vtk_renderer.ResetCamera()
		self.vtk_widget.Render()
		pass

