from Domain.vanzari import to_string
from Logic.CRUD import adaugare_vanzare, stergere_vanzare, modificare_vanzare


def meniu_optiuni():
    print("Add : id -> str, titlu -> str , gen ->str ,pret ->float , tip reducere -> str")
    print("Delete: id")
    print("Update: id -> str, titlu -> str , gen ->str ,pret ->float , tip reducere -> str")
    print("ShowAll")
    print("Break")


def show_all(lista):
    for vanzare in lista:
        print(to_string(vanzare))
    print()


def meniu_principal(lista):
    while True:
        optiune = input("Dati optiunea -> ")
        if optiune == "stop":
            break
        cuvinte = optiune.split(";")
        for elemente in cuvinte:
            comenzi = elemente.split(',')
            if comenzi[0].lower() == 'help':
                meniu_optiuni()
            elif comenzi[0].lower() == 'add':
                try:
                    lista = adaugare_vanzare(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
                except ValueError as ve:
                    print("Eroare : {}".format(ve))
            elif comenzi[0].lower() == 'delete':
                try:
                    lista = stergere_vanzare(comenzi[1], lista)
                except ValueError as ve1:
                    print("Eroare : {}".format(ve1))
            elif comenzi[0].lower() == "update":
                lista = modificare_vanzare(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
            elif comenzi[0].lower() == 'showall':
                show_all(lista)
            else:
                print("Optiune invalida! Alegeti alta sau incercati help pentru mai multe indicatii")