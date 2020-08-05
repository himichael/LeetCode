class UndergroundSystem(object):
    def __init__(self):
        self.map = dict()
        self.res = dict()

    def checkIn(self, id, stationName, t):
        self.map[id] = (stationName,t)

    def checkOut(self, id, stationName, t):
        start_name,start_time = self.map[id]
        key = (start_name,stationName)
        if key not in self.res:
            self.res[key] = [t-start_time,1]
        else:
            tmp = self.res[key]
            self.res[key] = [tmp[0]+t-start_time, tmp[1]+1]

    def getAverageTime(self, startStation, endStation):
        key = (startStation,endStation)
        return 1.0 * self.res[key][0]/self.res[key][1]