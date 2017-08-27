
import math
import random

class Node:
    int x
    int y
    def __init__(self, x,y):
       self.x = x
       self.y = y

    def getX:
        return self.x

    def getY:
        return self.y

    def jarak(self,node):
        jarX = abs(self.getX() - node.getX())
        jarY = abs(self.getY() - node.getY())
        jarXY = math.sqrt(jarX**2 + jarY**2)
        return jarXY

class ManageNode:
    arrNode = []

    def addNode(self,node):
        self.arrNode.append(node)

    def getNode(self,index):
        return self.arrNode[index]

    def jmlNode(self):
        return len(self.arrNode)

class

if __name__ == '__main__':




