#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    a = True
    while True:
        if not wall_is_beneath():
            move_down()
            a = False
        if wall_is_beneath():
            move_right()



    pass


if __name__ == '__main__':
    run_tasks()
