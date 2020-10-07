''' 
    Given two singly linked lists of size N and M, 
    write a program to get the point where two linked lists intersect each other.
'''
'''
Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.
    
    {
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

'''
LOGIC: The idea is to ignore the starting entries of the longer list (merge point can't be there), 
so that the two pointers are an equal distance from the end of the list. 
Then move them forwards until they merge.
lenA = count(listA) //iterates list A
lenB = count(listB) //iterates list B

ptrA = listA
ptrB = listB

//now we adjust either ptrA or ptrB so that they are equally far from the end
while(lenA > lenB):
    ptrA = ptrA->next
    lenA--
while(lenB > lenA):
    prtB = ptrB->next
    lenB--

while(ptrA != NULL):
    if (ptrA == ptrB):
        return ptrA //found merge point
    ptrA = ptrA->next
    ptrB = ptrB->next
'''


def intersetPoint(head_a,head_b):

    # getting lengths
    currA = head_a
    currB = head_b
    
    lenA=0
    while(currA is not None):
        lenA+=1
        currA = currA.next
    lenB=0
    while(currB is not None):
        lenB+=1
        currB = currB.next
    
    # now we adjust either ptrA or ptrB so that they are equally far from the end

    currA = head_a
    currB = head_b
    
    while(lenA > lenB):
        currA = currA.next
        lenA-=1
        
    while(lenB > lenA):
        currB = currB.next
        lenB-=1

    # adjusted pointers. Now we go forward till we meet :) 
    while(currB is not None):
        if (currA == currB):
            return currB.data #found merge point
        currA = currA.next
        currB = currB.next


