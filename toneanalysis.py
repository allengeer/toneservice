import requests
import json
import pprint
import os
import hashlib
import redis

def gettone(text):
    """Takes input text and submits to IBM Watson Tone Analysis system.
    Expects environment variables BLUEMIXUSER, BLUEMIXPASS, and BLUEMIXTONEURL set
    to point to an enabled IBM Watson Tone Analysis setup.
    Returns JSON object of tone analysis output
    """
    user = os.environ['BLUEMIXUSER']
    passwd = os.environ['BLUEMIXPASS']
    url = os.environ['BLUEMIXTONEURL']
    try:
        sidecar = os.environ['SIDECAR']
    except:
        sidecar = None
    headers = {"content-type": "text/plain"}
    if sidecar is not None:
        sha = hashlib.sha256(text).hexdigest()
        redisCache = redis.StrictRedis(host=sidecar, port=6379, db=0)
        cacheResponse = redisCache.get(sha)
        if cacheResponse is None:
            print "Cache Miss - %s" %sha
            try:
                r = requests.post(url, auth=(user, passwd), headers=headers, data=text)
                cacheResponse = str(r.text)
                redisCache.set(sha, cacheResponse)
            except:
                cacheResponse = None
                redisCache.set(sha, cacheResponse)
        else:
            print "Cache Hit - %s" %sha
        return cacheResponse
    else:
        try:
            r = requests.post(url, auth=(user, passwd), headers=headers, data=text)
            return str(r.text)
        except:
            return None
