from Domain.vanzari import creeaza_vanzare
from Logic.CRUD import adaugare_vanzare


def test_undo_si_redo():
    lista = []
    lista_mare = []
    undoList = []
    redoList = []
    lista = creeaza_vanzare(1, 'Test1', 'Comedie', 123, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]

    lista = creeaza_vanzare(2, 'Test2', 'Comedie', 12, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]

    lista = creeaza_vanzare(3, 'Test3', 'Actiune', 122, 'gold')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]
    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]
    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == []

    redoList.append(lista_mare)
    if len(undoList) > 0:
        lista_mare = undoList.pop()

    assert lista_mare == []

    lista = creeaza_vanzare(1, 'Test1', 'Comedie', 123, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = creeaza_vanzare(2, 'Test2', 'Comedie', 12, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = creeaza_vanzare(3, 'Test3', 'Actiune', 122, 'gold')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    lista = creeaza_vanzare(4, 'Test4', 'Actsiune', 122, 'golsad')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == []

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]