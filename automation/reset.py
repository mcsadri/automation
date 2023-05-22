import os
import shutil
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def reset(console):
    # delete default folder created by create_folder
    try:
        shutil.rmtree("doodah")
    except:
        pass

    # delete user-docs folder
    try:
        shutil.rmtree("user-docs")
    except:
        pass

    # re-populate user-docs folder from backup
    try:
        shutil.copytree("./assets/user-docs", "./user-docs")
    except:
        pass

    # delete deleted-users folder
    try:
        shutil.rmtree("deleted-users")
    except:
        pass