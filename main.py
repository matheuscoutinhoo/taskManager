from classes.owner import Owner
from time import sleep
from modules import cleaner, menu

def main():
   print('Hello! Welcome to taskManager! Let`s start!\n\n')

   owner = Owner.new_owner()
   print('\n\nCreating your account. Please wait...')
   sleep(3)
   cleaner()
   
   menu(owner)

if __name__ == "__main__":
   main()