import output
import requests
import json
import logging

class Thingspeak(output.Output):
  requiredData = ["APIKey","FeedID"]
  optionalData = []
  def __init__(self,data):
    self.APIKey=data["APIKey"]
    self.FeedID=data["FeedID"]
    # try:
    #   import http.client as http_client
    # except ImportError:
    # # Python 2
    #   import httplib as http_client
    # http_client.HTTPConnection.debuglevel = 1
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
  def outputData(self,dataPoints):
    arr = {}
    for idx, val in enumerate(dataPoints, 1):
      arr["field" + str(idx)] = str(val["value"])
    a = json.dumps(arr)
    try:
      z = requests.post("https://api.thingspeak.com/update.json",headers={"X-THINGSPEAKAPIKEY":self.FeedID, 'content-type': 'application/json'},data=a)
      if z.text=="0":
        print "Thingspeak Error: " + z.text
        return False
    except Exception:
      return False
    return True
