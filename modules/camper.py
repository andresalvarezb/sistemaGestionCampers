import os
from .variables import save, getAll

def create():
    os.system('cls')
    print(f"""
          {'-'*20}
          Formulario de Camper
          {'-'*20}""")

    save({
        'name': input('Name: '),
        'surname': input('Surname: '),
        'age': input('Age: '),
    })

    os.system('pause')

def read():
    print(getAll())

def update():
    pass

def delete():
    pass

def menu():
    os.system('cls')
    print(f"""
          {'-'*12}
          Menú Camper
          {'-'*12}""")
    menu = ['Guardar', 'Buscar', 'Actualizar', 'Eliminar', 'Salir']
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

if __name__ == '__main__':
    menu()