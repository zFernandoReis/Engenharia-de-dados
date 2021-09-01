def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://fernando-teste:fernando-teste@cluster0.ulaja.mongodb.net/myFirstDatabase"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#Conexão como cliente

    return client['Midias']#base de dados

if __name__ == "__main__":
    midia = get_database()
    collection_name1 = midia["Filmes"] 
    #collection_name2 = midia["Serie"]
    #collection_name3 = midia["Anime"]
   

    item_1= {
        "_id" : "LC001",
        "titulo" : "Laranja mecânica",
        "ano de lancamento" : 1972,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }

    item_2= {
        "_id" : "LC002",
        "titulo" : "Titanic",
        "ano de lancamento" : 1999,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_3= {
        "_id" : "LC003",
        "titulo" : "Titanic",
        "ano de lancamento" : 1999,
        "Classificacao" : 9,
        "categoria" : "Drama"
    }
    item_4= {
        "_id" : "LC004",
        "titulo" : "Clube da Luta",
        "ano de lancamento" : 1996,
        "Classificacao" : 8.0,
        "categoria" : "Ação"
    }

    item_5= {
        "_id" : "LC005",
        "titulo" : "A procura da felicidade",
        "ano de lancamento" : 2006,
        "Classificacao" : 8.3,
        "categoria" : "Drama"
    }
    item_6= {
        "_id" : "LC006",
        "titulo" : "Piratas do Caribe",
        "ano de lancamento" : 2001,
        "Classificacao" : 7,
        "categoria" : "Aventura"
    }
    item_7= {
        "_id" : "LC007",
        "titulo" : "Curtindo a vida adoidado",
        "ano de lancamento" : 1987,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }

    item_8= {
        "_id" : "LC008",
        "titulo" : "Leon, o profissional",
        "ano de lancamento" : 1994,
        "Classificacao" : 10,
        "categoria" : "Drama"
    }
    item_9= {
        "_id" : "LC009",
        "titulo" : "Uma odiseia no espaço",
        "ano de lancamento" : 1968,
        "Classificacao" : 7.5,
        "categoria" : "Ficção Cientifica"
    }
    item_10= {
        "_id" : "LC010",
        "titulo" : "Interstellar",
        "ano de lancamento" : 2014,
        "Classificacao" : 7,
        "categoria" : "Ficcção Cientifica"
    }
    item_11= {
        "_id" : "LC011",
        "titulo" : "Clube dos cincos",
        "ano de lancamento" : 1987,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }

    item_12= {
        "_id" : "LC012",
        "titulo" : "Leon, o profissional",
        "ano de lancamento" : 1994,
        "Classificacao" : 10,
        "categoria" : "Drama"
    }
    item_13= {
        "_id" : "LC013",
        "titulo" : "Uma odisseia no espaço",
        "ano de lancamento" : 1968,
        "Classificacao" : 7.5,
        "categoria" : "Ficção Cientifica"
    }
    item_14= {
        "_id" : "LC014",
        "titulo": "Oldboy",
        "ano de lancamento" : 2003,
        "Classificacao" : 9,
        "categoria" : "Ação"
    }

    item_15= {
        "_id" : "LC015",
        "titulo" : "A origem",
        "ano de lancamento" : 2010,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_16= {
        "_id" : "LC016",
        "titulo" : "O mundo de Andy",
        "ano de lancamento" : 1999,
        "Classificacao" : 10,
        "categoria" : "Drama"
    }
    item_17= {
        "_id" : "LC017",
        "titulo" : "Joia Bruta",
        "ano de lancamento" : 2019,
        "Classificacao" : 8.0,
        "categoria" : "Ação"
    }

    item_18= {
        "_id" : "LC018",
        "titulo" : "A pequena miss sunshine",
        "ano de lancamento" : 2006,
        "Classificacao" : 9,
        "categoria" : "Comedia"
    }
    item_19= {
        "_id" : "LC019",
        "titulo" : "Tenet",
        "ano de lancamento" : 2020,
        "Classificacao" : 7,
        "categoria" : "Aventura"
    }
    item_20= {
        "_id" : "LC020",
        "titulo" : "Candy man",
        "ano de lancamento" : 2021,
        "Classificacao" : 8,
        "categoria" : "Drama"
    }
    lista=[]
    lista2=[]
    for i in range(20):
        lista.append(f"item_{i+1}")
        for x in range(len(lista)):
           lista2.append(dict(lista[x]))
           collection_name1.insert_one(lista2)
    print("Documento inserido!")