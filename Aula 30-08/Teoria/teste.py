def get_database():
    from pymongo import MongoClient
    import pymongo

    from pymongo import MongoClient   
    CONNECTION_STRING = "mongodb+srv://fernando-teste:fernando-teste@cluster0.ulaja.mongodb.net/myFirstDatabase"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#Conexão como cliente

    return client['soulcodeTeste2']#base de dados

if __name__ == "__main__":
    dbname = get_database()

    collection_name = dbname["itens_soulcode"]
    print("Base de dados criada!")

    item_1= {
        "_id" : "LC001",
        "titulo" : "Laranja mecânica",
        "ano de lancamento" : 1972,
        "Classificacao" : 9.5,
        "categoria" : "Drama"
    }
    collection_name.insert_one(item_1)
    print("Documento inserido!")