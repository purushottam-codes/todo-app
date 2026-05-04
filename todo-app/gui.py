import functions
import FreeSimpleGUI as fsg
import time


# Choose a theme
fsg.theme("DarkBlue14")

# current_time = time.localtime()
# today = time.strftime("%A, %B %d, %Y", current_time)

#labels
clock_widget = fsg.Text("", key="clock")
label = fsg.Text("Type in a To-do")
input_box = fsg.InputText(tooltip="Type in a To-do", key="TODO")
list_box = fsg.Listbox(values=functions.get_todo(), key="todos_list",
                       enable_events=True, size=(50, 10))
#buttons
add_button = fsg.Button(key="Add",
    image_source="buttons_img/add.png",
    image_size=(32, 32),
    mouseover_colors="LightBlue2",
    tooltip="Add Task")
edit_button = fsg.Button(key="Edit",
    image_source="buttons_img/edit-button.png",
    image_size=(32, 32),
    mouseover_colors="LightBlue2",
    tooltip="Edit Task")
complete_button = fsg.Button( key="Complete",
    image_source="buttons_img/complete.png",
    image_size=(32, 32),
    mouseover_colors="LightBlue2",
    tooltip="Complete Task")
exit_button = fsg.Button(key="Exit",
    image_source="buttons_img/logout.png",
    image_size=(32, 32),
    mouseover_colors="LightBlue2",
    tooltip="Exit Application")

#display window
window = fsg.Window("My To-do App",
                    layout=[[clock_widget],
                            [label], [input_box], [add_button, edit_button, complete_button],
                            [list_box], [exit_button]],
                    font=("Open Sans", 13))
current_time = time.localtime()
while True:
    event, values = window.read(timeout=900)
    window["clock"].update(value=time.strftime("%Y-%m-%d %I:%M:%S %p"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            newTodo = values['TODO'] + "\n"
            todos.append(newTodo)
            functions.set_todo(todos)
            window["todos_list"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['TODO']
                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.set_todo(todos)
                window["todos_list"].update(values=todos)
            except IndexError:
                fsg.popup("Please Select an Item first.",title="Error", font=("Open Sans", 13))
        case "Complete":
            try:
                todos = functions.get_todo()
                todo_to_complete = values['todos_list'][0]
                todos.remove(todo_to_complete)
                functions.set_todo(todos)
                window["todos_list"].update(values=todos)
                window["TODO"].update(value="")
            except IndexError:
                fsg.popup("Please Select an Item first.", title="Error", font=("Open Sans", 13))
        case "todos_list":
            window["TODO"].update(value=values['todos_list'][0])
        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break

window.close()