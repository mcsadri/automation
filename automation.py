import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def main():
    os.system('clear')
    console = Console()

    user_task = task_selection(console)

    if user_task == "1":
        create_folder(console)
    elif user_task == "2":
        delete_user()
    elif user_task == "3":
        sort_docs()
    elif user_task == "4":
        parse_logs()
    else:
        task_selection(console)


def task_selection(console):
    task_desc = {
        "1": "Create a folder",
        "2": "Delete a user",
        "3": "Sort documents",
        "4": "Parse logs",
    }

    while True:
        console.print(f"[chartreuse3]Choose a task to perform:[/chartreuse3]")
        user_task = Prompt.ask(f"[cyan]1.[/cyan] {task_desc.get('1')}\n"
                               f"[cyan]2.[/cyan] {task_desc.get('2')}\n"
                               f"[cyan]3.[/cyan] {task_desc.get('3')}\n"
                               f"[cyan]4.[/cyan] {task_desc.get('4')}\n\n"
                               f"Enter the # for your selection")
        task_confirm = Prompt.ask(f"\nYou selected: [yellow]{user_task}. {task_desc.get(user_task)}[/yellow]\nConfirm "
                                  f"your choice ([cyan]Y[/cyan]es or [cyan]N[/cyan]o)")

        if task_confirm.lower() == "y":
            return user_task
        else:
            os.system('clear')


def create_folder(console):
    name_test = False
    folder_name = str()

    while not name_test:
        os.system('clear')
        folder_name = Prompt.ask("[chartreuse3]Make a new folder[/chartreuse3]\nWhat do you want to name your new "
                                 "folder?\n\nThe default name = [cyan]temp[/cyan]")
        if folder_name == "":
            folder_name = "temp"

        name_test = os.path.exists(folder_name)

        if name_test:
            Prompt.ask(f"\nThe name, [yellow]{folder_name}[/yellow], is already in use. Enter [cyan]any[/cyan] key to "
                       f"try again")
            print("pre name_test", name_test)
            name_test = False
            print("post name_test", name_test)
        else:
            folder_confirm = Prompt.ask(f"\nYou entered: [yellow]{folder_name}[/yellow]\nConfirm "
                                        f"your choice ([cyan]Y[/cyan]es or [cyan]N[/cyan]o)")
            if folder_confirm.lower() == "y":
                break

    try:
        os.mkdir(folder_name)
        if os.path.exists(folder_name):
            console.print(f"\nThe folder [yellow]{folder_name}[/yellow] has been created\n")
        else:
            print("\nelse Something did not work.\n")
    except OSError:
        print("\nexcept Something did not work.\n")


def delete_user():
    pass


def sort_docs():
    pass


def parse_logs():
    pass


def do_it_again():
    pass


if __name__ == "__main__":
    main()
