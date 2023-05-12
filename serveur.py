from flask import Flask,jsonify,request

app = Flask(__name__)

MOTES = [
        {
            "id":1,
            "name" : "Mote Kamnyola",
            "state": "UP",
            "uptime": "49 Minutes"
        },
        {
            "id":2,
            "name" : "Mote MAMAN YEMO",
            "state": "UP",
            "uptime": "29 Minutes"
        },
        {
            "id":3,
            "name" : "Mote LIKASI",
            "state": "DOWN",
            "uptime": "0 Minute"
        },
        {
            "id":4,
            "name" : "Mote GECAMINE",
            "state": "UP",
            "uptime": "22 Minutes"
        },

    ]
@app.route("/",methods=['GET'])
def bonjour():
    return "Bonjour tout le monde"


@app.route("/iot/all_mote",methods=['GET'])
def get_all_mote():
    return jsonify({"result":MOTES})

@app.route("/iot/add_mote/",methods=['POST'])
def add_new_mote():
    new_motes = request.json
    return jsonify(new_motes['motes'])


@app.route("/iot/update_name/<id>/<name>", methods=["PUT"])
def update_mote_name(id,name):
    motes_updated = []
    for mote in MOTES:
        if mote['id'] == id:
            mote['name'] = name
            motes_updated.append(mote)
        else:
            motes_updated.append(mote)
    
    return jsonify(motes_updated)

@app.route("/iot/crossout_mote/<id>", methods=["DELETE"])
def delete_mote(id):
    motes_updated = []
    for mote in MOTES:
        if mote['id'] == id:
            continue
        else:
            motes_updated.append(mote)
    
    return jsonify(motes_updated)
    
if __name__ == "__main__":
    app.run(debug=True)