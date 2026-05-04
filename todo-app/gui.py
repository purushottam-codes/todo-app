import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-do")
input_box = fsg.InputText(tooltip="Type in a To-do", key="TODO")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todo(), key="todos_list",
                       enable_events=True, size=(60, 10))
edit_button = fsg.Button("Edit")
cmplt_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")
window = fsg.Window("My To-do App",
                    layout=[[label], [input_box], [add_button, edit_button, cmplt_button],
                            [list_box], [exit_button]],
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
            window["todos_list"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['TODO']
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.set_todo(todos)
            window["todos_list"].update(values=todos)
        case "Complete":
            todos = functions.get_todo()
            todo_to_complete = values['todos_list'][0]
            todos.remove(todo_to_complete)
            functions.set_todo(todos)
            window["todos_list"].update(values=todos)
            window["TODO"].update(value="")
        case "todos_list":
            window["TODO"].update(value=values['todos_list'][0])
        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break

window.close()