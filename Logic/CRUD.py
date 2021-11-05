from Domain.vanzari import creeaza_vanzare, get_id


def adaugare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere, lista):
    '''
    Adaugarea unei vanzari intr o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: int
    :param tip_reducere: string
    :return: lista cu prajiturile vechi, actualizata cu cea adaugata acum
    '''


    vanzare = creeaza_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere)
    return lista + [vanzare]




def get_by_id(id, lista):
    '''
    Gaseste o vanzare cu id-ul dat dintr o lista
    :param id: string
    :param lista: lista de vanzari
    :return: vanzarea cu id ul dat din lista, None in caz contrar
    '''
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare
    return None

def stergere_vanzare(id, lista):
    '''
    Functie care sterge o vanzare cu id ul dat din lista
    :param id: string
    :param lista: lista de vanzari
    :return: o lista de vanzari cu exceptia vanzarii cu id-ul dat
    '''


    return [vanzare for vanzare in lista if get_id(vanzare) != id]




def modificare_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere, lista):
    '''
    Modifica vanzarea cu id-ul dat
    :param id:
    :param titlu_carte:
    :param gen_carte:
    :param pret:
    :param tip_reducere:
    :return:
    '''

    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua = creeaza_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua

def generare_lista():
    '''
    Formeaza o lista initiala de vanzari, neintroduse de utilizator de la tastatura
    in scop de testare
    :return: lista cu cateva vanzari predefinite
    '''
    lista = []
    lista = adaugare_vanzare("1", "Winnetou", "Aventura", 50, "none", lista)
    lista = adaugare_vanzare("2", "Harry Potter", "Aventura", 60, "silver", lista)
    lista = adaugare_vanzare("3", "Ragdoll", "Thriller", 76, "gold", lista)
    lista = adaugare_vanzare("4", "Becoming, Paperback", "Biografie", 37, "none", lista)
    lista = adaugare_vanzare("5", "Lantul", "Drama", 45, "silver", lista)
    lista = adaugare_vanzare("6", "Pacienta tacuta", "Drama", 55, "gold", lista)
    lista = adaugare_vanzare("7", "Winnetou", "Aventura", 55, "silver", lista)

    return lista