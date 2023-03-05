import time
import os

def time_millis():
    return int(time.time() * 1000)

PULSAR_ENV: str = 'PULSAR_ADDRESS'

def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")