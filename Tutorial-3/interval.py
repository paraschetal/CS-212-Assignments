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
                else:
                    self.root.leftSubTree.insert(node)

            else:
                if self.root.rightSubTree == None:
                    self.root.rightSubTree = IntervalTree(node)
                else:
                    self.root.rightSubTree.insert(node)
        #print self.root.__dict__
    
    def delete(self, root, interval):
        return
    
    def search(self, interval):
        return
    

if __name__ == '__main__':

    sampleData = [{15, 20}, {10, 30}, {17, 19},{5, 20}, {12, 15}, {30, 40}]
    root = IntervalNode(sampleData[0])
    print root.__dict__

    tree = IntervalTree(root)

    for data in sampleData[1:]:
        tree.insert(IntervalNode(data))

    #print tree.root.__dict__

    #print tree.root.leftSubTree.root.__dict__
    #print tree.root.rightSubTree.root.__dict__

    #print tree.root.leftSubTree.root.leftSubTree.root.__dict__
    #print tree.root.leftSubTree.root.rightSubTree.root.__dict__

    #print tree.root.rightSubTree.root.rightSubTree.root.__dict__        
