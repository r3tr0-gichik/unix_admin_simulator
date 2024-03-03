import subprocess
import os
import time
import colorama
from colorama import Fore, Back, Style
import random
def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)

def crash_server():
    bash('clear')
    server_status = f"{Fore.RED}OFFLINE{Style.RESET_ALL}"
    processes_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
    print(f"SERVER STATUS: {server_status}")
    print(f"PROCESSES STATUS: {processes_status}")
    print("Server is down and we dont know why...\nDeal with it.\n")
    time.sleep(1)
    print("U need to do something\n")
    crash_choise()

def crash_choise():
    print("-> restart server (use your script 'restart_server.sh')\n-> drink some tea (drink_tea.sh)\n-> cry(not recommended, cry.py)\n")
    print("Enter number of your desired action:")
    user_action = input(str("> "))
    if user_action == "./restart_server.sh":
        bash('clear')
        print('Hm... Lets try this one')
        time.sleep(3)
        print('I think all good, lets check it (enter "status")')
        terminal_command_status()   
    elif user_action == "./drink_tea.sh":
        bash('clear')
        print('Hm, drink tea is good, but maybe later?')
        time.sleep(3)
        crash_choise()
    elif user_action == "python cry.py":
        bash('clear')
        print("Oh, come on")
        time.sleep(3)
        print("Dont cry, that porblem is easy for u, just solve it and we can go to home")
        time.sleep(3)
        crash_choise()
    else:
        print("Wrong command, try again")
        crash_choise()

def terminal_command_status():
    if input(str("> ")) == "status":
        server_status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
        processes_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"

        print(f"SERVER STATUS: {server_status}")
        print(f"PROCESSES STATUS: {processes_status}")   
        time.sleep(1)
        print('HELL YEAZZZZ, U DID IT')
        time.sleep(1)
        print('Lets go back')
        time.sleep(3)
    else:
        print("Wrong command, maybe you mean 'status'?")
        terminal_command_status()

