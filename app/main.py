import os


def move_file(command: str) -> None:

    try:
        operation, file_old, file_new = command.split()
    except ValueError:
        return

    if operation != "mv":
        return

    if file_new.endswith("/"):
        file_new = os.path.join(file_new, os.path.basename(file_old))

    directory = os.path.dirname(file_new)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_old, "r") as old_file, open(file_new, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(file_old)
