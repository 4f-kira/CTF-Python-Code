#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket

# m = ['00000',
#      '11110',
#      '00010',
#      '01111',
#      '00000']

def fuck(m):
    size = len(m)
    m2 = [list(x) for x in m]
    path = []
    start = [1,0]
    end = [size-2,size-1]

    def valid(x,y):
        if (x>=0 and x<size and y>=0 and y<size and m2[x][y]=='1'):
            return (x,y) not in path
        else:
            return False

    def walk(x,y):
        if valid(x,y):
            path.append((x,y)) #入栈
            if(x==end[0] and y==end[1]):  #出口
                #print("successful!",path)
                return True

            if walk(x,y+1):#right
                return True
            elif walk(x+1,y):#down
                return True
            elif walk(x,y-1):#left
                return True
            elif walk(x-1,y):#up
                return True
            else:
                path.pop() #出栈
                m2[x][y] = '0'
                return False  # 无路可走

    if walk(start[0],start[1]):  #起点
        return len(path) 
    else:
        return 0 


def recvuntil(x):
    t1 = s.recv(512)
    while x not in t1:
        t1 += s.recv(512)
    return t1

host = '104.224.169.128'
port = 28880
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print recvuntil('(y/n)')
s.send('y')
for i in range(10):
    data = recvuntil('steps:')
    maze_size = len(data.split('\n')[1])
    maze = data.split('\n')[1:maze_size+1]
    print data
    #print maze
    num = fuck(maze)
    s.send(str(num)+'\n')

print recvuntil('\n')