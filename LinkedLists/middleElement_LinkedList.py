'''
Given a singly linked list of N nodes. The task is to find the middle of the linked list. For example, if given linked list is 1->2->3->4->5 then the output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.
Question: https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
'''

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

# function should return index to the any valid peak element
def findMid(head):
    # Code here
    # return the value stored in the middle node
    twoStepJumper = head
    oneStepJumper = head
    while(twoStepJumper != None and twoStepJumper.next!=None ):
            twoStepJumper = twoStepJumper.next.next
            oneStepJumper = oneStepJumper.next
    
    return oneStepJumper.data