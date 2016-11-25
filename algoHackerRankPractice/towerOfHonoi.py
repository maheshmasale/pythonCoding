def moveTowers(h,fromPol,toPole,withPole):
    if h > 0:
        moveTowers(h-1, fromPol, withPole, toPole)
        moveTower(fromPol,toPole)
        moveTowers(h-1,withPole,toPole,fromPol)

def moveTower(fromPole,toPole):
    print("Move disk from ",fromPole," to ",toPole)
7
moveTowers(2,"A","B","C")