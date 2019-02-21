from dnaseq import *

### Testing ###

class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('CTAGC')
        rh2 = RollingHash('TAGCG')
        rh3 = RollingHash('AGCGT')
        rh1.slide('C','G')
        self.assertTrue(rh1.current_hash() == rh2.current_hash())
        rh1.slide('T','T')
        self.assertTrue(rh1.current_hash() == rh3.current_hash())

class TestMultidict(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# This test case may break once you add the argument m (skipping).
class TestExactSubmatches(unittest.TestCase):
   def test_one(self):
       foo = 'yabcabcabcz'
       bar = 'xxabcxxxx'
       matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 1))
       print 'matches',matches
       correct = [(1,2), (4,2), (7,2)]
       self.assertTrue(len(matches) == len(correct))
       for x in correct:
           self.assertTrue(x in matches)

unittest.main()

#%%

#result: 
#[('yab', 6706, 0), ('abc', 5538, 1), ('bca', 5592, 2), ('cab', 5628, 3), ('abc', 5538, 4), ('bca', 5592, 5), ('cab', 5628, 6), ('abc', 5538, 7), ('bcz', 5617, 8)] 
#[('xxa', 6817, 0), ('xab', 6657, 1), ('abc', 5538, 2), ('bcx', 5615, 3), ('cxx', 5811, 4), ('xxx', 6840, 5), ('xxx', 6840, 6)]