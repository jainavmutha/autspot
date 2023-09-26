import socket
from flask import Response
from flask import Flask,redirect
from flask import render_template
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://<USERNAME>:<PASSWORD>autspot.u42dncc.mongodb.net/?retryWrites=true&w=majority')
dbname = client['Autism']
collection_name = dbname["Userdata"]

@app.route("/upload/<name>/<dob>/<age>/<type>/<date>/<behaviour>/<emotion>/<solution>/<mode>/<emg_name>/<emg_number>/<relationship>/<address>", methods=["POST", "GET"])
def upload_mongo(name,dob,age,type,date,behaviour,emotion,solution,mode,emg_name,emg_number,relationship,address):
    upload_item = {"name":str(name),"dob":str(dob),"age":str(age),"type":str(type),"date":str(date),"behaviour":str(behaviour),"emotion":str(emotion),"soulution":str(solution),"mode":str(mode),"emg_name":str(emg_name),"emg_number":emg_number,"relationship":str(relationship),"address":str(address)}
    collection_name.insert_one(upload_item)
    return redirect("http://www.google.com")

if __name__ == '__main__':
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host= local_ip,port=5000,debug=True,threaded=True)

