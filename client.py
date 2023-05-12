import requests
import json 

headers = {"Accept":"application/json"}
a=int(input("Saisir un nombre : "))
b=int(input("Saisir un nombre : "))

req = requests.get(f"http://127.0.0.1:5000/api/add/{a}/{b}",headers)
rep = req.json()
print(f"La somme de {a} + {b}= {rep['reponse']}")


import requests
res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
if res.ok:
    print(res.json())