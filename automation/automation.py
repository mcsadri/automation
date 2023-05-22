import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from create_folder import create_folder
from delete_user import delete_user
from sort_docs import sort_docs
from parse_logs import parse_logs
from tbd import tbd
from reset import reset


def main():
    os.system('clear')
    console = Console()

    user_task = task_selection(console)

    if user_task == "1":
        create_folder(console)
    elif user_task == "2":
        delete_user(console)
    elif user_task == "3":
        sort_docs()
    elif user_task == "4":
        parse_logs()
    elif user_task == "5":
        tbd()
    elif user_task == "6":
        reset()
    else:
        task_selection(console)


def task_selection(console):
    task_desc = {
        "1": "Create a folder",
        "2": "Delete a user",
        "3": "Sort documents",
        "4": "Parse logs",
        "5": "TBD",
    }

    while True:
        console.print(f"[chartreuse3]Choose a task to perform:[/chartreuse3]")
        user_task = Prompt.ask(f"[cyan]1.[/cyan] {task_desc.get('1')}\n"
                               f"[cyan]2.[/cyan] {task_desc.get('2')}\n"
                               f"[cyan]3.[/cyan] {task_desc.get('3')}\n"
                               f"[cyan]4.[/cyan] {task_desc.get('4')}\n"
                               f"[cyan]5.[/cyan] {task_desc.get('5')}\n\n"
                               f"Enter the # for your selection")

        # task_confirm = Prompt.ask(f"\nYou selected: [yellow]{user_task}. {task_desc.get(user_task)}[/yellow]\nConfirm "
        #                           f"your choice ([cyan]Y[/cyan]es or [cyan]N[/cyan]o)")
        # if task_confirm.lower() == "y":
        #     return user_task
        # else:
        #     os.system('clear')

        return user_task


if __name__ == "__main__":
    main()
