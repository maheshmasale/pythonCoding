import json
import time

class deduplicator(object):
    def __init__(self,dataFilePath):
        self.data = {"leads" : self.deduplicateIt(self.parseJSON((self.readFromFile(dataFilePath)))["leads"])}
        print(self.data)

    def deduplicateIt(self,dataArr):
        print(len(dataArr))
        dictData = {}
        for itr in dataArr:
            key = str(len(itr["_id"]))+itr["_id"]+str(len(itr["email"]))+itr["email"]
            if key not in dictData:
                dictData[key] = itr
            else:
                if self.compareDates(dictData[key]["entryDate"],itr["entryDate"]):
                    dictData[key] = itr
        print(len(dictData.values()))
        return dictData.values()

    def compareDates(self, dateStr1,dateStr2):
        dateStr1 = dateStr1[:-3]+dateStr1[-2:]
        dateStr2 = dateStr2[:-3]+dateStr2[-2:]
        tm1 = time.strptime(dateStr1, "%Y-%m-%dT%H:%M:%S%z")
        tm2 = time.strptime(dateStr2, "%Y-%m-%dT%H:%M:%S%z")
        if tm1 == tm2:
            if tm1.tm_gmtoff > tm2.tm_gmtoff:
                return False
            else:
                return True
        elif tm1 < tm2:
            return True
        else:
            return False

    def parseJSON(self,dataStr):
        return json.loads(dataStr)

    def readFromFile(self,path):
        with open(path) as file:
            data = file.read()
        return data

    def convertToJson(self):
        return json.dumps(self.data, default=self.jdefault)
        #return json.dumps(self.data)

dedup = deduplicator("leads.json")