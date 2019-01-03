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
		self.UpdateImage()

		pass

	def SetImageData( self ):

		pass

	def UpdateImage( self ):
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









