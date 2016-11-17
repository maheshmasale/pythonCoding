class Bottle(object):
    def __init__(self,id):
        self.id = id
        self.isPoisoned = False

    def setToPoisoned(self):
        self.isPoisoned = True

    def getId(self):
        return self.id

    def isBottlePoisoned(self):
        return self.isPoisoned

class TestStrip(object):
    DAYS_FOR_RESULT = 7
    dropsByDay = []

    def __init__(self,id):
        self.id = id

    def getID(self):
        return self.id

    def increaseSizeByDays(self,day):
        while len(TestStrip.dropsByDay) <= day:
            TestStrip.dropsByDay.append([])

    def addDropsOnDay(self,dayGiven,bottle):
        self.increaseSizeByDays(dayGiven)
        TestStrip.dropsByDay[dayGiven].append(bottle)

    def hasPoison(self, bottles = []):
        for i in bottles:
            if i.isBottlePoisoned():
                return True
        return False

    def getLastWeeksBottles(self,day):
        if day < TestStrip.DAYS_FOR_RESULT:
            return []
        return TestStrip.dropsByDay[day-TestStrip.DAYS_FOR_RESULT]

    def isPsitiveOnDay(self,day):
        testDay = day - TestStrip.DAYS_FOR_RESULT
        if testDay < TestStrip.DAYS_FOR_RESULT or testDay >= len(TestStrip.dropsByDay):
            return False

        for i in range(testDay+1):
            if TestStrip.hasPoison(TestStrip.dropsByDay[i]):
                return True
        return False

    