from Logic.CRUD import adaugare_vanzare


def test_undo_si_redo():
    lista = []
    lista_mare = []
    undoList = []
    redoList = []
    lista = adaugare_vanzare('1', 'Test1', 'Comedie', 123, 'silver', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]


    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}]] #merge

    lista = adaugare_vanzare('2', 'Test2', 'Comedie', 12, 'silver', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]


    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}]]
    #merge

    lista = adaugare_vanzare('3', 'Test3', 'Actiune', 122, 'gold', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}]]



    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}]]



    redoList.append(lista_mare)
    lista_mare = undoList.pop()



    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}]]
    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == []

    redoList.append(lista_mare)

    if len(undoList) > 0:
        lista_mare = undoList.pop()

    assert lista_mare == []

    lista = adaugare_vanzare('1', 'Test1', 'Comedie', 123, 'silver', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = adaugare_vanzare('2', 'Test2', 'Comedie', 12, 'silver', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = adaugare_vanzare('3', 'Test3', 'Actiune', 122, 'gold', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]


    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}]]



    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()



    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}]]


    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()



    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}], [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}]]



    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()



    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'},{'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}]
                          ]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    lista = adaugare_vanzare('4', 'Test4', 'Actsiune', 122, 'gold', lista)
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '4', 'titlu': 'Test4', 'gen': 'Actsiune', 'pret': 122, 'reducere': 'gold'}]
                          ]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()


    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '4', 'titlu': 'Test4', 'gen': 'Actsiune', 'pret': 122, 'reducere': 'gold'}]
                          ]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}]]


    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == []

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '4', 'titlu': 'Test4', 'gen': 'Actsiune', 'pret': 122, 'reducere': 'gold'}]
                          ]


    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()


    assert lista_mare == [[{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}],
                          [{'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '1', 'titlu': 'Test1', 'gen': 'Comedie', 'pret': 123, 'reducere': 'silver'}, {'id': '2', 'titlu': 'Test2', 'gen': 'Comedie', 'pret': 12, 'reducere': 'silver'}, {'id': '3', 'titlu': 'Test3', 'gen': 'Actiune', 'pret': 122, 'reducere': 'gold'}, {'id': '4', 'titlu': 'Test4', 'gen': 'Actsiune', 'pret': 122, 'reducere': 'gold'}]
                          ]
