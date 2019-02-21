buf='abc'
while buf!='':
    char=buf[0]
    buf=buf[1:]
    print char
if buf=='':
    print 'true'

#from kfasta import *
#seq = FastaSequence('trivial.fa')
#seqstr = ''
#for c in seq:
#    seqstr += c
#    print c
#    print seqstr