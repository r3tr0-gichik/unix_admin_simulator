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

def power_off_event():
    bash('clear')
    server_status = f"{Fore.RED}OFFLINE{Style.RESET_ALL}"
    processes_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
    print(f"SERVER STATUS: {server_status}")
    print(f"PROCESSES STATUS: {processes_status}")
    time.sleep(2)
    print("Electicity went out... Server is down.")
    time.sleep(random.randint(7,10))
    print("Stil no power. Maybe its just a temporary problem.")
    time.sleep(random.randint(5,10))
    print("Power on, lets check our processes (enter 'isitalive.sh')")
    time.sleep(1)
    alive_check()
    time.sleep(1)
    print("It seems processes are not started, use startservices.sh to start them.")
    start_services()
    bash('clear')
    time.sleep(1)
    print('Well, now we can check the status');terminal_command_status()


def terminal_command_status():
    if input("> ") == "status":
        bash('clear')
        server_status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
        processes_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"
        print(f"SERVER STATUS: {server_status}")
        print(f"PROCESSES STATUS: {processes_status}")   
        time.sleep(1)
        print('Fine, its working')
        time.sleep(1)
        print('Lets go back')
        time.sleep(3)
    else:
        print("Wrong command, maybe you mean 'status'?")
        terminal_command_status()

def alive_check():
    if input(str("> ")) == "./isitalive.sh":
        server_status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
        processes_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
        print(f"SERVER STATUS: {server_status}")
        print(f"PROCESSES STATUS: {processes_status}")
    else:
        print("Err: command not found")
        alive_check()

def start_services():
    if input(str("> ")) == "./startservices.sh":
        print("Wait a minute...")
        s='#'
        for i in range(11):
            time.sleep(random.randint(1, 3))
            print((str(i*10)), '%', i*s, end='\r')
        time.sleep(3)
    else:
        print("Err: command not found")