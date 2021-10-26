from Domain.vanzari import to_string
from Logic.CRUD import adaugare_vanzare, stergere_vanzare, modificare_vanzare
from Logic.functionalitati import aplicare_discount, modificare_gen_pentru_titlu


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("5. Modificarea genului pentru un titlu dat")
    print("a. Afisarea vanzarilor")
    print("x. Iesire")


def ui_adaugare_vanzare(lista):
    '''
    Adauga o vanzare in lista pe baza alegerii userului
    :param lista:
    :return: adauga vanzarea creata in lista
    '''
    id = input("Dati id-ul: ")
    titlu_carte = input("Numele cartii: ")
    gen_carte = input("Genul cartii: ")
    pret = int(input("Pretul cartii: "))
    tip_reducere = input("Tipul de reducere (se va alege intre 'none', 'silver' sau 'gold')")
    return adaugare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere, lista)


def ui_stergere_vanzare(lista):
    '''
    Sterge o vanzare din lista pe baza id ului dat de user
    :param lista:
    :return: lista de vanzari fara vanzarea aleasa de user
    '''
    id = input("Dati id-ul vanzarii pe care o doriti stearsa: ")
    return stergere_vanzare(id, lista)

def ui_modificare_vanzare(lista):
    '''
    Modifica o vanzare din lista pe baza id ului
    :param lista: lista de vanzari
    :return: lista de vanzari, cu modificarile efectuate pe vanzarea dorita
    '''
    id = input("Dati id-ul vanzarii pe care doriti sa o modificati: ")
    titlu_carte = input("Titlu nou: ")
    gen_carte = input("Genul nou: ")
    pret = int(input("Noul pret al cartii: "))
    tip_reducere = input("Tipul nou de reducere: (none/silver/gold) ")
    return modificare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere,lista)

def show_all(lista):
    print("Lista vanzarilor: ")
    print()
    for vanzare in lista:
        print(to_string(vanzare))


def ui_aplicare_discount(lista):
    '''
    aplica discountul pentru toate tipurile de reducere silver si gold
    :param lista:
    :return: lista cu schimbarile facute
    '''
    return aplicare_discount(lista)


def ui_modificare_gen(lista):
    '''
    Modifica genul unei carti cu titlul introdus de la tastatura
    :param lista:
    :return:
    '''
    titlu = input("Titlul cartii pe care doriti sa il modificati: ")
    gen_nou = input("Noul gen pentru cartea cu titlul selectat: ")
    return modificare_gen_pentru_titlu(lista, titlu, gen_nou)


def run_menu(lista):
    while True:
        print()
        print_menu()
        optiune = input("Alegeti optiunea dorita: ")
        print()
        if optiune == "1":
            lista = ui_adaugare_vanzare(lista)
        elif optiune == "2":
            lista = ui_stergere_vanzare(lista)
        elif optiune == "3":
            lista = ui_modificare_vanzare(lista)
        elif optiune == "4":
            lista = ui_aplicare_discount(lista)
        elif optiune == "5":
            lista = ui_modificare_gen(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida! Selectati din nou.")
