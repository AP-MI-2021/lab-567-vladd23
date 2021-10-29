from Logic.CRUD import adaugare_vanzare, generare_lista
from Tests.apelare_toate_teste import all_tests
from UserInterface.consola import run_menu


def main():
    all_tests()
    lista = generare_lista()
    run_menu(lista)

if __name__ == '__main__':
    main()