import os
from rich.prompt import Prompt


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

    return
