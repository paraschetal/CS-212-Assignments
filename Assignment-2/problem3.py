#!/usr/bin/env python
'''
The Chef is planning a buffet for the DirectiPlex inauguration party, and everyone is invited. On their way in, each guest picks up a sheet of paper containing a random number (this number may be repeated). The guests then sit down on a round table with their friends.

The Chef now decides that he would like to play a game. He asks you to pick a random person from your table and have them read their number out loud. Then, moving clockwise around the table, each person will read out their number. The goal is to find that set of numbers which forms an increasing subsequence. All people owning these numbers will be eligible for a lucky draw! One of the software developers is very excited about this prospect, and wants to maximize the number of people who are eligible for the lucky draw. So, he decides to write a program that decides who should read their number first so as to maximize the number of people that are eligible for the lucky draw. Can you beat him to it?
Input

The first line contains t, the number of test cases (about 15). Then t test cases follow. Each test case consists of two lines:

    The first line contains a number N, the number of guests invited to the party.
    The second line contains N numbers a1, a2, ..., an separated by spaces, which are the numbers written on the sheets of paper in clockwise order.

Output

For each test case, print a line containing a single number which is the maximum number of guests that can be eligible for participating the the lucky draw.
Constraints

    1 ≤ N ≤ 10000
    You may assume that each number number on the sheet of paper; ai is randomly generated, i.e. can be with equal probability any number from an interval [0,U], where U is some upper bound (1 ≤ U ≤ 106).




Author: Paras Chetal
Enrollment No. 15114049
'''


def ci(arr, a, b, val):
    while (b-1)>1:
        m = int(round((a + (b-a)/2)))
        if arr[m] >= val:
            b = m
        else:
            a = m
    return b

def lislen(arr, size):
    length = 0
    lis = [0]*size
    lis[0] = arr[0]
    for i in range(0, size):
        if arr[i]>lis[length-1]:
            lis[length] = arr[i]
            length += 1
        elif arr[i] < lis[0]:
            lis[0] = arr[i]
        else:
            lis[ci(lis, -1, length - 1, arr[i])] = arr[i]
    return length

def main():
    t = int(input())

    while t>0:
        mi = 0
        ans = 0
        n = int(input())
        arr = [0]*(n*n)
        inp = [int(i) for i in input().split(' ')]
        for i in range(0,n):
            arr[i] = inp[i]
            arr[i + n] = arr[i]

        for i in range(0,n):
            ans = lislen(arr[i:i+n], n)
            if ans>mi:
                mi = ans
        print(mi)
        t = t-1

if __name__ == '__main__':
    main()
