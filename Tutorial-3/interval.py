"""
Interval Tree: an interval tree is a tree data structure to hold intervals. Specifically, it allows one to efficiently find all intervals that overlap with any given interval or point. --Wikipedia

Interval Tree implementation in python.

Author: Paras Chetal
Enrollment No. 15114049
"""

class IntervalNode:

    def __init__(self, interval):
        self.interval = interval
        self.maxInSubtree = 0
        self.left = None
        self.right = None


class IntervalTree:

    def __init__(self, root):
        self.root = root

    def insert(self, root, node):
        return
    
    def delete(self, root, interval):
        return
    
    def search(self, interval):
        return

if __name__ == '__main__':

    sampleData = [{15, 20}, {10, 30}, {17, 19},{5, 20}, {12, 15}, {30, 40}]
    
    root = IntervalNode(sampleData[0])

    tree = IntervalTree(root)
        
