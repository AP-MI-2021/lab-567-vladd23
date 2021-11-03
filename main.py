from Logic.CRUD import adaugare_vanzare, generare_lista
from Tests.apelare_toate_teste import all_tests
from UserInterface.consola import run_menu
from UserInterface.string_console import meniu_principal


def main():
    all_tests()
    lista = generare_lista()
    meniu_principal(lista)

if __name__ == '__main__':
    main()