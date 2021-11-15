from Domain.vanzari import get_reducere, get_pret, set_pret, get_titlu, set_gen, get_gen, creeaza_vanzare, get_id


def aplicare_discount(lista):
    '''
    Aplica un discount de 5% reducerilor silver si 10% discount reducerilor de tip gold
    :param lista:
    :return:
    '''
    lista_noua =[]
    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) - (0.05 * get_pret(vanzare)),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        elif get_reducere(vanzare) == "gold":
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) - (0.10 * get_pret(vanzare)),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua

def modificare_gen_pentru_titlu(lista, titlu, gen_nou):
    '''
    Modifica genul unei vanzari cu titlul dat
    :param lista: lista de vanzari
    :param titlu: titlul dupa care se cauta
    :return: lista cu modificari
    '''
    lista_noua =[]

    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_nou,
                get_pret(vanzare),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua

def pret_minim_per_gen(lista):
    '''
    Functie care calculeaza pretul minim al unei vanzari pentru fiecare gen de carte
    :param lista: lista de vanzari
    :return: dictionar in care cheia este genul si
    valoarea o reprezinta pretul minim al vanzarii din genul respectiv
    '''
    rezultat = {}
    for vanzare in lista:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = get_pret(vanzare)
        else:
            rezultat[gen] = get_pret(vanzare)

    return rezultat


def sortare_in_functie_de_pret(lista):
    '''
    Functie care sorteaza lista crescator in functie de pret
    :param lista: lista de vanzari
    :return: lista de vanzari sortata
    '''
    return sorted(lista, key=lambda x: get_pret(x))

def nr_titluri_gen(gen, lista):
    lista_titluri = []
    for vanzare in lista:
        if get_gen(vanzare) == gen:
            lista_titluri.append(get_titlu(vanzare))

    set_lista_titluri = set(lista_titluri)
    lista_fara_duplicatii = list(set_lista_titluri)

    return len(lista_fara_duplicatii)

def nr_titluri_distincte_pe_gen(lista):
    '''
    Functie care determina pentru fiecare gen, numarul de titluri distincte
    :param lista: lista de vanzari
    :return: dictionar care are ca si cheie numele genului,
    iar ca valoare numarul de titluri distincte pentru acel gen
    '''
    rezultat = {}
    for vanzare in lista:
        gen = get_gen(vanzare)
        if gen not in rezultat:
            rezultat[gen] = nr_titluri_gen(gen, lista)

    return rezultat