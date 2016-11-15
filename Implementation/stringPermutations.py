def permu(str,l,r):
    if l == r:
        print(str)
    else:
        for i in range(l,r+1):
            str = swap(str,l,i)
            permu(str,l+1,r)
            str = swap(str, l, i) #reverting changes

def swap(str,l,i):
    if l == i:
        return str
    str = str[:l] + str[i] + str[l+1:i]+str[l]+ str[i+1:]
    return str

str="ABcD"
permu(str,0,len(str)-1)