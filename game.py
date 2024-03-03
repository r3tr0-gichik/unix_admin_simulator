import subprocess
import os
import time
import colorama
from colorama import Fore, Back, Style
import random
import crash_event
import power_off_event
import all_good_event
import processes_is_down_event


def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)

# Add days counter

def game():
    print("Welcome to the game!")
    print("If u wanna start plz enter 'start'\nIf u wanna exit enter 'exit'")
    answer = input(str("> "))
    if answer == "start":
        start()
    elif answer == "exit":
        print("Goodbye!\n")
    else:
        print("Wrong command\nPlease try again")
        game()

def start():
    bash('clear')
    server_status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
    processes_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"
    # days_passed = days_counter()
    print(f"SERVER STATUS: {server_status}")
    print(f"PROCESSES STATUS: {processes_status}")
    # print(f"DAYS PASSED: {days_passed}")


    time.sleep(random.randint(5,10))

    event = str(random.randint(1,5))

    if event == "1": # Crash server event
        crash_event.crash_server()

    elif event == "2": # Power off event
        power_off_event.power_off_event()
        
    elif event == "3": # All good
        all_good_event.all_good_event()

    elif event == "4": # All good
        all_good_event.all_good_event()

    elif event == "5": # Processes is down
        processes_is_down_event.processes_is_down()







def main():
    try:
        game()
        while True:
            start()
    except KeyboardInterrupt:
        print("U pressed Ctrl+C. Exiting...")
        time.sleep(1)






if __name__ == "__main__":
    main()