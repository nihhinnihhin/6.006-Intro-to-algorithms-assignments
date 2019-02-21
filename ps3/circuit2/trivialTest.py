# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:02:39 2018

@author: Hinson
"""


class RangeIndex(object):
    """Sorted array-based range index implementation."""
    def __init__(self):
        """Initially empty range index."""
        self.data=[]
        
    def add(self, key):
        """Inserts a key in the range index."""
        if key is None:
            raise ValueError('Cannot insert None in the index')
        self.data.insert(self._binary_search(key),key)
        
    def remove(self, key):
        """Removes a key from the range index."""
        index=self._binary_search(key)
        if index < len(self.data) and self.data[index] == key:
            self.data.pop(index)
    
    
    def list(self, low_key, high_key):
        """List of Values for the keys that fall within [low_key, high_key]."""
        low_index =self._binary_search(low_key)
        high_index =self._binary_search(high_key)
        return self.data[low_index:high_index]
    
    def count(self, low_key, high_key):
        """
        Number of keys that fall within [low_key, high_key].
        
        There might be a problem here for low_index and high_index only 
        represent the right position to insert the key, then for the case where
        self.data doesn't has the low_key, e.g. [1, 3, 5, 6], 
        self.count(4, 6)=1, contradict the right answer 2
        """
        low_index =self._binary_search(low_key)
        high_index =self._binary_search(high_key)
        return high_index-low_index
 
    def _binary_search(self, key):
        """"
        Binary search for the given key in the sorted array.
        
        return: the right position to insert for key.
        """
        low, high =0, len(self.data)-1
        while low <=high:
            mid=(low+high)//2
            mid_key=self.data[mid]
            if key < mid_key:
                high=mid-1
            elif key >mid_key:
                low=mid+1
            else:
                return mid
        return high + 1

index=RangeIndex()
for i in range(3,8):
    index.add(i)
index.list(0,10)    
index.remove(4)
index.list(0,10)
index.list(4,7)
index.count(4,7)