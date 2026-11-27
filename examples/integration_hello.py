import SimpleITK as sitk
import vtk

from sitk_vtk_connect import sitk_to_vtk


def create_image():
    return sitk.GaussianSource(
        outputPixelType=sitk.sitkFloat32,
        size=[128, 128, 128],
        sigma=[20, 20, 20],
        mean=[64, 64, 64],
        scale=255
    )


def visualize(image):
    vtk_image = sitk_to_vtk(image)

    viewer = vtk.vtkImageViewer2()
    viewer.SetInputData(vtk_image)

    # Display the middle axial slice
    viewer.SetSliceOrientationToXY()
    viewer.SetSlice(image.GetSize()[2] // 2)

    # Intensity display settings
    viewer.SetColorWindow(255)
    viewer.SetColorLevel(127.5)

    interactor = vtk.vtkRenderWindowInteractor()
    viewer.SetupInteractor(interactor)

    window = viewer.GetRenderWindow()
    window.SetWindowName("SimpleITK + VTK")
    window.SetSize(600, 600)

    viewer.GetRenderer().ResetCamera()

    interactor.Initialize()
    viewer.Render()
    interactor.Start()


if __name__ == "__main__":
    image = create_image()
    visualize(image)