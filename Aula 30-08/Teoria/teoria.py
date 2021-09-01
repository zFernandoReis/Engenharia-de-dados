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
        "titulo" : "Robocop",
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
    ################################################ fim dos filmes ###################################

    ############################################### começa series ######################################
    item_21= {
        "_id" : "LC021",
        "titulo" : "Game of Thrones",
        "ano de lancamento" : 2012,
        "Classificacao" : 6,
        "categoria" : "Drama"
    }

    item_22= {
        "_id" : "LC022",
        "titulo" : "Todo mundo odeia o chris",
        "ano de lancamento" :2013 ,
        "Classificacao" : 8 ,
        "categoria" : "comedia"
    }
    item_23= {
        "_id" : "LC023",
        "titulo" : "The Boys",
        "ano de lancamento" : 2019,
        "Classificacao" : 9,
        "categoria" : "Drama"
    }
    item_24= {
        "_id" : "LC024",
        "titulo" : "The walking dead",
        "ano de lancamento" : 2012,
        "Classificacao" : 9,
        "categoria" : "Ação"
    }

    item_25= {
        "_id" : "LC025",
        "titulo" : "Atlanta",
        "ano de lancamento" : 2016,
        "Classificacao" : 8.3,
        "categoria" : "Drama"
    }
    item_26= {
        "_id" : "LC026",
        "titulo" : "Eu a patro e as crianças",
        "ano de lancamento" : 2013,
        "Classificacao" : 7,
        "categoria" : "Comedia"
    }
    item_27= {
        "_id" : "LC027",
        "titulo" : "Chaves",
        "ano de lancamento" : 1984,
        "Classificacao" : 8,
        "categoria" : "Comedia"
    }

    item_28= {
        "_id" : "LC028",
        "titulo" : "Chapolin",
        "ano de lancamento" : 1962,
        "Classificação" : 9,
        "categoria" : "Drama"
    }
    item_29= {
        "_id" : "LC029",
        "titulo" : "Smallville",
        "ano de lancamento" : 2001,
        "Classificacao" : 5,
        "categoria" : "Aventura"
    }
    item_30= {
        "_id" : "LC030",
        "titulo" : "Invencivel",
        "ano de lancamento" : 2021,
        "Classificacao": 9,
        "categoria" : "Ação"
    }
    item_31= {
        "_id" : "LC031",
        "titulo" : "Stargirl",
        "ano de lancamento" : 2020,
        "Classificacao" : 4,
        "categoria" : "Aventura"
    }

    item_32= {
        "_id" : "LC032",
        "titulo" : "Lúcifer",
        "ano de lancamento" : 2016,
        "Classificacao" : 8.5,
        "categoria" : "Comedia"
    }
    item_33= {
        "_id" : "LC033",
        "titulo" : "You",
        "ano de lancamento" : 2018,
        "Classificacao" : 9,
        "categoria" : "Suspense"
    }
    item_34= {
        "_id" : "LC034",
        "titulo" : "Preacher",
        "ano de lancamento" : 2016,
        "Classificacao" : 9,
        "categoria" : "Ação"
    }

    item_35= {
        "_id" : "LC035",
        "titulo" : "Atypical",
        "ano de lancamento" : 2019,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_36= {
        "_id" : "LC036",
        "titulo" : "Naruto",
        "ano de lancamento" : 2009,
        "Classificacao" : 7,
        "categoria" : "Aventura"
    }
    item_36= {
        "_id" : "LC036",
        "titulo" : "Dragon ball Z",
        "ano de lancamento" : 2002,
        "Classificacao" : 9.5,
        "categoria" : "Ação"
    }
    item_37= {
        "_id" : "LC037",
        "titulo" : "Erased",
        "ano de lancamento" : 2016,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_38= {
        "_id" : "LC038",
        "titulo" : "Death Note",
        "ano de lancamento" : 2008,
        "Classificacao" : 9.5,
        "categoria" : "Policial"
    }
    item_39= {
        "_id" : "LC039",
        "titulo" : "Hunter x Hunter",
        "ano de lancamento" : 2019,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_40= {
        "_id" : "LC040",
        "titulo" : "Beastrars",
        "ano de lancamento" : 2018,
        "Classificacao" : 9.5,
        "categoria" : "Aventura"
    }
    item_41= {
        "_id" : "LC040",
        "titulo" : "Beastrars",
        "ano de lancamento" : 2018,
        "Classificacao" : 9.5,
        "categoria" : "Aventura"
    }
    item_42= {
        "_id" : "LC042",
        "titulo" : "No Game No Life",
        "ano de lancamento" : 2015,
        "Classificacao" : 8.2,
        "categoria" : "Aventura"
    }
    item_43= {
        "_id" : "LC043",
        "titulo" : "Attack on titan",
        "ano de lancamento" : 2014,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    item_44= {
        "_id" : "LC044",
        "titulo" : "One punch man",
        "ano de lancamento" : 2017,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }
    item_45= {
        "_id" : "LC045",
        "titulo" : "Noragami",
        "ano de lancamento" : 2018,
        "Classificacao" : 7,
        "categoria" : "Ação"
    }
    item_46= {
        "_id" : "LC046",
        "titulo" : "Kuroko no Basket",
        "ano de lancamento" : 2015,
        "Classificacao" : 9.5,
        "categoria" : "Aventura"
    }
    item_47= {
        "_id" : "LC047",
        "titulo" : "Bakemonogatari",
        "ano de lancamento" : 2015,
        "Classificacao" : 9.5,
        "categoria" : "Aventura"
    }
    item_48= {
        "_id" : "LC048",
        "titulo" : "Fullmetal Alchimist",
        "ano de lancamento" : 2013,
        "Classificacao" : 8.2,
        "categoria" : "Aventura"
    }
    item_49= {
        "_id" : "LC049",
        "titulo" : "Boku no Hero Academia",
        "ano de lancamento" : 2014,
        "Classificacao" : 9.5,
        "categoria" : "Açao"
    }
    item_50= {
        "_id" : "LC050",
        "titulo" : "Beki",
        "ano de lancamento" : 2017,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }
    item_51= {
        "_id" : "LC051",
        "titulo" : "Boruto",
        "ano de lancamento" : 2019,
        "Classificacao" : 7,
        "categoria" : "Ação"
    }
    item_52= {
        "_id" : "LC052",
        "titulo" : "Tokyo Ghoul",
        "ano de lancamento" : 2017,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }
    item_53= {
        "_id" : "LC053",
        "titulo" : "Nanatsu no taizai",
        "ano de lancamento" : 2018,
        "Classificacao" : 7,
        "categoria" : "Aventura"
    }
    item_54= {
        "_id" : "LC054",
        "titulo" : "Soul Eater",
        "ano de lancamento" : 2013,
        "Classificacao" : 6,
        "categoria" : "Ação"
    }
    item_55= {
        "_id" : "LC055",
        "titulo" : "Sakura Card Captors",
        "ano de lancamento" : 2015,
        "Classificacao" : 8.3,
        "categoria" : "Aventura"
    }
    item_56= {
        "_id" : "LC056",
        "titulo" : "Barakamon",
        "ano de lancamento" : 2011,
        "Classificacao" : 10,
        "categoria" : "Aventura"
    }
    item_57= {
        "_id" : "LC057",
        "titulo" : "Under Pretender",
        "ano de lancamento" : 2018,
        "Classificacao" : 9.5,
        "categoria" : "Açao"
    }
    item_58= {
        "_id" : "LC058",
        "titulo" : "ReLIFE",
        "ano de lancamento" : 2018,
        "Classificacao" : 8,
        "categoria" : "Aventura"
    }
    item_59= {
        "_id" : "LC059",
        "titulo" : "Samurai X",
        "ano de lancamento" : 2019,
        "Classificacao" : 7,
        "categoria" : "Ação"
    }
    item_60= {
        "_id" : "LC060",
        "titulo" : "jojo bizzare adventure",
        "ano de lancamento" : 2019,
        "Classificacao" : 7,
        "categoria" : "Aventura"
    }

    ############################################# Fim de Series ####################
    ############################################## Começo Musicas ########################
    collection_name1.insert_many([item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11,item_12,item_13,item_14,item_15,item_16,item_17,item_18,item_19,item_20])
    print("Documento inserido!")

   

    