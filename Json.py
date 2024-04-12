import json
# Deserialization
with open ("people.json",mode = "r", encoding = "UTF-8-sig") as file:
    data= json.loads(file.read()) #load  json string
    #Hoặc 
    #data = json.load(file) # load 1 file json về dạng object để python có thể hiểu được
    print(data)
    print(type(data))
# Serialization
dulieu = {'name': 'Guido van Rossum', 'age': 65, 'degree': ['mathematics', 'computer science'], 'retired': True, 'carrer': {'google': {'from': 1999, 'to': 2013}, 'dropbox': {'from': 2013, 'to': 2019}}}
with open ("luutru_file.json",mode = "w", encoding = "UTF-8-sig") as luutru:
    json.dump(dulieu,luutru)
string_json = json.dumps(dulieu,indent=4)
print(string_json)
print(type(string_json))