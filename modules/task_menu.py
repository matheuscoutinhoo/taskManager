from modules import cleaner

def task_menu(owner):
   cleaner()
   
   task_list = owner.get_task_list()
   
   print('TASK LIST\n')
   
   task_id = 1
   for task in task_list:
      task_data = task.get_task_data()
      print(f'{task_id} - Description: {task_data['Description']} - Status: {task_data['Status']}')
      task_id += 1
      