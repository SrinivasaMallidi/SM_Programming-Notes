class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
    
    def inorder(self,ansTree):
        if self.left:
            self.left.inorder(ansTree)
        ansTree.append(self.val)
        if self.right:
            self.right.inorder(ansTree)
    
    def preorder(self,ansTree):        
        ansTree.append(self.val)
        if self.left:
            self.left.preorder(ansTree)
        if self.right:
            self.right.preorder(ansTree)

    def isSubTree(self,b2):
        print("In Order Traversal::")
        inorderTree1 = []
        inorderTree2 = []
        self.inorder(inorderTree1)
        print("Tree-1::"+str(inorderTree1))
        b2.inorder(inorderTree2)
        print("Tree-2::"+str(inorderTree2))

        inorderStr1 = str(inorderTree1).replace("[","").replace("]","")
        inorderStr2 = str(inorderTree2).replace("[","").replace("]","")

        if(inorderStr1.find(inorderStr2) == -1):
            return False


        print("PreOrder Traversal::")
        preorderTree1 = []
        preorderTree2 = []
        self.preorder(preorderTree1)
        print("Tree-1::"+str(preorderTree1))
        b2.preorder(preorderTree2)
        print("Tree-2::"+str(preorderTree2))

        preorderStr1 = str(preorderTree1).replace("[","").replace("]","")
        preorderStr2 = str(preorderTree2).replace("[","").replace("]","")

        if(preorderStr1.find(preorderStr2) == -1):
            return False
        return True
    
b1 = BinaryTree(8)
b1.left = BinaryTree(7)
b1.right = BinaryTree(4)
b1.left.left = BinaryTree(3)
b1.left.right = BinaryTree(6)
b1.right.left = BinaryTree(7)
b1.right.right = BinaryTree(9)

b2 = BinaryTree(7)
b2.left = BinaryTree(3)
b2.right = BinaryTree(6)


if (b1.isSubTree(b2)):
    print("b2 is Subtree of b1")
else:
    print("b2 is not a Subtree of b1")