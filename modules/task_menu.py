from modules import cleaner

def task_menu(owner):
   cleaner()
   
   task_list = owner.get_task_list()
   
   print('TASK LIST\n')
   
   task_id = 1
   for task in task_list:
      task_data = task.get_task_data()
      print(f'{task_id} - Description: {task_data['Description']} - Status: {task_data['Status']} - Start date: {task_data['Start Date']} - End Date: {task_data['End Date']} - Category: {task_data['Category']}')
      task_id += 1
      
   option = int(input('\nWhat do you want to do?\n\n1 - delete a task\n2 - edit a task\n3 - create a new task\n4 - back to menu\n\nOption: '))
   
   if option == 1:
      removed_task_id = int(input('Type the task ID to be deleted: '))
      for i, task in enumerate(task_list):
         if (i+1) == removed_task_id:
            cleaner()
            owner.delete_task(task)
            cleaner()
            task_menu(owner)