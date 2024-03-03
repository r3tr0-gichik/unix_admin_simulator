import subprocess
import os
import random


def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)

class Processes_Error():
    def choice_err_code(self):
        error_code = str(random.randint(1,3))
        return error_code
    
    def output_err_code():
        process_error = Processes_Error()
        error_code = process_error.choice_err_code()
        return error_code
    
    def output_text(err_code):
        if err_code == "1":
            print(f"Err_code: {err_code} - Too many zombies")
        elif err_code == "2":
            print(f"Err_code: {err_code} - Processes are stopped")
        elif err_code == "3":
            print(f"Err_code: {err_code} - No expected processes")
        else:
            print(f"Err: there is no expected error code")

def process_err_code():
    err_code = Processes_Error.output_err_code()
    Processes_Error.output_text(err_code)
