#!/usr/bin/env python
'''
Problem Statement
        

A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.
 
Definition
        
Class:  ZigZag
Method: longestZigZag
Parameters: int[]
Returns:    int
Method signature:   int longestZigZag(int[] sequence)
(be sure your method is public)
    
 
Constraints
-   sequence contains between 1 and 50 elements, inclusive.
-   Each element of sequence is between 1 and 1000, inclusive.




Author: Paras Chetal
Enrollment No. 15114049
'''

def main():
    l = int(input("Length: "))
    p = [0]*l
    n = [0]*l

    s = [int(i) for i in input("Enter list: ").split(' ')]
    
    for i in range(0,l):
        p[i] = 0
        n[i] = 0

        for j in range(0,l)[::-1]:
            d = s[i] - s[j]
            if d>0:
                p[i] = max(n[j] + 1, p[i])
            elif d<0:
                n[i] = max(p[j] + 1, n[i])


    print("Length of longest zig-zag sequence: " + str(max(n[l-1], p[l-1])))

if __name__ == "__main__":
    main()
