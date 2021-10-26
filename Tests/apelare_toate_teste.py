from Tests.teste_crud import test_adaugare_vanzare, test_modificare_vanzare, test_stergere_vanzare
from Tests.teste_domeniu import test_domeniu
from Tests.teste_functionalitati import test_aplicare_discount, test_modificare_gen_pentru_titlu


def all_tests():
    test_domeniu()
    test_adaugare_vanzare()
    test_modificare_vanzare()
    test_stergere_vanzare()
    test_aplicare_discount()
    test_modificare_gen_pentru_titlu()