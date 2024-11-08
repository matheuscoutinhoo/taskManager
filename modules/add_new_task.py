from modules import cleaner

from classes import Task
from time import sleep

def add_new_task(owner):
   from modules.menu import menu
   cleaner()
   task = Task.new_task()
   owner.add_task(task)
   cleaner()
   print('Creating task...')
   sleep(2)
   cleaner()
   print('Your task was succesfully created.')
   sleep(2)
   menu(owner)
   