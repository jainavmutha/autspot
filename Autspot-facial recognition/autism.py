import face_recog
from face_recog import Detect
import socket
from flask import Response
from flask import Flask,redirect
from flask import render_template
import open_harshitha
import sms_send
import threading
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://<USERNAME>:<Password>autspot.u42dncc.mongodb.net/?retryWrites=true&w=majority')
dbname = client['Autism']
collection_name = dbname["Userdata"]
dector = Detect()
lock = threading.Lock()

@app.route("/getemo")
def get_emotion():
    emotion  = dector.capture()
    print(emotion)
    myquery = { "name": "Sam Parker","emotion":str(emotion)}
    q_results = collection_name.find(myquery)
    results = list(q_results)
    if(len(results)!=0): 
        print(results[0]["solution"])
        solution = results[0]["solution"]
        mode = results[0]["mode"]
        emg_contact = results[0]["emg_number"]
        sms_send.send_alert(emg_contact)
        if(mode == "picture"):
            url = open_harshitha.gen_image(solution)
            print(url)
            return redirect(url)
        if(mode == "music"):
            return redirect("https://soundcloud.com/relaxdaily/relaxing-music-calm-studying-yoga")
        if(mode == "meditation"):
            return redirect("https://soundcloud.com/jack-kornfield/breathe-love-in-breathe-love-out-meditation-jack-kornfield?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing;auto_play=true")  
    else:
        print("Not found")
    return render_template("index.html")  


if __name__ == '__main__':
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host= local_ip,port=8000,debug=True,threaded=True)






