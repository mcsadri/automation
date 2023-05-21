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
        delete_user(console)
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


def create_folder(console, folder_name=str()):
    name_test = False

    if not folder_name:
        while not name_test:
            os.system('clear')
            folder_name = Prompt.ask("[chartreuse3]Make a new folder[/chartreuse3]\nWhat do you want to name your new "
                                     "folder?\n\nThe default name = [cyan]doodah[/cyan]")
            if folder_name == "":
                folder_name = "doodah"

            name_test = os.path.exists(folder_name)

            if name_test:
                Prompt.ask(f"\nThe name, [yellow]{folder_name}[/yellow], is already in use. Enter [cyan]any[/cyan] "
                           f"key to try again")
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

    else:
        try:
            os.mkdir(folder_name)
            if os.path.exists(folder_name):
                return True
            else:
                print("\nelse Something did not work.\n")
                return False
        except:
            print("\nexcept Something did not work.\n")
            return False


def delete_user(console):

    path = "./user-docs"
    user_to_del = str()
    user_path = str()

    while True:
        os.system('clear')
        console.print(f"[red]So you want to delete a user? Does that make you feel powerful?[/red]\n")

        users = sorted(os.listdir(path))
        table = Table(title=f"[cyan]All Users")
        table.add_column("Row")
        table.add_column("User Name")
        table.add_column("# of Files")
        for user in users:
            user_path = path + "/" + user
            table.add_row(str(users.index(user) + 1), user, str(len(os.listdir(user_path))))

        console.print(table)
        selected_row = Prompt.ask(f"\nWhich unforunate soul do you wish to delete?\nEnter the [cyan]row #[/cyan] to be deleted")
        if selected_row.isnumeric():
            selected_row = int(selected_row)
            if 0 < selected_row <= len(users):
                user_to_del = users[selected_row - 1]
                break
        else:
            Prompt.ask(f"\n[yellow]{selected_row}[/yellow], is not a valid entry. Enter [cyan]any[/cyan] key to try again")

    # create deleted_users folder if it doesn't already exist
    deleted_path = "deleted_users"
    name_test = os.path.exists(deleted_path)
    if not name_test:
        create_folder(console, deleted_path)

    # create the user folder for the deleted user in the deleted_users folder
    deleted_path = "deleted_users"
    name_test = os.path.exists(deleted_path + "/" + user_to_del)
    if not name_test:
        create_folder(console, deleted_path + "/" + user_to_del)

    # move the user files from user-docs to deleted-users
    user_path = path + "/" + user_to_del
    deleted_user_path = deleted_path + "/" + user_to_del
    user_files = os.listdir(user_path)
    for file in user_files:
        shutil.move(user_path + "/" + file, deleted_user_path + "/" + file)


def sort_docs():
    pass


def parse_logs():
    pass


def do_it_again():
    pass


if __name__ == "__main__":
    main()
