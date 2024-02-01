# import modules.camper as camper
# if __name__ == '__main__':
#     camper.menu()
import os
from modules.Camper import Camper

if __name__ == '__main__':
    os.system('cls')
    print(f"""
          {'-'*12}
          Menu Camper
          {'-'*12}""")
    menu = ['Create', 'Read', 'Update', 'Delete', 'Exit']
    while True:
        # os.system('cls')
        print(''.join([f'{item+1}. {value}\n' for item, value in enumerate(menu)]))
        try:
            option = int(input('Option: '))
            if option <= len(menu) and option > 0:
                match(option):
                    case 1:
                        name = input('Name: ')
                        surname = input('Surname: ')
                        age = int(input('Age: '))
                        camper = Camper(name, surname, age)
                    case 2:
                        camper.read()
                    case 3:
                        camper.update()
                    case 4:
                        camper.delete()
                    case 5:
                         break
        except ValueError:
            print('Choose a option')