def get_database():
    from pymongo import MongoClient
    import pymongo

    # Forneça o url do atlas mongodb para conectar python a mongodb usando pymongo
    CONNECTION_STRING = "mongodb+srv://fernando-teste:teste-fernando@cluster0.ulaja.mongodb.net/myFirstDatabase"

    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cria o banco de dados.
    
    return client['soulcodeTeste2']
  
'''
def mostrarDocumentos():
    dbname = get_database()
    collection_name = dbname["itens_mysql_export2"]
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)
'''
from mysql.connector import connect
import MySQLdb


db = MySQLdb.connect(host="185.201.11.44", user="u781216269_rootx", 
   passwd="h5S3J#oP1@", db="u781216269_library")

cursor = db.cursor()
cursor.execute("SELECT * FROM `admin`")
numrows = int(cursor.rowcount)
linhas = cursor.fetchall()

print("Número total de registros encontrados: ", cursor.rowcount)
print("\nMostrand resultados...")
'''
i=0
for linha in linhas:
   print("ID: ", linha[0])
   print("Dado_1: ", linha[1])
   print("ISBN: ", linha[4])    
   print("Preço R$ : ", linha[5])
'''
def get_valoresql():
    #dbname = get_database()
    #collection_name = dbname["itens_mysql_export2"]  
    for linha in linhas:     
        item_1 = {
        "_id": linha[0], 
        "dado_1": linha[1],
        "ISBN": linha[4],
        "Preço": linha[5]
        }
    return item_1

dbname = get_database()
collection_name = dbname["itens_mysql_export2"]  
collection_name.insert_one(get_valoresql())