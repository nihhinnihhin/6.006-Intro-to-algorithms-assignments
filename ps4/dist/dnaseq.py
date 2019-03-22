#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

if sys.version_info >= (3,):
    xrange = range
    
SUB_SEQ=0
HASH_VALUE=1
POS=2
X=0
Y=1

### Utility classes ###

# Maps integer keys to a set of arbitrary values.

class RollingHash:
    def __init__(self, s):
        self.HASH_BASE = 7
        self.seqlen = len(s)
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.curhash = h

    # Returns the current hash value.
    def hash(self):
        return self.curhash

    # Updates the hash by removing previtm and adding nextitm.  Returns the updated
    # hash value.
    def slide(self, previtm, nextitm):
        self.curhash = (self.curhash * self.HASH_BASE) + ord(nextitm)
        self.curhash -= ord(previtm) * (self.HASH_BASE ** self.seqlen)
        return self.curhash

class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.table={}
        if not pairs==[]:
            for pair in pairs:
                self.put(pair[0], pair[1])
                # is pair[1] list, pair=('subseq',[(1,2),(2,4)])
#        raise Exception("Not implemented!")
    
    def __contains__(self, item):
        return (item in self.table)
    
    # Associates the value v with the key k.
    # key: subsequence--AGCT    value: offsets--[(x,y)]     v: tuple offset--(x,y)
    def put(self, k, v):
        if k in self.table:
            self.table[k].append(v)
        else:
            self.table[k]=[v]
#        raise Exception("Not implemented!")
            
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        try:
            return self.table[k]
        except KeyError:
            return []
        #        raise Exception("Not implemented!")

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    try:
        assert k > 0
        subsequences=kfasta.subsequences(seq,k)
        pos=0
        for s in subsequences:
            if pos==0:
                rh=RollingHash(s)
                hashValue=rh.current_hash()
                subseqInfo=(s,hashValue,pos)
                pos+=1
                previtm=s[0]
            else:
                nextitm=s[len(s)-1]
                rh.slide(previtm,nextitm)
                hashValue=rh.current_hash()
                subseqInfo=(s,hashValue,pos)
                pos+=1
                previtm=s[0]
            yield subseqInfo
    except StopIteration:
        return
    
#    raise Exception("Not implemented!") 
    

# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    try:
        matchesDict=Multidict()
        A=subsequenceHashes(a,k)
        B=subsequenceHashes(b,k)
    #    print list(A),'\n',list(B),'\n'
        matchesDict.put('abc',(1, 2))
        if 'abc' in matchesDict:
            matchesDict=Multidict()
        else:
            raise Exception('error: from __contains__() method')
        for subA in A:
            print subA[HASH_VALUE],'\n'
            for subB in B:
                print subA[HASH_VALUE],subB[HASH_VALUE],'\n'
                if subA[HASH_VALUE]==subB[HASH_VALUE]:
                    matchesDict.put(subA[SUB_SEQ],(subA[POS],subB[POS]))
                    print subA[SUB_SEQ],(subA[POS],subB[POS])
                yield (1,1)
    except StopIteration:
        return
        
#        lookup the table, check whether the subA exists in the table
#        print subA[HASH_VALUE],'\n'
#        # if the new subseq is already in the table
#        # then add
#        if subA[SUB_SEQ] in matchesDict:
#            print subA[HASH_VALUE],'\n'
#            offsets=[]
#            ys=[]   
#            # to store the disticntive y, and check y not in ys everytime it adds (x,y) ,in case add same(x,y)
#            # maybe the matchDict could store xs and ys as its values, the time would be less. version 2.0
##        if subA[SUB_SEQ] in matchesDict.table:
#            for offset in matchesDict[subA[SUB_SEQ]]:
#                y=offset[Y]
#                print y
#                if y not in ys:
#                    matchesDict.put(newSubSeq,(x,y))
#                    ys.append(y)
#                    print newSubSeq,(x,y)
#                    yield (x,y)
##                    print x
#        else:
#            for subB in B:
#                print subA[HASH_VALUE],subB[HASH_VALUE],'\n'
#                if subA[HASH_VALUE]==subB[HASH_VALUE]:
##                    print subB[SUB_SEQ],'y=',2
#                    y=subB[POS]
#                    matchesDict.put(newSubSeq,(x,y))
#                    print newSubSeq,(x,y)
#                    yield (x,y)
#    raise Exception("Not implemented!")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)

