import os
from rich.console import Console
from rich.prompt import Prompt
from create_folder import create_folder
from delete_user import delete_user
from sort_docs import sort_docs
from parse_logs import parse_logs
from reset import reset


def main():
    os.system('clear')
    console = Console()

    user_task = task_selection(console)

    if user_task == "1":
        create_folder(console)
        return True
    elif user_task == "2":
        delete_user(console)
        return True
    elif user_task == "3":
        sort_docs(console)
        return True
    elif user_task == "4":
        parse_logs(console)
        return True
    elif user_task == "5":
        reset(console)
        return True
    elif user_task.lower() == "q":
        console.print(f"\n[yellow]Quitting...[/yellow]")
        return False
    else:
        task_selection(console)


def task_selection(console):
    task_desc = {
        "1": "Create a folder",
        "2": "Delete a user",
        "3": "Sort documents",
        "4": "Parse logs",
        "5": "Reset folders for testing",
    }

    while True:
        console.print(f"[chartreuse3]Choose a task to perform:[/chartreuse3]")
        user_task = Prompt.ask(f"[cyan]1.[/cyan] {task_desc.get('1')}\n"
                               f"[cyan]2.[/cyan] {task_desc.get('2')}\n"
                               f"[cyan]3.[/cyan] {task_desc.get('3')}\n"
                               f"[cyan]4.[/cyan] {task_desc.get('4')}\n"
                               f"[cyan]5.[/cyan] {task_desc.get('5')}\n"
                               f"[cyan]Q.[/cyan] Quit\n\n"
                               f"Enter the # for your selection")

        if user_task in task_desc or user_task.lower() == "q":
            return user_task
        else:
            Prompt.ask(f"\n[yellow]{user_task}[/yellow], is not a valid entry. Enter [cyan]any[/cyan] key to try again")
            os.system('clear')


if __name__ == "__main__":
    loop = True
    while loop:
        loop = main()
    print("")
