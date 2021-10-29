from Domain.vanzari import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import adaugare_vanzare, get_by_id, stergere_vanzare, modificare_vanzare


def test_adaugare_vanzare():
    lista =[]
    lista = adaugare_vanzare("1", "Abecedar", "Thriller", 30, "none", lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_titlu(get_by_id("1", lista)) == "Abecedar"
    assert get_gen(get_by_id("1", lista)) == "Thriller"
    assert get_pret(get_by_id("1", lista)) == 30
    assert get_reducere(get_by_id("1", lista)) == "none"

def test_stergere_vanzare():
    lista = []
    lista = adaugare_vanzare("1", "Abecedar", "Thriller", 30, "none", lista)
    lista = adaugare_vanzare("2", "Ion", "Interbelic", 40, "silver", lista)
    lista = adaugare_vanzare("3", "Bond", "Action", 50, "gold", lista)

    lista = stergere_vanzare("3", lista)
    assert len(lista) == 2
    assert get_by_id("3", lista) is None
    assert get_by_id("2", lista) is not None

    lista = stergere_vanzare("1", lista)
    assert len(lista) == 1
    assert get_by_id("2", lista) is not None

def test_modificare_vanzare():
    lista = []
    lista = adaugare_vanzare("1", "Abecedar", "Thriller", 30, "none", lista)
    lista = adaugare_vanzare("2", "Ion", "Interbelic", 40, "silver", lista)
    lista = adaugare_vanzare("3", "Bond", "Action", 50, "gold", lista)

    lista = modificare_vanzare("1", "Morcoveata", "Thriller", 35, "silver", lista)

    vanzare_actualizata = get_by_id("1", lista)

    assert get_id(vanzare_actualizata) == "1"
    assert get_titlu(vanzare_actualizata) == "Morcoveata"
    assert get_gen(vanzare_actualizata) == "Thriller"
    assert get_pret(vanzare_actualizata) == 35
    assert get_reducere(vanzare_actualizata) == "silver"

    assert get_id(get_by_id("2", lista)) == "2"
    assert get_titlu(get_by_id("2", lista)) == "Ion"
    assert get_gen(get_by_id("2", lista)) == "Interbelic"
    assert get_pret(get_by_id("2", lista)) == 40
    assert get_reducere(get_by_id("2", lista)) == "silver"
