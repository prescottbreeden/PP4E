# initialize data to be stored in files, pickles, shelves

# records
bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue = {'pay': 50000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
tom = {'pay': 0, 'job': 'None', 'age': 45, 'name': 'Tom'}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])
