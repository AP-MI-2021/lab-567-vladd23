from Domain.vanzari import to_string
from Logic.CRUD import adaugare_vanzare, stergere_vanzare, modificare_vanzare
from Logic.functionalitati import aplicare_discount, modificare_gen_pentru_titlu, pret_minim_per_gen, \
    sortare_in_functie_de_pret, nr_titluri_distincte_pe_gen


def print_menu():
    print()
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7. Ordonarea vânzărilor crescător după preț")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print()
    print("u. Undo")
    print("r. Redo")
    print("a. Afisarea vanzarilor")
    print("x. Iesire")
    print()


def ui_adaugare_vanzare(lista, undo_list, redo_list):
    '''
    Adauga o vanzare in lista pe baza alegerii userului
    :param lista:
    :return: adauga vanzarea creata in lista
    '''
    try:
        id = input("Dati id-ul: ")
        titlu_carte = input("Numele cartii: ")
        gen_carte = input("Genul cartii: ")
        pret = int(input("Pretul cartii: "))
        tip_reducere = input("Tipul de reducere (se va alege intre 'none', 'silver' sau 'gold')")
        rezultat = adaugare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere, lista)
        redo_list.clear()
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_vanzare(lista, undo_list, redo_list):
    '''
    Sterge o vanzare din lista pe baza id ului dat de user
    :param lista:
    :return: lista de vanzari fara vanzarea aleasa de user
    '''
    try:
        id = input("Dati id-ul vanzarii pe care o doriti stearsa: ")
        rezultat = stergere_vanzare(id, lista)
        undo_list.append(lista)
        redo_list.clear()

        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_modificare_vanzare(lista, undo_list, redo_list):
    '''
    Modifica o vanzare din lista pe baza id ului
    :param lista: lista de vanzari
    :return: lista de vanzari, cu modificarile efectuate pe vanzarea dorita
    '''

    try:
        id = input("Dati id-ul vanzarii pe care doriti sa o modificati: ")
        titlu_carte = input("Titlu nou: ")
        gen_carte = input("Genul nou: ")
        pret = int(input("Noul pret al cartii: "))
        tip_reducere = input("Tipul nou de reducere: (none/silver/gold): ")
        rezultat = modificare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere,lista)
        redo_list.clear()
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    print("Lista vanzarilor: ")
    print()
    for vanzare in lista:
        print(to_string(vanzare))


def ui_aplicare_discount(lista,  undo_list, redo_list):
    '''
    aplica discountul pentru toate tipurile de reducere silver si gold
    :param lista:
    :return: lista cu schimbarile facute
    '''
    try:
        undo_list.append(lista)
        redo_list.clear()
        nou = aplicare_discount(lista)

        return nou
    except ValueError as ve:
        print("Eraore: {}".format(ve))
        return lista


def ui_modificare_gen(lista, undo_list, redo_list):
    '''
    Modifica genul unei carti cu titlul introdus de la tastatura
    :param lista:
    :return: lista cu modificarile efectuate
    '''
    titlu = input("Titlul cartii pe care doriti sa il modificati: ")
    gen_nou = input("Noul gen pentru cartea cu titlul selectat: ")
    modificare = modificare_gen_pentru_titlu(lista, titlu, gen_nou)
    redo_list.clear()
    undo_list.append(lista)

    return modificare


def ui_pret_minim_gen(lista):
    '''
    Afiseaza pretul minim pentru fiecare gen
    :param lista: lista de vanzari
    :return:
    '''
    rezultat = pret_minim_per_gen(lista)
    for cheie in rezultat:
        print(cheie, ":", rezultat[cheie], "lei")




def ui_ordonare_in_functie_de_pret(lista):
    '''
    Functie care modifica lista de vanzari ordonand-o crescator in functie de pret
    :param lista: lista de vanzari
    :return: lista ordonata crescator in functie de pret
    '''
    lista = sortare_in_functie_de_pret(lista)
    for vanzare in lista:
        print(vanzare)



def ui_nr_titluri_distincte_per_gen(lista):
    '''
    Functie care determina numarul de titluri distincte pentru fiecare gen
    :param lista: lista de vanzari
    :return: lista de vanzari
    '''
    try:
        rezultat = nr_titluri_distincte_pe_gen(lista)

        for cheie in rezultat:
            print(cheie, ":", rezultat[cheie], "titluri distincte")
    except ValueError as ve:
        print("Eroare: {}".format(ve))




def run_menu(lista):

    undo_list = []
    redo_list = []

    while True:
        print()
        print_menu()
        optiune = input("Alegeti optiunea dorita: ")
        print()
        if optiune == "1":
            lista = ui_adaugare_vanzare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_stergere_vanzare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modificare_vanzare(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_aplicare_discount(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_modificare_gen(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_minim_gen(lista)
        elif optiune == "7":
            print(ui_ordonare_in_functie_de_pret(lista))
        elif optiune == "8":
            ui_nr_titluri_distincte_per_gen(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se mai poate efectua functia de undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate aplica redo!")
        else:
            print("Optiune invalida! Selectati din nou.")
