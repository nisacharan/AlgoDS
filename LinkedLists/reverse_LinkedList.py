

def reverseList(head):
    # Code here
    prevNode = None
    currNode = head
    nextNode = None
    while(currNode!=None):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    head = prevNode
    return head
