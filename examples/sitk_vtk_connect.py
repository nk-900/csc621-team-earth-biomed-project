import SimpleITK as sitk
import vtk
from vtk.util.numpy_support import numpy_to_vtk

def sitk_to_vtk(image):
    if image.GetDimension() != 3:
        raise ValueError("Expected 3D image")

    if image.GetNumberOfComponentsPerPixel() != 1:
        raise ValueError("Expected a scalar image")

    array = sitk.GetArrayFromImage(image)

    scalars = numpy_to_vtk(
        array.ravel(order="C"),
        deep=True
    )

    vtk_image = vtk.vtkImageData()

    vtk_image.SetDimensions(image.GetSize())
    vtk_image.SetSpacing(image.GetSpacing())
    vtk_image.SetOrigin(image.GetOrigin())
    vtk_image.SetDirectionMatrix(*image.GetDirection())
    vtk_image.GetPointData().SetScalars(scalars)

    return vtk_image
