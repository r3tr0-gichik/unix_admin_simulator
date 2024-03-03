from tabulate import tabulate
import random
from random import randint
import time

import subprocess
import os
import random


def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)



# Создание таблицы с данными
data = [['PID', 'USER', 'PRI', 'NI', 'VIRT', 'RES', 'SHR', 'S', 'CPU%', 'MEM%'],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'R', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        [randint(448, 10852), 'root', 20, 0, randint(11, 1334), randint(500,  19999), randint(1499, 32999), 'S', randint(1, 2), randint(1,2)],
        ]
memory_usage = [
    [0,     '[||||----------------------------------------------------------]'],
    [1,     '[||------------------------------------------------------------]'],
    [2,     '[|||||||-------------------------------------------------------]'],
    [3,     '[|||-----------------------------------------------------------]'],
    ['Mem', '[|||||||||||||||||||||-----------------------------------------]'],
    ['Swp', '[||------------------------------------------------------------]'],
]
processes_type = [
    ['Tasks',  ' ', randint(5, 20)],
    ['Threads',' ', randint(1, 140)],
    ['Kthr',   ' ', randint(1, 140)],
    ['Running',' ', randint(1,140)],
    ['Zombie', ' ', randint (0, 9)],
    ['Stopped',' ', randint(0, 9)]
]

# Вывод таблицы


def htop_processes():
    bash('clear')
    print(tabulate(data, headers='firstrow'))
    print(tabulate(memory_usage))
    print(tabulate(processes_type))


        