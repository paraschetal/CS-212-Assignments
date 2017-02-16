"""
Interval Tree: an interval tree is a tree data structure to hold intervals. Specifically, it allows one to efficiently find all intervals that overlap with any given interval or point. --Wikipedia

Interval Tree implementation in python.

Author: Paras Chetal
Enrollment No. 15114049
"""

class IntervalNode:

    def __init__(self, interval):
        self.interval = interval
        self.maxInSubTree = None
        self.high = max(i for i in interval)
        self.low = min(i for i in interval)
        self.leftSubTree = None
        self.rightSubTree = None
        self.parent = None

    def setParent(self, parent):
        self.parent = parent


class IntervalTree:

    def __init__(self, root):
        self.root = root

    def insert(self, node):
        if self.root == None:
            self.root = root
        else:
            self.root.maxInSubTree = max(self.root.maxInSubTree, node.high)

            if node.low < self.root.low:
                if self.root.leftSubTree == None:
                    self.root.leftSubTree = IntervalTree(node)
                    self.root.leftSubTree.root.setParent(self.root)
                else:
                    self.root.leftSubTree.insert(node)

            else:
                if self.root.rightSubTree == None:
                    self.root.rightSubTree = IntervalTree(node)
                    self.root.rightSubTree.root.setParent(self.root)
                else:
                    self.root.rightSubTree.insert(node)
                    
 
    def delete(self, interval):
        if self.root.interval == interval:

            whichChild = ''
            if self.root.parent.rightSubTree == self:
                whichChild = 'right'
                
            elif self.root.parent.leftSubTree == self:
                whichChild = 'left'
                

                
            if not self.root.rightSubTree and not self.root.leftSubTree: #If the node has no child
                if whichChild == 'left':
                    self.root.parent.leftSubTree = None
                else:
                    self.root.parent.rightSubTree = None

                    
            elif not self.root.rightSubTree or not self.root.leftSubTree: #If the node has only one child
                
                if self.root.rightSubTree != None:
                    if whichChild == 'left':
                        self.root.parent.leftSubTree = self.root.rightSubTree
                    else:
                        self.root.parent.rightSubTree = self.root.rightSubTree
                        
                        
                else:
                    if whichChild == 'left':
                        self.root.parent.leftSubTree = self.root.leftSubTree
                    else:
                        self.root.parent.rightSubTree = self.root.leftSubTree
                        
            
            else: #If the node has both children
               
                leftmostSubChildOfTheRightNode = self.root.rightSubTree
                while(leftmostSubChildOfTheRightNode.root.leftSubTree!=None):
                    leftmostSubChildOfTheRightNode = leftmostSubChildOfTheRightNode.root.leftSubTree
                    
                lefttemp = self.root.leftSubTree
                righttemp = self.root.rightSubTree
                
                if whichChild == 'left':
                    
                    self.root.parent.leftSubTree.root = leftmostSubChildOfTheRightNode.root
                    self.root.leftSubTree = lefttemp
                    if righttemp.root.leftSubTree == None:
                        self.root.rightSubTree = None
                    else:
                        self.root.rightSubTree = righttemp
                   
                    if not lefttemp and not righttemp:
                        pass
                    elif not lefttemp and not (not righttemp):
                        self.root.maxInSubTree = righttemp.root.maxInSubTree
                    elif not (not lefttemp) and not righttemp:
                        self.root.maxInSubTree = lefttemp.root.maxInSubTree
                    else:
                        pass
                        

                else:
                    self.root.parent.rightSubTree.root = leftmostSubChildOfTheRightNode.root
                    self.root.leftSubTree = self.root.leftSubTree
                    if righttemp.root.leftSubTree == None:
                        self.root.rightSubTree = None
                    else:
                        self.root.rightSubTree = self.root.rightSubTree

                    if not lefttemp and not righttemp:
                        pass
                    elif not lefttemp and not (not righttemp):
                        self.root.maxInSubTree = righttemp.root.maxInSubTree
                    elif not (not lefttemp) and not righttemp:
                        self.root.maxInSubTree = lefttemp.root.maxInSubTree
                    else:
                        pass

                
                self.delete(leftmostSubChildOfTheRightNode.root.interval)

            
        else:
            
            if min(i for i in interval) < self.root.low:
                if not self.root.leftSubTree:
                    print "1. No such interval found."
                else:
                    self.root.leftSubTree.delete(interval)
                    
            elif min(i for i in interval) > self.root.low:
                if not self.root.rightSubTree:
                    print "2. No such interval found."
                else:
                    self.root.rightSubTree.delete(interval)
                    
            else:
                print "3. No such interval found."
                



    def search(self, interval):
        return
   

if __name__ == '__main__':

    sampleData = [{15, 20}, {10, 30}, {17, 19},{5, 20}, {12, 15}, {30, 40}]
    root = IntervalNode(sampleData[0])

    tree = IntervalTree(root)

    for data in sampleData[1:]:
        tree.insert(IntervalNode(data))

'''
    print tree.root.__dict__

    print tree.root.leftSubTree.root.__dict__
    print tree.root.rightSubTree.root.__dict__

    print tree.root.leftSubTree.root.leftSubTree.root.__dict__
    print tree.root.leftSubTree.root.rightSubTree.root.__dict__

    print tree.root.rightSubTree.root.rightSubTree.root.__dict__        
'''
    
    tree.delete({10,30})
    
'''   
    print tree.root.__dict__

    print tree.root.leftSubTree.root.__dict__
    print tree.root.rightSubTree.root.__dict__

    print tree.root.leftSubTree.root.leftSubTree.root.__dict__
    print tree.root.rightSubTree.root.rightSubTree.root.__dict__
'''
