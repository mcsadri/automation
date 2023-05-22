import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from delete_user import print_users_table
from create_folder import create_folder


def sort_docs(console):

    users_path = "./user-docs"
    user_path = str()


    os.system('clear')
    console.print(f"Let's sort from files. For fun and profit.\n")

    users = sorted(os.listdir(users_path))

    # for user in users:
    #     for root, dirs, files in os.walk(users_path + "/" + user):
    #         # Print all folder names
    #         # for dir_name in dirs:
    #         #     print(os.path.join(root, dir_name))
    #
    #         # Print all file names
    #         for file_name in files:
    #             print(os.path.join(root, file_name))
    #         print("")

    for user in users:
        dir_list = os.listdir(users_path + "/" + user)

        print(dir_list)
        print("")

    # print_users_table(console, users, users_path)

    Prompt.ask("waiting")
