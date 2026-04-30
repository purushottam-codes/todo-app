import functions
import FreeSimpleGUI as fsg

lable = fsg.Text("Type in a To-do")
input_box = fsg.InputText(tooltip="Type in a To-do")
add_button = fsg.Button("Add")

window = fsg.Window("My To-do App", layout=[[lable],[input_box, add_button]])
window.read()
window.close()