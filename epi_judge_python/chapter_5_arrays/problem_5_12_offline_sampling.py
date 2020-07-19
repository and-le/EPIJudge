#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[4]:


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def random_subset(A, k):
    """
    Returns a random subset of size k. All subsets of size k are equally likely.
    The subset will returned in the first k elements of A
    Time: O(k)
    Space: O(1)
    """
    
    # Pick the k elements
    for i in range(k):
        # Pick a random index in the interval [i, n - 1]
        idx = random.randint(i, len(A) - 1) 
        
        # Move the chosen element to the front.
        swap(A, i, idx)
        
        # All subsets of size k are equally likely because for each i,
        # all elements had equal probability of being chosen
    return A


# In[5]:


random_subset([0, 1, 2, 3], 3)


# In[6]:


random_subset([0, 1, 2, 3], 3)


# In[7]:


random_subset([0, 1, 2, 3], 3)


# In[8]:


random_subset([0, 1, 2, 3], 3)


# In[ ]:





# In[ ]:




