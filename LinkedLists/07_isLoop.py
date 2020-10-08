'''
	Your task is to detect if any loop is present 
	in the given linked list.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: True or False (boolean)
'''
def detectLoop(head):
    #code here
    slowPtr = head
    fastPtr = head
    while(fastPtr and slowPtr and fastPtr.next ):
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next
        if(fastPtr is slowPtr):
            return True
    return False