def creeaza_vanzare(id, titlu_carte, gen_carte, pret, tip_reducere):
    '''
    Functie care creeaza o vanzare cu toate caracteristicile
    :param id: str
    :param titlu_carte: str
    :param gen_carte: str
    :param pret: int
    :param tip_reducere: str
    :return: o vanzare sub forma de dictionar
    '''

    return [id, titlu_carte, gen_carte, pret, tip_reducere]


def get_id(vanzare):
    '''
    Returneaza id-ul vanzarii
    :param vanzare:
    :return: id
    '''
    return vanzare[0]

def get_titlu(vanzare):
    '''
    Returneaza titlul vanzarii
    :param vanzare:
    :return: titlul
    '''
    return vanzare[1]

def get_gen(vanzare):
    '''
    Returneaza genul unei carti
    :param vanzare:
    :return: gen
    '''
    return vanzare[2]

def get_pret(vanzare):
    '''
    Returneaza pretul unei carti
    :param vanzare:
    :return: pretul
    '''
    return float(vanzare[3])

def get_reducere(vanzare):
    '''
    Returneaza tipul de reducere pe care il primeste un client
    :param vanzare:
    :return: tip reducere
    '''
    return vanzare[4]

def to_string(vanzare):
    '''
    transforma dictionarul vanzare sub forma de string
    :param vanzare:
    :return: dictionarul vanzare sub forma de string
    '''
    return '"id": {}, "titlu_carte": {}, "gen_carte": {}, "pret": {},"tip_reducere": {}'.format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )

def set_pret(vanzare, pret_nou):
    '''
    Seteaza un pret nou pentru o vanzare
    :param vanzare:
    :param pret_nou:
    :return:
    '''
    vanzare[3] = pret_nou

def set_gen(vanzare, gen_nou):
    '''
    Inlocuieste un gen de cart cu altul nou
    :param vanzare:
    :param gen_nou:
    :return:
    '''
    vanzare[2] = gen_nou