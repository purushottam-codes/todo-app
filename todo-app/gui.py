import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-do")
input_box = fsg.InputText(tooltip="Type in a To-do", key="TODO")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todo(), key="todos_list",
                       enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")

window = fsg.Window("My To-do App",
                    layout=[[label], [input_box], [add_button, edit_button], [list_box]],
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
            window["todos_list"].update(todos)
        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['TODO']
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.set_todo(todos)
            window["todos_list"].update(todos)
        case "todos_list":
            window["TODO"].update(values['todos_list'][0])
        case fsg.WIN_CLOSED:
            break

window.close()