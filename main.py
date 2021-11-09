from Logic.CRUD import adaugare_vanzare, generare_lista
from Tests.apelare_toate_teste import all_tests
from UserInterface.consola import run_menu
from UserInterface.string_console import meniu_principal


def main():
    all_tests()
    lista = generare_lista()
    print("1. Consola principala")
    print("2. String console")
    x = input("Tipul de consola dorita: ")
    if x == "1":
        run_menu(lista)
    elif x == "2":
        meniu_principal(lista)
    else:
        print("Optiunea dorita nu exista!")
if __name__ == '__main__':
    main()