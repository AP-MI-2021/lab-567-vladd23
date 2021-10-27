from Domain.vanzari import get_titlu, get_id, get_gen, get_pret, get_reducere, to_string, set_pret, set_gen, \
    creeaza_vanzare


def test_domeniu():

    vanzare1 = creeaza_vanzare("1", "Ragdoll", "thriller", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "Winnetou", "aventura", 45, "gold")

    assert get_titlu(vanzare1) == "Ragdoll"
    assert get_id(vanzare1) == "1"
    assert get_gen(vanzare1) == "thriller"
    assert get_pret(vanzare1) == 50
    assert get_reducere(vanzare1) == "silver"
    set_pret(vanzare1, 40)
    assert get_pret(vanzare1) == 40
    set_gen(vanzare1, "actiune")
    assert get_gen(vanzare1) == "actiune"