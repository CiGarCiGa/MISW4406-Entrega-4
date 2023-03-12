from flask import Response, Flask, request
import requests
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary
import time
import os

app = Flask(__name__)

def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

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
            pending_messages=topic_response.json()['msgInCounter']-topic_response.json()['msgOutCounter']
        except:
            print('No messages in the broker yet')
        res.append(f'pending_messages_{topic.replace("://","/").replace("/","_").replace("-","_")} {"{:.1f}".format(pending_messages)}\n')
    return Response(res, mimetype="text/plain")

