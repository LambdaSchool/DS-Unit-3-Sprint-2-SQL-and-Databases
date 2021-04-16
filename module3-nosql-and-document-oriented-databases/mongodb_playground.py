import pymongo 
import dns

client = pymongo.MongoClient("mongodb+srv://timrocar:AmI9EUqOUMcUTEdb@cluster0.suem0.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test


db.test.insert_one({'x':1})


db.test.count_documents({'x':1})


print(db.test.find({'x':1}))


max_doc = {
    'food': 'rhino',
    'color': 'orange',
    'number': 7
}


jim_doc = {
    'animal': 'rhino',
    'color': 'orange',
    'cities': ['New York', 'Chicago']
}


all_docs = [jim_doc, max_doc]


db.test.insert_many(all_docs)


list(db.test.find())


db.test.insert_one({
    'food': 'cookies',
    'color': 'orange'
})


list(db.test.find({'color': 'orange'}))


more_docs = []
for i in range(10):
    doc = {'even': i%2 ==0}
    doc = 



df.test.insert_many(more_docs)


list(db.test.find({'even': True, 'value': 0}))

list(db.test.find({'even': True, 'value': 1}))

list(db.test.find({'even': True}))