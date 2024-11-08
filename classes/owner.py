class Owner:
   def __init__(self, name, task_list):
      self.__name = name
      self.__task_list = task_list
      
   @classmethod
   def new_owner(cls):
      name = input('Enter your name: ')
      task_list = []
      new_owner = Owner(name, task_list)
      return new_owner
   
   def add_task(self, task):
      self.__task_list.append(task)
   
   def get_task_list(self):
      return self.__task_list
   
   def get_name(self):
      return self.__name
   
   
   
       