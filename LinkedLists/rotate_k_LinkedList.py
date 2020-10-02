# This function should rotate list counter-
# clockwise by k and return head node
def rotateList(head, k):
    # code here
    currPntr = head
    #connecting last & first nodes
    while(currPntr.next!=None):
        currPntr=currPntr.next
    currPntr.next = head
    
    #go to kth node & break the chain
    currPntr = head
    while(k-1):
        currPntr = currPntr.next
        k-=1
    newHead = currPntr.next
    currPntr.next = None
    return newHead
    