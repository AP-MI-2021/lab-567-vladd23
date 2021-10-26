from Domain.vanzari import get_titlu, get_id, get_gen, get_pret, get_reducere, to_string, set_pret, set_gen


def test_domeniu():
    vanzare1 = {"id": "1", "titlu_carte": "Ragdoll", "gen_carte": "thriller", "pret": 50,"tip_reducere": "gold" }
    vanzare2 = {"id": "2", "titlu_carte": "Winnetou", "gen_carte": "aventura", "pret": 45, "tip_reducere": "none"}
    assert get_titlu(vanzare1) == "Ragdoll"
    assert get_id(vanzare1) == "1"
    assert get_gen(vanzare1) == "thriller"
    assert get_pret(vanzare1) == 50
    assert get_reducere(vanzare1) == "gold"
    set_pret(vanzare1, 40)
    assert get_pret(vanzare1) == 40
    set_gen(vanzare1, "actiune")
    assert get_gen(vanzare1) == "actiune"