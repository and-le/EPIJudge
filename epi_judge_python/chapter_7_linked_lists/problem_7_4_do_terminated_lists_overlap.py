#!/usr/bin/env python
# coding: utf-8

# In[5]:


from list_node import ListNode


# In[6]:


def length(L):
    """
    Returns the length of the given list L.
    """
    cur = L
    length = 0
    while cur:
        length += 1
        cur = cur.next
        
    return length


def advance(L, k):
    """
    Returns a pointer to the kth node in the given list.
    If k > length(L), returns None.
    """
    cur = L
    i = 0
    while cur and i < k:
        i += 1
        cur = cur.next
        
    return cur

def overlapping_no_cycle_lists(L1, L2):
    """
    Returns the first overlapping node between L1 and L2, if one exists.
    Otherwise, returns None.
    
    Time: O(n), n = total number of nodes
    Space: O(1)
    """
    len_L1 = length(L1)
    len_L2 = length(L2)
    
    # The first overlapping node is found by advancing the longer list by 
    # abs(len_L1 - len_L2) nodes and then advancing both lists one node
    # at a time until there is a common node.
    cur_L1 = L1
    cur_L2 = L2
    
    if len_L1 > len_L2:
        cur_L1 = advance(L1, len_L1 - len_L2)
    elif len_L2 > len_L1:
        cur_L2 = advance(L2, len_L2 - len_L1)
    # No advancing is needed if both lists have the same length
    
    while cur_L1 and cur_L2:
        if cur_L1 == cur_L2:
            return cur_L1
        else:
            cur_L1 = cur_L1.next
            cur_L2 = cur_L2.next
    
    # If there were no common nodes, cur_L1 will be None
    return cur_L1   


# In[10]:


# Both lists have the same length, with an overlapping node in the middle.
n1_L1 = ListNode(3)
n2_L1 = ListNode(5)
n3_L1 = ListNode(7)

n1_L1.next = n2_L1
n2_L1.next = n3_L1

n1_L2 = ListNode(2)
n1_L2.next = n2_L1

overlapping_no_cycle_lists(n1_L1, n1_L2)


# In[11]:


# One list is longer than the other
n1_L1 = ListNode(3)
n2_L1 = ListNode(5)
n3_L1 = ListNode(7)
n4_L1 = ListNode(9)

n1_L1.next = n2_L1
n2_L1.next = n3_L1
n3_L1.next = n4_L1


n1_L2 = ListNode(2)
n1_L2.next = n3_L1

overlapping_no_cycle_lists(n1_L1, n1_L2)


# In[ ]:




