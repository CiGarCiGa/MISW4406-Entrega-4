from flask import Response, Flask, request
import requests
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary
import time
import os
import re
import logging
import traceback

app = Flask(__name__)

def broker_host():
    return os.getenv('BROKER_HOST', default="35.196.17.46")

def broker_port():
    return os.getenv('BROKER_PORT', default="8080")

@app.route("/metrics")
def metrics():
    res = []
    url = f'http://{broker_host()}:{broker_port()}/admin/v2/persistent/public/default/'
    #print(url,flush=True)
    response = requests.get(url)
    #graphs['h'].observe()
    for topic in response.json():
        #print(topic,flush=True)
        topic_url=f'http://{broker_host()}:{broker_port()}/admin/v2/{topic.replace("://","/")}/stats'
        #print(topic_url,flush=True)
        topic_response = requests.get(topic_url)
        pending_messages = 0.0
        try:
            #print("Aqui estuvo carlos",flush=True)
            matches = re.findall('\"msgBacklog\": ?([\d]*)', str(topic_response.content), re.DOTALL)
            #print(str(matches))
            if matches:
                count = 0
                for i in matches:
                    #print(str(count))
                    count = count + int(i)
                pending_messages=count
            else:
                cal=topic_response.json()['msgInCounter']-topic_response.json()['msgOutCounter']
                if cal < 0:
                    print('Negative values for msgInCounter - msgOutCounter', flush=True)
                    pending_messages=0
                else:
                    pending_messages=topic_response.json()['msgInCounter']-topic_response.json()['msgOutCounter']
        except:
            print('No messages in the broker yet')
            traceback.print_exc()
        res.append(f'pending_messages_{topic.replace("://","/").replace("/","_").replace("-","_")} {"{:.1f}".format(pending_messages)}\n')
    return Response(res, mimetype="text/plain")

