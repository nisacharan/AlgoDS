"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    # Code here
    currNode = head
    nextNode = None
    prevNode = None
    cntr = 0
    while(currNode is not None and cntr < k):
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
        cntr+=1
    if(nextNode is not None):
        head.next = reverse(nextNode,k)
    
    return prevNode
