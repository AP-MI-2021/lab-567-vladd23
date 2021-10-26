from Domain.vanzari import get_reducere, get_pret, set_pret, get_titlu, set_gen


def aplicare_discount(lista):
    '''
    Aplica un discount de 5% reducerilor silver si 10% discount reducerilor de tip gold
    :param lista:
    :return:
    '''

    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            pret_actual = get_pret(vanzare)
            pret_nou = pret_actual - 5 * pret_actual / 100
            set_pret(vanzare, pret_nou)
        if get_reducere(vanzare) == "gold":
            pret_actual = get_pret(vanzare)
            pret_nou = pret_actual - 10 * pret_actual / 100
            set_pret(vanzare, pret_nou)

    return lista

def modificare_gen_pentru_titlu(lista, titlu, gen_nou):
    '''
    Modifica genul unei vanzari cu titlul dat
    :param lista: lista de vanzari
    :param titlu: titlul dupa care se cauta
    :return: lista cu modificari
    '''
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            set_gen(vanzare, gen_nou)

    return lista