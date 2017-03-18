# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    stackArr = []
    #counter to insert "-" at k=1th position from end
    counter = 0
    #running for loop from end of string to start
    for i in range(len(S)-1,-1,-1):
        if S[i] != "-":
            if counter == K:
                stackArr.append("-")
                counter = 0
            stackArr.append(S[i].capitalize())
            counter = counter+ 1
    #reversed() takes O(N) time to reverse the given array so it should be fine to use here.
    return "".join(reversed(stackArr))


#str = "242424"
#str = "-r--"
str = "-11"
print(solution(str,1))