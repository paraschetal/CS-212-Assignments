#!/usr/bin/env python
'''
Problem: https://community.topcoder.com/stat?c=problem_statement&pm=1889

Author: Paras Chetal
Enrollment No. 15114049
'''

def main():
    arr = [[0 for x in range(0, 101)] for y in range(0, 101)]
    width = int(input("Width: "))
    height = int(input("Height: "))
    bad = []
    print("Enter bad blocks line by line. When done enter 'end'")
    inp = input()
    while(inp!="end"):
        a = int(inp.split(' ')[0])
        b = int(inp.split(' ')[1])
        c = int(inp.split(' ')[2])
        d = int(inp.split(' ')[3])

        if a == c:
            if b>d:
                arr[a][b] = -1
            else:
                arr[c][d] = -1
        else:
            if a>c:
                arr[a][b] = -2
            else:
                arr[c][d] = -2
        
        inp = input()

    for i in range(0, width+1):
        for j in range(0, height+1):
            if i == 0 and j==0:
                arr[i][j] = 1
            else:
                if arr[i][j] == 0:
                    if j!=0:
                        arr[i][j] += arr[i][j-1]
                    if i!=0:
                        arr[i][j] += arr[i-1][j]
                elif arr[i][j] == -1:
                    if i == 0:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = arr[i - 1][j]
                elif arr[i][j] == -2:
                    if j==0:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = arr[i][j - 1]

    print(arr[width][height])

if __name__ == '__main__':
    main()
