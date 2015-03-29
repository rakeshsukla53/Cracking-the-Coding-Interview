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

    def getleftValue(self):
        return self.left.getRootValue()

    def getrightValue(self):
        return self.right.getRootValue()

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getRootValue(self):
        return self.value

    def setRootValue(self, obj):
        self.value = obj

    def inOrder(self):   #basically inOrder goes from left center right
        if self.left:
            self.left.inOrder()
        print self.value
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print self.value
    
    def preOrder(self):
        print self.value
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()


    def lookup(self, data, parent = None):

        if data > self.value:
            if self.right is None:
                return None, None
            self.right.lookup(data, self)

        elif data < self.value:
            if self.left is None:
                return None, None
            self.left.lookup(data, self)

        else:
            return self, parent




root = BinarySearchTree(8)

root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node, parent = root.lookup(6)

parent.getRootValue()



















