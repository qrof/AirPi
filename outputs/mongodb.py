import output
import datetime
from pymongo import MongoClient

class MongoDB(output.Output):
  requiredData = ["host","port","database"]
  optionalData = ["collection","username", "password"]
  def __init__(self,data):
    client = MongoClient(data["host"], int(data["port"]))
    db = client[data["database"]]
    if data["collection"]:
      self.collection = db[data["collection"]]
    else:
      self.collection = db.sensors
  def outputData(self,dataPoints):
    try:
      for i in dataPoints:
        i['date'] = datetime.datetime.utcnow()
        #print self.collection.insert(i)
    except Exception:
      return False
    return True
