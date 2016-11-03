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
print(c)