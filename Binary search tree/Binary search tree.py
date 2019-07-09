
# Create the node class
class node:
    def __init__(self, value):
        self.value= value
        self.leftChild= None
        self.rightChild= None

# Create tree class

class binarySearchTree:
    # Set the rooooooooot
    def __init__(self, value= None):
        self.root= value

    # Insert value into tree
    def insertTree(self, value):
        if self.root== None:
            self.root= node(value)
            
        else:
            self._insertTree(value, self.root)
    
    def _insertTree(self, value, currNode):
        if value< currNode.value:
            if currNode.leftChild== None:
                currNode.leftChild= node(value)
            else:
                self._insertTree(value, currNode.leftChild)
        elif value> currNode.value: 
            if currNode.rightChild== None:
                currNode.rightChild= node(value)
            else:
                self._insertTree(value, currNode.rightChild)
        else: 
            print("This value is already in the tree")
    
    # Print the all the value in sorted order
    def treePrint(self):
        if self.root !=None :
            self._treePrint(self.root)
    
    def _treePrint(self, currNode):
        if currNode != None:
            self._treePrint(currNode.leftChild)
            print(currNode.value)
            self._treePrint(currNode.rightChild)
   
    # Print heigh of the tree
    def height(self):
        if self.root!= None:
            return self._height(self.root, 0)
        else:
            return 0
    def _height(self, currNode, currHeight):
        if currNode==None: 
            return currHeight
        else:
            leftHeight= self._height(currNode.leftChild, currHeight+1)
            rightHeight= self._height(currNode.rightChild, currHeight+1)
            return max(leftHeight, rightHeight)
    
    # Find a value in the tree ( Not very useful)
    def find(self, value):
        if self.root== value:
            print('Found at root')
        else: 
            self._find(self.root, value)
    
    def _find(self, currNode, value):
        if currNode==None:
            print('Not found')
        else:
            if currNode.value> value:
                self._find(currNode.leftChild, value)
            elif currNode.value < value:
                self._find( currNode.rightChild, value)
            else:
                print('Found')
        
        # Create a balanced binary search tree from sorted array
    def insertSort(self, sortedArr):
        mid= len(sortedArr)//2
        if mid>1:
            self.insertTree(sortedArr[mid])
            self.insertSort(sortedArr[:mid])
            self.insertSort(sortedArr[mid:])

    
# Create a random list of number
import random
import mergeSort as mS
key= random.sample(range(1000), 500)
mS.mergeSort(key)

list= binarySearchTree()
list.insertSort(key)
list.treePrint()
print("The tree's height is : " + str(list.height()))
list.find(932)


