import requests
import json
import pprint
import os

def gettone(text):
    """Takes input text and submits to IBM Watson Tone Analysis system.
    Expects environment variables BLUEMIXUSER, BLUEMIXPASS, and BLUEMIXTONEURL set
    to point to an enabled IBM Watson Tone Analysis setup.
    Returns JSON object of tone analysis output
    """
    user = os.environ['BLUEMIXUSER']
    passwd = os.environ['BLUEMIXPASS']
    url = os.environ['BLUEMIXTONEURL']
    headers = {"content-type": "text/plain"}
    try:
        r = requests.post(url, auth=(user,passwd),headers = headers,data=text)
        return str(r.text)
    except:
        return False
