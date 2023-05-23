# LAB - Class 19

## Project: Automation

## Author: Manuch Sadri

### Overview

An introduction to automation and organization using Python. Your team is working on a project to improve the organization and automation of various tasks. This includes handling user data, sorting files, parsing logs, and other miscellaneous tasks. You'll be writing Python scripts to automate these tasks and make your team's work more efficient.

### Feature Tasks and Requirements

- [X] Automate the creation of a folder.
  - [X] Write a Python script to create a new folder with a specified name.

- [X] Handle a deleted user.
  - [X] `user2` is a deleted user and need to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.

- [ ] Sort documents into appropriate folders.
  - [ ] Go through a given folder and sort the documents into additional folders based on their file type.
    - [ ] Move log files into a `logs` folder. If a `logs` folder doesn't exist, your script should create one.
    - [ ] Move email files into a `mail` folder. If a `mail` folder doesn't exist, your script should create one.

- [ ] Parse a log file for errors and warnings.
  - [ ] From the previous task, you've moved a log file into the `logs` folder. Now, parse the log file for errors and warnings and create two separate log files in a target directory:
    - [ ] `errors.log`: Contains all error messages.
    - [ ] `warnings.log`: Contains all warning messages.

- [X] Create a menu-driven application.
  - [X] Give the user a list of automation tasks (1-4) and let them choose one to execute. Customize your application by incorporating an additional automation task, choose one:
    - [ ] Counting the number of specific file types in a directory.
    - [ ] Renaming files based on a specific pattern.
    - [ ] Automatically backing up specific folders.
    - [X] Automatically reset testing sandbox.

### User Acceptance Testing

- [ ] ???. Your Python scripts will be tested by an automated system. Make sure to follow the requirements and instructions closely. Your menu-driven application should be user-friendly and easy to navigate.

### Configuration

- [X] Create a project named `automation`.
- [X] Copy the folders and files from [lab/assets/user-docs](https://github.com/codefellows/seattle-code-python-401n7/tree/main/class-19/lab/assets/).
- [X] Create the necessary folders and files to demonstrate and test your automation tasks according to the Feature Tasks and Requirements.
