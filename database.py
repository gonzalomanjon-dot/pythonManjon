from pymongo import MongoClient
import certifi 

MONGO_URI = 'mongodb+srv://dbManjon:<030706>@cluster0.veooafi.mongodb.net/?'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client['dbb_products_app']
    except:
        print('Error de conexion con la bdd') 
    return db
