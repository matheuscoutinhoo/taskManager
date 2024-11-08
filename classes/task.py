class Task:
   def __init__(self, start_date, end_date, description, category, status):
      self.__end_date = end_date
      self.__start_date = start_date
      self.__description = description
      self.__category = category
      self.__status = status
   
   @classmethod
   def new_task(cls):
      status = str(input('Enter task status (To do, In progress, Done): '))
      start_date = str(input('Enter task start date (DD/MM): '))
      end_date = str(input('Enter task end date (DD/MM): '))
      description = str(input('Enter task description: '))
      category = str(input('Enter task category: '))
      
      new_task = Task(start_date, end_date, description, category, status)
      return new_task
   
   def set_status(self):
      self.status = str(input('Enter the status of the task (To Do, Doing, Done): '))

   def get_task_data(self):
      return {
         'Status': self.__status,
         'End Date': self.__end_date,
         'Start Date': self.__start_date,
         'Description': self.__description,
         'Category': self.__category
      }
      

   
   