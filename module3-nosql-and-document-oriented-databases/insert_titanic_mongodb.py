import pymongo
import pandas as pd
import passwords

# import titanic df
df = pd.read_csv('titanic.csv')

# clean out my df name strings:
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')

#create rows of tuples from the df
def gen_row_tuples(df):
    rows = []
    for idx, vals in df.iterrows():
        row = [idx]
        
        for val in vals.values:
            row.append(val)
        row = tuple(row)
        rows.append(row)
    return rows

# create tuples from DF
tups = gen_row_tuples(df)

#some bug testing
# print(df.columns.tolist())
# print(tups[0])

#connect to db with 3.4
client = pymongo.MongoClient("mongodb://"+passwords.login+":"+passwords.password + "@cluster0-shard-00-00-spucf.mongodb.net:27017,cluster0-shard-00-01-spucf.mongodb.net:27017,cluster0-shard-00-02-spucf.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# populate mongodb
for tup in tups:
    dict_entry = {
        'Survived': tup[1] ,
        'Pclass': tup[2], 
        'Name': tup[3], 
        'Sex': tup[4], 
        'Age': tups[5], 
        'Siblings/Spouses Aboard': tups[6], 
        'Parents/Children Aboard': tups[7], 
        'Fare': tups[8]
    }
    db.test.insert_one(dict_entry)

#querry mongodb to confirm insert worked

print('The most eligible women on the Titanic: ')

ladies = list(db.test.find({
    'Pclass':1,
    'Sex': 'female',
    # 'Age' : {$gt:17},
    'Survived' : 1
},{'Name':1}))
print('There are %d eligible women.' % len(ladies) )
for lady in ladies[:5]:
    print('\n', lady['Name'])




