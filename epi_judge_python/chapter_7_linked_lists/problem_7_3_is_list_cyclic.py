#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Problem 7.3 : Testing a linked list for having a cycle
"""
from list_node import ListNode


# In[18]:


def has_cycle(L):
    """
    Returns None if the given list does not have a cycle; otherwise,
    returns the first node in the cycle if the list does contain
    a cycle.
    
    Time: O(n)
    Space: O(1)
    """    
    # If list is just one node and cyclic
    if L.next is L:
        print(f"List is just 1 node and cyclic")
        return L
    
    # Use two iterators, one fast and one slow. If there is a cycle,
    # then the fast iterator will evntually overlap with the slow
    # iterator.
    fast = L
    slow = L
    while fast:
        print(f"Still in first loop")

        fast = fast.next
        
        # Check for a cycle or if the end of the linked list was reached
        if (fast is slow) or (not fast):
            break
        
        # Advance fast one more node
        fast = fast.next
        
        # Check for a cycle
        if (fast is slow) or (not fast):
            break
            
        # Advance slow
        slow = slow.next
        
    print("Exited first loop")
        
    
    # If there is no cycle, fast will be None
    if not fast:
        print(f"No cycle")
        return None
        
    # To find the first node in the cycle, first determine the length of the cycle
    cycle_len = 1
    curr = fast.next
    while curr is not fast:
        cycle_len += 1
        curr = curr.next
        
    print(f"Cycle length = {cycle_len}")
    
    # Determine the first node in the cycle, using a node at the start of the list, and a 
    # node of cycle_len nodes away. When iterators to both nodes overlap, the start node
    # has been found.
    
    head = L
    cycle_start = L
    i = 0
    while i < cycle_len:
        cycle_start = cycle_start.next
        i += 1
    
    while head is not cycle_start:
        head = head.next
        cycle_start = cycle_start.next
        
    return cycle_start


# In[20]:


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3 # Cycle start
has_cycle(n1)


# In[ ]:





# In[ ]:




