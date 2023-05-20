import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def main():
    os.system('clear')
    console = Console()

    user_task = task_selection(console)


def task_selection(console):
    task_desc= {
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
                               f"Enter the # for your selection:")

        user_confirm = Prompt.ask(f"\nYou selected: [yellow]{user_task}. {task_desc.get(user_task)}[/yellow]\nConfirm your choice ([cyan]Y[/cyan]es or [cyan]N[/cyan]o)")

        if user_confirm.lower() == "y":
            return user_task
        else:
            os.system('clear')


def create_folder():
    pass


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
