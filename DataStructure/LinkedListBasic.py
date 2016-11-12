#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def createLinkedList(arr):
    s = Node(arr[0])
    head = s
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        s.next = temp
        s = temp
    return head

def print_list(head):
    NodeN = head
    if NodeN != None:
        print(NodeN.data)
    while NodeN.next != None:
        NodeN = NodeN.next
        print(NodeN.data)

newHead = createLinkedList([1,2,3])
while newHead != None:
    print(newHead.data)
    newHead = newHead.next


