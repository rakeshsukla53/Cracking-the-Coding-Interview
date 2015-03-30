__author__ = 'rakesh'

import pybst


class BinarySearchTree:   #now you can perform any type of opertion on this tree

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


    def lookup(self, data, parent=None):

        if data > self.value:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)

        elif data < self.value:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)   #refer to this note to under
            # http://www.pythontutor.com/visualize.html#mode=display
            #you need to return the value because everything is recursive here

        else:
            print "Node is %s" % self.getRootValue()
            print "Parent is %s" % parent.getRootValue()

            return self, parent

    def delete(self, data):

        node, parent = self.lookup(data)

        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

                del node

            else:
                self.data = 0

        elif children_count == 1:
            #if there is only one node then you need to replace it with its child
            if node.left:
                n = node.left
            if node.right:
                n = node.right

            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node

        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left

            node.value = successor.value  #find the inorder successor of the node and replace it
            if parent.left == successor:
                parent.left = successor.right

            else:
                parent.right = successor.right

    def printout(self):   #this is the inorder traversal of the whole tree. Inorder traversal will give you all whole tree

        if self.left:
            self.left.printout()
        print self.value
        if self.right:
            self.right.printout()

    def compare_two_tree(self, node):  #when you are comparing two trees then its right and left child should be equal

        if node is None:
           print "Tree are not equal"
           return False


        if self.value != node.value:
            print "Trees are not equal"
            return False

        else:
            if self.left:
                self.left.compare_two_tree(node.left)
            print self.value
            if self.right:
                self.right.compare_two_tree(node.right)  #if it printouts all the trees values then they are equal
        #just use simply use the inorder traversal and compare each value as we go along

    def children_count(self):

        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


def height(tree):   #you can print out the height of the tree
    if tree == None:
        return 0
    else:

        return 1 + max(height(tree.left), height(tree.right))


root = BinarySearchTree(8)

root.insert(3)
root.insert(10)
root.insert(2)
root.insert(4)
root.insert(9)
root.insert(11)

#root.delete(3)  # 1 is deleted from the binary tree

node = BinarySearchTree(8)
node.insert(3)
node.insert(10)
node.insert(2)
node.insert(4)
node.insert(9)
node.insert(11)

root.compare_two_tree(node)





















