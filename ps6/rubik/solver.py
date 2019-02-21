#debug mistake:
#    uncreadted set,rB.hierarchy[currLevel].add(vB)

from collections import deque
import rubik

PARENT=0
NEIGHBOR=0
MOVE=1

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    return biDirectBFS(start,end)
#    raise NotImplementedError

class BFSResult(object):
    def __init__(self):
        self.level={}
        self.hierarchy={}
        self.parentMovePairs={}  # move refers to from parent to child
        
#class rubikGraph(object):
#    def __init__(self):
#        print "please input your source configuration\n"
#        s=rubik.input_configuration()
#        print "then target configuration"
#        t=rubik.input_configuration()
        
#    def add_edge(self,u,v):
#        if self.adj[u] is None:
#            self.adj[u]=[]
#        self.adj[u].append(v)
        
def neighborsMovePairs(position):
        nbMovePairs=[]
        for twist in rubik.quarter_twists:
#            print "apply twist " + rubik.quarter_twists_names[twist] 
#            + "i.e. " + rubik.perm_to_string + "to "+ "position u"
            neighbor=rubik.perm_apply(twist, position)
            move=twist
            nbMovePairs.append((neighbor,move))
        return nbMovePairs
            
def biDirectBFS(s, t):
    """
    Queue-based implementation of BFS.
    
    Args:
        g: a graph with adjacency list adj such that g.adj[u] is a list of u's 
        neighborsMovePairs.
        s: source.
    """
    rB=BFSResult()
    rB.level={s:0}
    rB.hierarchy={0:{s},1:set()}
    rB.parentMovePairs={s:(None,None)}
    
    rE=BFSResult()
    rE.level={t:0}
    rE.hierarchy={0:{t},1:set()}
    rE.parentMovePairs={t:(None,None)}
    
    queueB=deque()
    queueB.append(s)
    
    queueE=deque()
    queueE.append(t)
    
    newB=s   
    newE=t
    meet=None
    SM=deque()   # shortest moves sequence
    if s==t:
        meet=s
        return SM
    else:
        while queueB or queueE:
            uB=queueB.popleft()
            uE=queueE.popleft()
    
            nbMovePairsB=neighborsMovePairs(uB)
            nbMovePairsE=neighborsMovePairs(uE)
            for i in range(6):
                vB=nbMovePairsB[i][NEIGHBOR]
                vE=nbMovePairsE[i][NEIGHBOR]
                if vB not in rB.level:
                    # prevB is the last new found, so it won't be None
                    if newB:prevB=newB  
                    rB.parentMovePairs[vB]=(uB,nbMovePairsB[i][MOVE])
                    rB.level[vB]=currLevel=rB.level[uB]+1
#                    print 'current level {0},prev level {1}, vB {2}, uB {3}'\
#                    .format(currLevel,rB.level[prevB],rB.level[vB],rB.level[uB])

                    # if vB is the first element in the level, 
                    # then create a new set for the next next level, same as initialization
                    if(rB.level[prevB]==rB.level[uB]):  
                        rB.hierarchy[rB.level[vB]+1]=set()
                    rB.hierarchy[currLevel].add(vB)
                    queueB.append(vB)
                    newB=vB
                    # even length path; odd length path
                    if (newB in rE.hierarchy[currLevel]) or (newB in rE.hierarchy[currLevel-1]):
                        meet=newB
                        break
                else:
                    newB=None
                # to flip 'B' and 'E' then it is the reverse direction search
                if vE not in rE.level:
                    if newE:prevE=newE
                    rE.parentMovePairs[vE]=(uE,nbMovePairsE[i][MOVE])
                    rE.level[vE]=currLevel=rE.level[uE]+1
                    if(rE.level[prevE]==rE.level[uE]):  
                        rE.hierarchy[rE.level[vE]+1]=set()
                    rE.hierarchy[currLevel].add(vE)
                    queueE.append(vE)
                    newE=vE
                    if (newE in rB.hierarchy[currLevel]) or (newE in rB.hierarchy[currLevel-1]):
                        meet=newE
                        break
                else:
                    newE=None
    #    SP=deque(meet)  # here the object meet need to be iterable, can be changed to string
            if(meet):
#                print "meet",meet,'\ns',s,"\nt",t
                parentB=meet
                parentE=meet
                while rB.parentMovePairs[parentB][PARENT]:
                    SM.appendleft(rB.parentMovePairs[parentB][MOVE])
                    parentB=rB.parentMovePairs[parentB][PARENT]
                while rE.parentMovePairs[parentE][PARENT]:
                    SM.append(rubik.twistInv(rE.parentMovePairs[parentE][MOVE]))
                    parentE=rE.parentMovePairs[parentE][PARENT]
                SM=list(SM)
#                print SM
                return SM
    
        
    
                
                
            