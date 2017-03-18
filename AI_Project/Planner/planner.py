class MonkeyBananaPlanner(object):
    monkey = "monkey"
    box = "box"
    bananaList = ["banana1", "banana2", "banana3"]
    posList = ["posa","posb","posc","posd"]
    heightList = ["low","high"]
    def __init__(self):
        pass

    def isMonkey(self,X):
        if X == self.monkey :
            return True
        return False
    def isBox(self,X):
        if X == self.box:
            return True
        return False
    def isBanana(self,X):
        if X in self.bananaList:
            return True
        return False

    def isPosition(self,X):
        if X in self.posList:
            return True
        return False

    def isHeight(self,X):
        if X in self.posList:
            return True
        return False

    def possGo(self,M,H,P):
        if self.isMonkey(M) and self.isHeight(H) and self.isPosition(P) and H == "low":
            return True
        return False

    def possPush(self,M,Mh,Mp,B,Bp):
        if self.isMonkey(M) and self.isHeight(Mh) and self.isPosition(Mp) and self.isPosition(Bp) \
                and self.isBox(B) and Mh == "low" \
                and Mp == Bp:
            return True
        return False
    
    def possClimbup(self):


d = MonkeyBananaPlanner()
print(d.isPosition("posd"))