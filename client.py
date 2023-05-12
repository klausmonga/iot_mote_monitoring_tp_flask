import requests
import json 




def get_all_motes():
    headers = {"Accept":"application/json"}
    req = requests.get("http://127.0.0.1:5000/iot/all_mote",headers)
    rep = req.json()
    print(rep['reponse'])

def create_mote(mote):
    
    res = requests.post('http://localhost:5000/iot/add_mote/', json={"motes":mote})
    if res.ok:
        print(res.json())

def update_mote_name(id,name):
    headers = {"Accept":"application/json"}
    req = requests.get(f"http://127.0.0.1:5000/iot/update_name/{id}/{name}",headers)
    rep = req.json()
    print(rep['reponse'])

#IT GOING TO DELETE THE MOTE
def unlink_mote(id):
    headers = {"Accept":"application/json"}
    req = requests.get(f"http://127.0.0.1:5000/iot/update_name/{id}/{name}",headers)
    rep = req.json()
    print(rep['reponse'])


input =int(input("PUT 1 TO LIST ALL MOTES \n PUT 2 TO create one mote \n PUT 3 TO edit a MOTE \n PUT 4 TO delete A MOTE BY ID : \n"))

if input == 1:
    get_all_motes()
elif input == 2:
    mote = {
        "id":5,
        "name" : "Mote kin",
        "state": "UP",
        "uptime": "2 Minutes"
    }
    create_mote(mote)
elif input == 3:
    update_mote_name(3,"kabulamenshi")
elif input == 4:
    unlink_mote(2)