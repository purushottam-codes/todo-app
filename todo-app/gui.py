import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-do")
input_box = fsg.InputText(tooltip="Type in a To-do", key="TODO")
add_button = fsg.Button("Add")

window = fsg.Window("My To-do App", layout=[[label], [input_box, add_button]],
                    font=("Open Sans", 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            newTodo = values['TODO'] + "\n"
            todos.append(newTodo)
            functions.set_todo(todos)
        case fsg.WIN_CLOSED:
            break

window.close()