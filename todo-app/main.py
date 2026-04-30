import functions
action_prompt_text = """
----------------------------------------------------------------------------------
Add - add a new task
View - view the task list in format [task_id. Task]
Edit - edit a task by entering the task_id
Complete - complete the task by entering the task_id
Exit - exit the program
----------------------------------------------------------------------------------
"""
user_prompt = "Enter your task: "


while True:
    action = input(action_prompt_text).strip().lower()

    if action.startswith("view") or action.startswith("show"):
        print("\nShowing the tasks:")
        # file = open("todos.txt", "r")
        # tasks = file.readlines()
        # file.close()
        # copying the items from file to remove the extra lines while viewing
        # new_tasks = []
        # for task in tasks:
        #     task = task.strip('\n')
        #     new_tasks.append(task)
        # list comprehension ex:
        # new_tasks = [item.strip('\n') for item in tasks]
        tasks = functions.get_todo()
        if not tasks:
            print("the task list is empty.")
        else:
            for index, item in enumerate(tasks, start=1):
                item = item.strip('\n')
                print(f"{index}. the Task is '{item}'")

    elif action.startswith("add"):
        task = action[4:].strip() + "\n"
        # file = open("todos.txt", "r")
        # tasks = file.readlines()
        # file.close()
        # task_text = input(user_prompt).strip() + "\n"
        tasks = functions.get_todo()
        tasks.append(task)
        functions.set_todo(tasks)
        # file = open("todos.txt", "w")
        # file.writelines(tasks)
        # file.close()

    elif action.startswith("edit"):
        # file = open("todos.txt", "r")
        # tasks = file.readlines()
        # file.close()
        tasks = functions.get_todo()
        if not tasks:
            print("the task list is empty.")
        else:
            try:
                number = int(action[5:])
                number -= 1
            except ValueError:
                print("the edit option is invalid.")
                print("Hint: edit task_id")
                continue
            new_todo = input("Enter the new ToDo: ")
            tasks[number] = new_todo + "\n"
            functions.set_todo(tasks)
            print("Done editing, you can choose option view to see the changes...")

    elif action.startswith("complete"):
        # print("\nCompleting your tasks:")
        try:
            index_num = int(action[9:])
            index_num -= 1
            print(index_num)
        except ValueError:
            print("the Complete option is invalid.")
            print("Hint: complete task_id")
            continue

        tasks = functions.get_todo()

        if not tasks:
            print("the task list is empty.")
        try:
            if tasks[index_num]:
                task = tasks.pop(index_num)
                print("\nThe task is '" + task + "'" + "has been completed.")
                functions.set_todo(tasks)
        except IndexError:
            print("the task id to complete is not valid.")
            print("Hint: complete task_id")
            continue

    elif action.startswith("exit"):
        break
    else:
        print("\nHey enter a valid option.")

print("Bye !!!")
