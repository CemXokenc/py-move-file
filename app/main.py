import os


def move_file(command: str) -> None:

    try:
        operation, file_old, file_new = command.split(" ")
    except ValueError:
        return

    if operation != "mv":
        return

    path = ""

    for dir_name in file_new.split("/")[:-1]:
        path = os.path.join(path, dir_name)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    with open(file_old, "r") as old_file, open(file_new, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(file_old)
