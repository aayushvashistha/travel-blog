from pymongo import MongoClient
def get_db_handle(host, port):

 client = MongoClient(host=host,
                      port=int(port),
                    #   username=username,
                    #   password=password
                     )
 db_handle = client['desiwanderer']
 
 return db_handle