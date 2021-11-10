from Tests.teste_crud import test_adaugare_vanzare, test_modificare_vanzare, test_stergere_vanzare
from Tests.teste_domeniu import test_domeniu
from Tests.teste_functionalitati import test_aplicare_discount, test_modificare_gen_pentru_titlu, \
    test_pret_minim_per_gen, test_sortare_in_functie_de_pret, test_nr_titluri_distincte_pe_gen
from Tests.teste_undo_redo import test_undo_si_redo


def all_tests():
    test_domeniu()
    test_adaugare_vanzare()
    test_modificare_vanzare()
    test_stergere_vanzare()
    test_aplicare_discount()
    test_modificare_gen_pentru_titlu()
    test_pret_minim_per_gen()
    test_sortare_in_functie_de_pret()
    test_nr_titluri_distincte_pe_gen()
    test_undo_si_redo()
