import os

PULSAR_ENV: str = 'PULSAR_ADDRESS'

def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")