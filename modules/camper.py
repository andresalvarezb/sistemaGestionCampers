import os
from .variables import save, getAll
from tabulate import tabulate

def create():
    os.system('cls')
    print(f"""
          {'-'*20}
          Camper's form
          {'-'*20}""")

    save({
        'name': input('Name: '),
        'surname': input('Surname: '),
        'age': input('Age: '),
    })

    os.system('pause')

def read(code = None):
    if (not code != None):
        print(tabulate(getAll(), headers=['Name', 'Surname', 'Age']))
    else:
        print(tabulate(getAll()[code-1], headers=['Name', 'Surname', 'Age']))

def update():
    os.system('cls')
    read()
    print(f"""
          {'-'*12}
          Update Camper
          {'-'*12}""")

    code = int(input('Which is the camper\'s code to update: '))
    read(code)
    while True:
        print("""Are you sure to update this camper?
              1. Yes
              2. No""")
        option = int(input(': '))
        match(option):
            case 1:
                information = {
                    'name': input('Name: '),
                    'surname': input('Surname: '),
                    'age': input('Age: '),
                }
                getAll()[code-1] = information
                break
            case 2:
                break

def delete():
    os.system('cls')
    read()
    print(f"""
          {'-'*12}
          Delete Camper
          {'-'*12}""")

    code = int(input('Which is the camper\'s code to delete: '))
    read(code)
    while True:
        print("""Are you sure to delete this camper?
              1. Yes
              2. No""")
        option = int(input(': '))
        match(option):
            case 1:
                del getAll()[code-1]
                break
            case 2:
                break

def menu():
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
                        create()
                    case 2:
                        read()
                    case 3:
                        update()
                    case 4:
                        delete()
                    case 5:
                         break
        except ValueError:
            print('Choose a option')
