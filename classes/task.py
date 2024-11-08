class Task:
   def __init__(self, owner, end_date, start_date, description, category, status):
      self.__end_date = end_date
      self.__start_date = start_date
      self.__description = description
      self.__category = category
      self.__owner = owner
      self.__status = status
   
   @classmethod
   def new_task(cls):
      status = str(input('Enter task status (To do, In progress, Done): '))
      owner = str(input('Enter task owner: '))
      end_date = str(input('Enter task end date (YYYY-MM-DD): '))
      start_date = str(input('Enter task start date (YYYY-MM-DD): '))
      description = str(input('Enter task description: '))
      category = str(input('Enter task category: '))
      
      new_task = Task(owner, end_date, start_date, description, category, status)
      return new_task
   
   def set_status(self):
      self.status = str(input('Enter the status of the task (To Do, Doing, Done): '))

   def get_task_data(self):
      return {
         'Status': self.__status,
         'Owner': self.__owner,
         'End Date': self.__end_date,
         'Start Date': self.__start_date,
         'Description': self.__description,
         'Category': self.__category
      }
      

   
   