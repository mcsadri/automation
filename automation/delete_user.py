import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from create_folder import create_folder


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