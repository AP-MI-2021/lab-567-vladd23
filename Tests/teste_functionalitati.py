from Domain.vanzari import get_pret, get_gen, creeaza_vanzare, get_id
from Logic.CRUD import generare_lista, adaugare_vanzare
from Logic.functionalitati import aplicare_discount, modificare_gen_pentru_titlu, pret_minim_per_gen, \
    sortare_in_functie_de_pret, nr_titluri_distincte_pe_gen


def test_aplicare_discount():

    lista = []
    lista = adaugare_vanzare("1", "Carte1", "Drama", 50,"gold", lista)
    lista = adaugare_vanzare("2", "Carte2", "Aventura", 50, "silver", lista)
    lista = adaugare_vanzare("3", "Carte3", "Comedie", 50, "none", lista)

    lista_noua = aplicare_discount(lista)

    assert get_pret(lista_noua[0]) == 45.0
    assert get_pret(lista_noua[1]) == 47.5
    assert get_pret(lista_noua[2]) == 50.0


def test_modificare_gen_pentru_titlu():
    vanzare1 = creeaza_vanzare("1", "Ragdoll", "thriller", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "Winnetou", "aventura", 45, "gold")

    lista = []
    lista = adaugare_vanzare("1", "Ragdoll", "thriller", 50, "silver", lista)
    lista = adaugare_vanzare("2", "Winnetou", "aventura", 45, "gold", lista)
    lista = modificare_gen_pentru_titlu(lista, "Ragdoll", "actiune")
    assert get_gen(lista[0]) == "actiune"

def test_pret_minim_per_gen():
    lista = generare_lista()
    rezultat = pret_minim_per_gen(lista)

    assert rezultat["Aventura"] == 50
    assert rezultat["Drama"] == 45
    assert rezultat["Thriller"] == 76

def test_sortare_in_functie_de_pret():
    lista = generare_lista()
    lista = sortare_in_functie_de_pret(lista)
    assert get_id(lista[0]) == "4"
    assert get_pret(lista[0]) < get_pret(lista[1])
    assert get_id(lista[1]) == "5"

def test_nr_titluri_distincte_pe_gen():
    lista = generare_lista()
    rezultat = nr_titluri_distincte_pe_gen(lista)
    assert rezultat["Aventura"] == 2
    assert rezultat["Thriller"] == 1
    assert rezultat["Biografie"] == 1
