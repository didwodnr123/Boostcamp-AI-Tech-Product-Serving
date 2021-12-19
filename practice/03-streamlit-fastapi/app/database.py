from pymongo import MongoClient
import certifi

def run_db():
    ca = certifi.where()
    client = MongoClient('mongodb+srv://jadon:aiit@cluster0.13mh6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
    db = client.aiit
    evidence = db.evidence
    return evidence

def insert2db(keyword, results, collection):
    docs = []
    for res in results:
            docs.append({
                "keyword": keyword,
                "comment": res['comment'],
                "label": res['label'],
                "score": res['score']
            })
    collection.insert_many(docs)