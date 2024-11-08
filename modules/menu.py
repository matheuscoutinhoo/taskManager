from modules import cleaner
from modules.add_new_task import add_new_task
from modules.task_menu import task_menu
from time import sleep

def menu(owner):
   cleaner()
   task_list = owner.get_task_list()
   print(f'Hello, {owner.get_name()}!')
   
   try:
      option = int(input((f'\nYou have {len(task_list)} tasks. Please select an option:\n\n1 - Add a new task\n2 - View task list\n3 - Exit\n')))
      
      if option == 1:
         add_new_task(owner)
      elif option == 2:
         task_menu(owner)
   except ValueError:
      cleaner()
      print('\nPlease select an valid option!!\n')
      sleep(3)
      cleaner()
      menu(owner)
   