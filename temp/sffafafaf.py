s = "aabb"
t = "ab"
import re
c = 0
s = s.replace()
while True:
    if t in s:
        s = re.sub(t,"",s)
        c += 1
    else:
        break
#print(c)

def strTrunc(strInp):
    cnt = 0
    strInp += " "  # inserting dummy character
    strNew = ""
    for i in range(len(strInp) - 1):
        if strInp[i] == strInp[i + 1]:
            cnt += 1
        else:
            strNew += str(cnt) + strInp[i]
            cnt = 0
