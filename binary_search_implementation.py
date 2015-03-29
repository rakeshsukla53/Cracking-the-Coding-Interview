__author__ = 'rakesh'


class BinarySearchTree:

    def __init__(self, value):

        self.value = value
        self.right = None
        self.left =  None

    def insert(self, data):  #this will take the value and insert accordingly

        if data > self.value:
            if self.right == None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

        elif data < self.value:
            if self.left == None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def isleaf(self):
        return (self.right == None) and (self.left == None)

    def getLeftChildValue(self):
        return self.getRootValue()

    def getRightChildValue(self):
        return self.right.getRootValue()

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getRootValue(self):
        return self.value

    def setRootValue(self, obj):
        self.value = obj

    def inOrder(self):   #basically inOrder goes from left center right
        if self.leftChild:
            self.leftChild.inOrder()
        print self.value
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print self.value


root = BinarySearchTree(8)

root.insert(3)
root.insert(10)
root.insert(1)













