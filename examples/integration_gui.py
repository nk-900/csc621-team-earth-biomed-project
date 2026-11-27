import SimpleITK as sitk

from fltk import Fl, Fl_Window, Fl_Button, Fl_Box
from integration_hello import create_image, visualize


# for the project, replace 'create_image()' with sitk.ReadImage("<image location>")
original_image = create_image()
segmented_image = None


def show_original(widget):
    visualize(original_image)


def segment_image(widget):
    global segmented_image

    segmented_image = sitk.BinaryThreshold(
        original_image,
        lowerThreshold=100,
        upperThreshold=255,
        insideValue=255,
        outsideValue=0
    )

    status.label("Segmentation complete")
    status.redraw()


def show_segmentation(widget):
    if segmented_image is not None:
        visualize(segmented_image)
    else:
        status.label("Run segmentation first")
        status.redraw()


def exit_app(widget):
    window.hide()


# GUI
window = Fl_Window(400, 340, "Biomedical Imaging")
window.begin()

status = Fl_Box(20, 10, 360, 40, "Image ready")

original_button = Fl_Button(
    50, 60, 300, 45, "View Original Image"
)
original_button.callback(show_original)

segment_button = Fl_Button(
    50, 115, 300, 45, "Run Segmentation"
)
segment_button.callback(segment_image)

result_button = Fl_Button(
    50, 170, 300, 45, "View Segmentation"
)
result_button.callback(show_segmentation)

exit_button = Fl_Button(
    50, 250, 300, 45, "Exit"
)
exit_button.callback(exit_app)

window.end()
window.show()

Fl.run()