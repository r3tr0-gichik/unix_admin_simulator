import subprocess
import os
import time
import colorama
from colorama import Fore, Back, Style
import random
import err_processes_code
from err_processes_code import process_err_code
from htop_func import htop_processes

def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)

commandList = ["htop", "ls", "cat"]

def processes_is_down():
    bash('clear')
    server_status = f"{Fore.GREEN}ONLINE{Style.RESET_ALL}"
    processes_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
    print(f"SERVER STATUS: {server_status}")
    print(f"PROCESSES STATUS: {processes_status}")
    time.sleep(1)
    print("Wait, what the hell is going on?")
    time.sleep(2)
    print("Lets check if all necessary services are running...")

    print(f"Use this commands: {commandList}\n")

    terminal_commands()
    

def terminal_commands():

    user_action = input(str("> "))
    if user_action == "htop" and user_action in commandList:
        terminal_command_htop()
    elif user_action == "ls" and user_action in commandList:
        print("whatifallprocessesdown.txt", "restartprocesses.sh", "killthiszombies.py", "processes_err_code.sh", "startservices.sh")
        terminal_commands()
    elif user_action == "cat":
        print("Err: cat must get file")
        terminal_commands()
    elif user_action == "./restartprocesses.sh":
        restartprocesses()
    elif user_action == "python killthiszombies.py":
        kill_this_zombies()
    elif user_action == "cat whatifallprocessesdown.txt":
        print("Hello, my friend, Im your ancestor (in a way)\n"
              "So, if you've opened this file, that means u have problems with processes,\n"
              "Probably they are all down on somthing else.\n"
              "Dont worry, Ill help you with it).\n"
              "First of all, look at them processes (use htop in terminal)\n"
              "If you see too much zombies - use my script (killthiszombies.py)\n"
              "If all processes are stopped, just turn it on with restartprocesses.sh.\n"
              "If u see 'No exected processes' error that means they are not started, use startservices.sh.\n")
        terminal_commands()
    elif user_action == "./processes_err_code.sh":
        process_err_code()
        terminal_commands()
    elif user_action == "./startservices.sh":
        startservices()
    else:
        print("Err: this command is not in list of not allowed")
        terminal_commands()

def kill_this_zombies():
    bash('clear')
    print("Killing...")
    print ("Press Ctrl+C to stop.")
    time.sleep(1)
    s = "#"
    for i in range(11):
        time.sleep(random.randint(1, 3))
        print((str(i*10)), '%', i*s, end='\r')
    print('\n')
    time.sleep(3)
    print("\nAll zombies killed successfully")

def restartprocesses():
    case = random.randint(1,2)
    match case:
        case 1:
            bash('clear')
            service_1_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
            service_2_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"
            for i in range(1,6):
                if random.randint(1,2) == 1:
                    print(f"SERVICE {i} STATUS: {service_1_status}")
                    time.sleep(1)
                else:
                    print(f"SERVICE {i} STATUS: {service_2_status}")
                    time.sleep(1)
            print("Err: One or more processes are not working")
            time.sleep(1)
            print('Rebooting...')
            time.sleep(1)
            s = "#"
            for i in range(11):
                time.sleep(random.randint(1, 3))
                print((str(i*10)), '%', i*s, end='\r')
            print('\n')
            for i in range(1,6):
                print(f"SERVICE {i} STATUS: {service_2_status}")
                time.sleep(1)
            print('All processes are rebooted and started successfully')
            time.sleep(1)
            print('Exiting...')
            time.sleep(1)

        case 2:
            bash('clear')
            service_1_status = f"{Fore.RED}UNKNOWN{Style.RESET_ALL}"
            service_2_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"
            for i in range(1,6):
                print(f"SERVICE {i} STATUS: {service_1_status}")
                time.sleep(1)
            print("Err: One or more processes are not working")
            time.sleep(1)
            print('Starting...')
            time.sleep(1)
            s = "#"
            for i in range(11):
                time.sleep(random.randint(1, 3))
                print((str(i*10)), '%', i*s, end='\r')
            print('\n')
            for i in range(1,6):
                print(f'SERVICE {i} STATUS: {service_2_status}')
                time.sleep(1)
            print('All processes are running')
            time.sleep(1)
            print('Exiting...')
            time.sleep(1)
            
        case _: 
            print("Error: unknown number of cases, rebooting...")
            time.sleep(3)
            restartprocesses()

def startservices():
    bash('clear')
    print('Checking services status...'); time.sleep(1); print('Showing...\n'); time.sleep(1)
    service_1_status = f"{Fore.RED}LOADING{Style.RESET_ALL}"
    service_2_status = f"{Fore.GREEN}RUNNING{Style.RESET_ALL}"
    s = "#"
    for i in range(1, 6): 
        print(f'SERVICE {i}: {service_1_status}')
        for j in range(11):
            print((str(j*10)), '%'," : ", j*s, end='\r')
            time.sleep(random.randint(1, 3))
        print('\n')
        time.sleep(random.randint(1, 3))
    bash('clear')
    print('REBOOTING')
    time.sleep(1)
    for i in range(1,6):
        print(f'SERVICE {i}: {service_2_status}')
        time.sleep(0.1)
    print('\nALL PROCESSES BOOTED SUCCESSFULLY')
    time.sleep(0.05)
    print('Exiting...')
    time.sleep(3)




def terminal_command_htop():
    htop_processes()
    time.sleep(3)
    print('So... Can you understand something here?')
    time.sleep(1)
    print(f'I think, processes_err_code.sh is more effective or another commands in list {commandList}')
    terminal_commands()
    
