import os


def move_file(command: str) -> None:

    operation, file_old, file_new = command.split(" ")

    if operation == "mv":
        path = ""

        for dir_name in file_new.split("/")[:-1]:
            try:
                os.mkdir(path + dir_name)
            except FileExistsError:
                pass
            path += dir_name + "/"

        old_file = open(file_old, "r")
        new_file = open(file_new, "w")

        new_file.write(old_file.read())
        old_file.close()
        os.remove(file_old)
