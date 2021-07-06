from pymongo import MongoClient

def connect_to_database():

    connection = "mongodb+srv://atlas:123123123@atlas.bbqo9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(connection)
    
    db = client.gettingStarted
    
    player_db = db.player    
    
    player = {
        "nome": "Guilherme Cavalheiro",
        "posicao": "Atacante"
    }

    player_db.insert_one(player)

    return client

if __name__ == "__main__":
    connect_to_database()