from fltk import Fl, Fl_Window, Fl_Box, Fl_Button

#Create window
window = Fl_Window(400, 250, "FLTK - Hello World")
window.begin()

#Create text widget
label = Fl_Box(20, 40, 360, 100, "Hello, World!")
label.labelsize(30)

#Create button
button = Fl_Button(150, 170, 100, 40, "Exit")

#Define button behavior
def exit_callback(widget):
    window.hide()

button.callback(exit_callback)

#Finalize window
window.end()
window.show()

#Start event loop
Fl.run()