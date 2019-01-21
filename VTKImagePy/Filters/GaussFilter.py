import vtk

def GaussFilter2D(self, vtk_image_data ):
	vtk_gauss_filter2d = vtk.vtkImageGaussianSmooth()
	vtk_gauss_filter2d.SetInputData( vtk_image_data )
	vtk_gauss_filter2d.SetDimensionality( 2 )
	vtk_gauss_filter2d.SetRadiusFactor( 5 )
	vtk_gauss_filter2d.SetStandardDeviation( 3 )
	vtk_gauss_filter2d.Update()
	pass

def GaussFilter3D( self, vtk_image_data ):
	vtk_gauss_filter3d = vtk.vtkImageGaussianSmooth()
	vtk_gauss_filter3d.SetInputData( vtk_image_data )
	vtk_gauss_filter3d.SetDimensionality( 3 )
	vtk_gauss_filter3d.SetRadiusFactor( 5 )
	vtk_gauss_filter3d.SetStandardDeviation( 3 )
	vtk_gauss_filter3d.Update()
	pass