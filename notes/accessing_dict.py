import pprint

db = {
        'bob': {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'},
        'sue': {'pay': 50000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
        }

pprint.pprint(db)
print(db)

for key in db:
    print(key, '=>', db[key]['name'])

for record in db.values():
    print(record['pay'])

x = [db[key]['name'] for key in db]
print(x)

y = [rec['name'] for rec in db.values()]
print(y)
