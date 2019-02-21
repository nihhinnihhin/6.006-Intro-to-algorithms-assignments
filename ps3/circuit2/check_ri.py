# -*- coding: utf-8 -*-
"""
Representation Invariant Test Harness

Created on Sun Oct 14 21:49:47 2018

@author: Hinson
"""
import bstsize_r
t = bstsize_r.BST()
print t
for i in range(20):
    t.insert(i)
print t

t.delete(2)
print 'after deleting 2\n'
#t.delete_min()
print t
 

#import avl_r
#t = avl_r.AVL()
#print t
#
#for i in range(20):
#    t.insert(i);
#print t
##t.delete(2)
#print 'after deleting 2\n'
##t.delete_min()
#print t