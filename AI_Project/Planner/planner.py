#import random
class IndivObj():
    def __init__(self,name,pos,height,holds=[]):
        self.n = name
        self.p = pos
        self.h = height
        self.holds = holds

class State():
    def __init__(self,m,b1,b2,b3,bx):
        self.Plan = []
        self.m = m
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.bx = bx

    def convertPlanToSituationCalculus(self):
        pass

class MonkeyBananaPlanner(object):
    monkey = "monkey"
    box = "box"
    bananaList = ["banana1", "banana2", "banana3"]
    posList = ["posa","posb","posc","posd"]
    heightList = ["low","high"]
    goalState = []
    setAction = []

    def __init__(self,flName):
        self.m = IndivObj("monkey","posa","low",[])
        self.b1 = IndivObj("banana1", "posa", "high", [])
        self.b2 = IndivObj("banana2", "posb", "high", [])
        self.b3 = IndivObj("banana3", "posc", "high", [])
        self.bx = IndivObj("banana3", "posd", "low", [])
        self.currState = State(self.m,self.b1,self.b2,self.b3,self.bx)
        self.goalState = self.readGoalStateFromFile(flName)

    def plan(self):
        try:
            #Devise plan here
            i = 0
            self.planRecurr(i,self.currState)
        except:
            print("Exception")

    def planRecurr(self,i,tempState):
        if i == 20:
            return
        if self.isGoalState(tempState):
            tempState.convertPlanToSituationCalculus()
            raise Exception("Plan Complete")

        if self.possClimbUp(tempState.m.n,tempState.m.h,tempState.m.p, tempState.bx.n, tempState.bx.p):
            self.planRecurr(i+1, self.climbUp(tempState))
            tempState.m.h = self.heightList[1]

        if self.possClimbDown(tempState.m.n,tempState.m.h,tempState.m.p, tempState.bx.n, tempState.bx.p):
            self.planRecurr(i+1, self.climbDown(tempState))
            tempState.m.h = self.heightList[0]
        


    def climbUp(self,tempState):
        tempState.m.h = self.heightList[1]
        return tempState

    def climbDown(self, tempState):
        tempState.m.h = self.heightList[0]
        return tempState

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

    def possClimbUp(self,M,Mh,Mp,B,Bp):
        if self.isMonkey(M) and self.isHeight(Mh) and self.isPosition(Mp) \
                and self.isPosition(Bp) and self.isBox(B) and Mh == "low" \
                and Mp == Bp:
            return True
        return False

    def possClimbDown(self,M,Mh,Mp,B,Bp):
        if self.isMonkey(M) and self.isHeight(Mh) and self.isPosition(Mp) and self.isPosition(Bp) \
                and self.isBox(B) and Mh == "high" \
                and Mp == Bp:
            return True
        return False

    def possGrasp(self,M,Mp,Mh,MHolds, B,Bp,Bh):
        if self.isMonkey(M) and self.isHeight(Mh) and self.isPosition(Mp) and self.isPosition(Bp) \
                and self.isBanana(B) and self.isHeight(Bh) and Mh == "high" \
                and Mp == Bp and B not in MHolds:
            return True
        #Check if monkey does not hold this items!
        return False

    def possUngrasp(self, M, Mp, Mh,MHolds, B, Bp, Bh):
        if self.isMonkey(M) and self.isHeight(Mh) and self.isPosition(Mp) and self.isPosition(Bp) \
                and self.isBanana(B) and self.isHeight(Bh) \
                and Mp == Bp and B in MHolds:
            return True
        #check if monkey holds this items!
        return False

    def isGoalState(self,tempState):
        for i in self.goalState:
            stmnt = i.split()
            if stmnt[0] == "holds":
                if len(set(stmnt[1][1:-1].split(',')).difference(tempState.m.holds)) > 0:
                    return False
            else:
                if self.isMonkey(stmnt[1]):
                    if tempState.m.p != stmnt[2] or tempState.m.h != stmnt[3]:
                        return False
                elif self.isBox(stmnt[1]):
                    if tempState.bx.p != stmnt[2] or tempState.bx.h != stmnt[3]:
                        return False
                elif self.isBanana(stmnt[1]):
                    if tempState.b1.n == stmnt[1]:
                        if tempState.b1.p != stmnt[2] or tempState.b1.h != stmnt[3]:
                            return False
                    elif tempState.b2.n == stmnt[1]:
                        if tempState.b2.p != stmnt[2] or tempState.b2.h != stmnt[3]:
                            return False
                    else:
                        if tempState.b3.p != stmnt[2] or tempState.b3.h != stmnt[3]:
                            return False

    def readGoalStateFromFile(self, flName):
        data = [line.rstrip('\n') for line in open(flName)]
        return data

d = MonkeyBananaPlanner('goal1.txt')
d.plan()