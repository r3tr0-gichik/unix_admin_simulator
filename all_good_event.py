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

def all_good_event():
    print('Nothing happened today, go home.')
    time.sleep(3)