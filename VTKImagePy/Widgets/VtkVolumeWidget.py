import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QWidget, QGridLayout

class VtkVolumeWidget( QWidget ):
	def __init__( self ):
		super().__init__()
		self.m_vtkWidget = QVTKRenderWindowInteractor( self )
		self.m_layoutMain = QGridLayout()
		self.m_layoutMain.addWidget( self.m_vtkWidget )
		self.setLayout( self.m_layoutMain )
		
		self.m_vtkRender = vtk.vtkRenderer()
		self.m_vtkRenderWin = self.m_vtkWidget.GetRenderWindow()
		self.m_vtkRenderWin.AddRenderer( self.m_vtkRender )
		self.m_vtkInteractor = self.m_vtkRenderWin.GetInteractor()
		self.m_vtkInteractor.Initialize()
		#self.TestDisplay()

		pass

	def DisplayVolume( self, vtkOutput ):

		vtkPiecewiseFunc = vtk.vtkPiecewiseFunction()
		vtkPiecewiseFunc.AddPoint( 20, 0.0 )
		vtkPiecewiseFunc.AddPoint( 255, 0.2 )

		vtkColorTransFunc = vtk.vtkColorTransferFunction()
		vtkColorTransFunc.AddRGBPoint( 0.0, 0.0, 0.5, 0.0 )
		vtkColorTransFunc.AddRGBPoint( 60.0, 1.0, 0.0, 0.0 )
		vtkColorTransFunc.AddRGBPoint( 128.0, 0.2, 0.1, 0.9 )
		vtkColorTransFunc.AddRGBPoint( 196.0, 0.27, 0.21, 0.1 )
		vtkColorTransFunc.AddRGBPoint( 255.0, 0.8, 0.8, 0.8 )

		vtkVolProperty = vtk.vtkVolumeProperty()
		vtkVolProperty.SetColor( vtkColorTransFunc )
		vtkVolProperty.SetScalarOpacity( vtkPiecewiseFunc )
		vtkVolProperty.ShadeOn()
		vtkVolProperty.SetInterpolationTypeToLinear()
		vtkVolProperty.SetAmbient( 0.2 )
		vtkVolProperty.SetDiffuse( 0.9 )
		vtkVolProperty.SetSpecular( 0.2 )
		vtkVolProperty.SetSpecularPower( 10 )
		
		vtkVolMapper = vtk.vtkSmartVolumeMapper()
		vtkVolMapper.SetInputConnection( vtkOutput )

		vtkVol = vtk.vtkVolume()
		vtkVol.SetMapper( vtkVolMapper )
		vtkVol.SetProperty( vtkVolProperty )
		
		self.m_vtkRender.AddVolume( vtkVol )
		self.m_vtkRender.ResetCamera()
		self.m_vtkRenderWin.Render()
		pass

	def TestDisplay( self ):
		#test
		srcSphere = vtk.vtkSphereSource()
		srcSphere.SetCenter( 0, 0, 0 )
		srcSphere.SetRadius( 5.0 )
		polyMapper = vtk.vtkPolyDataMapper()
		polyMapper.SetInputConnection( srcSphere.GetOutputPort() )
		polyActor = vtk.vtkActor()
		polyActor.SetMapper( polyMapper )
		self.m_vtkRender.AddActor( polyActor )
		self.m_vtkRender.ResetCamera()
		self.m_vtkWidget.Render()
		pass

