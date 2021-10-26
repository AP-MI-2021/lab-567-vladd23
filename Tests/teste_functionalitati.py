from Domain.vanzari import get_pret, get_gen
from Logic.functionalitati import aplicare_discount, modificare_gen_pentru_titlu


def test_aplicare_discount():
    vanzare1 = {"id": "1", "titlu_carte": "Ragdoll", "gen_carte": "thriller", "pret": 50, "tip_reducere": "silver"}
    vanzare2 = {"id": "2", "titlu_carte": "Winnetou", "gen_carte": "aventura", "pret": 45, "tip_reducere": "gold"}
    lista = []
    lista.append(vanzare1)
    lista.append(vanzare2)
    aplicare_discount(lista)
    assert get_pret(lista[0]) == 47.5
    assert get_pret(lista[1]) == 40.5

def test_modificare_gen_pentru_titlu():
    vanzare1 = {"id": "1", "titlu_carte": "Ragdoll", "gen_carte": "thriller", "pret": 50, "tip_reducere": "silver"}
    vanzare2 = {"id": "2", "titlu_carte": "Winnetou", "gen_carte": "aventura", "pret": 45, "tip_reducere": "gold"}
    lista = []
    lista.append(vanzare1)
    lista.append(vanzare2)
    modificare_gen_pentru_titlu(lista, "Ragdoll", "actiune")
    assert get_gen(lista[0]) == "actiune"