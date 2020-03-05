#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while True:
        if wall_is_above() and wall_is_beneath():
            move_right()
            if wall_is_on_the_right():
                move_left()
        elif not wall_is_beneath() or not wall_is_above():
            move_up()
            if wall_is_above():
                while True:
                    move_left()



    pass


if __name__ == '__main__':
    run_tasks()
