import shutil
from rich.prompt import Prompt


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

    Prompt.ask(f"\nThe folders have been reset for testing. Enter [cyan]any[/cyan] key to return to menu")
