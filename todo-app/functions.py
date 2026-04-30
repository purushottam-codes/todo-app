# getter and setter functions for the file
def get_todo(filepath="todos.txt"):
    """
    Checks the todo doc file and returns the todos if it exists
    :return: a list of the todos
    """
    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos

def set_todo(todos_arg, filepath="todos.txt"):
    """
    Writes to the todo doc file
    :param todos_arg: list of the todos
    :param filepath: file path of the todos file
    :return: None
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
    return None

if __name__ == "__main__":
    print("Hello, from the Functions module")
    print(get_todo())