#!/usr/bin/env python
# coding: utf-8

# # Final Code

# In[13]:


class AVLNode:
    def __init__(self, value):
        '''Constructor for initialzing AVL Node'''
        self.value = value
        self.left = None
        self.right = None
        self.height = 1     

class AVLTree:
    def __init__(self):
        '''Constructor for initializing AVLTree Class'''
        self.root = None
        
    def __balance_factor(self, node):

        if not node: # IF NODE == NONE RETURN 0
            return 0
        
        if node.left: # HEIGHT OF LEFT SUBTREE
            left_height = self.__Height(node.left)+1
            
        else: # IF NO LEFT SUBTREE, LEFT HEIGHT WILL BE 0
            left_height = 0
            
        if node.right: # HEIGHT OF RIGHT SUBTREE
            right_height = self.__Height(node.right)+1  
            
        else: # IF NO RIGHT SUBTREE, LEFT HEIGHT WILL BE 0
            right_height = 0
        
        return left_height-right_height
                
    def Insert(self, value):
        '''This method is for inserting a node into the AVL Class. Time Complexity: O(logn)'''
        if not self.root: # CHECK IF ROOT EXIST OR NOT
            node = AVLNode(value)
            self.root = node
        else: # IF ROOT EXIST, PERFORM RECURSIVE CALL FOR INSERTION
            self.root = self.__Insert(self.root, value, self.root)
                                                     
    def __Insert(self, root, value, parent):
        
        if not root: 
            root = AVLNode(value)

        elif value>root.value: # IF VALUE IS GREATER THAN ROOT, SEND TO RIGHT SUBTREE
            root.right = self.__Insert(root.right, value, root)

        elif value<root.value: # IF VALUE IS LESS THAN ROOT, SEND TO LEFT SUBTREE
            root.left = self.__Insert(root.left, value, root)

        elif root.value==value: # IF VALUE ALREADY EXIST
            pass   
            
        # CHECK IF INSERTION HAS DISTURBED BALANCE FACTOR OF ANY NODE
        check_insertion = self.__check_insertion(root, value)
        
        if check_insertion:
            return check_insertion
  
        return root

    def Delete(self, value):
        '''This method is for deleting a node from the AVLTree Class. Time Complexity: O(logn)'''
        if not self.root: # IF ROOT DOESNT EXIST
            pass
        
        else:
            self.root =  self.__delete_node(self.root, value)
    
    def __delete_node(self,n,value):
        
        # IF n IS NONE
        if not n:
            return n
        
        elif value < n.value:     # IF VALUE IS LESS THAN ROOT, SEND TO LEFT SUBTREE
            n.left = self.__delete_node(n.left, value)
        elif value > n.value:     # IF VALUE IS GREATER THAN ROOT, SEND TO RIGHT SUBTREE
            n.right = self.__delete_node(n.right, value)
        else:
            if n.left is None: 
                temp = n.right
                n = None
                return temp
            
            elif n.right is None:
                temp = n.left
                n = None
                return temp
            
            temp = self.__Min(n.right)
            n.value = temp.value
            n.right = self.__delete_node(n.right, temp.value)
            
        if n is None:
            return n
        
        # CHECK IF DELETION HAS DISTURBED BALANCE FACTOR OF ANY NODE
        check_deletion = self.__check_deletion(n)
        
        if check_deletion:
            return check_deletion
    
        return n
    
    def __check_deletion(self, node):
        node.height = 1 + max(self.__Height(node.left), self.__Height(node.right))
        balanceFactor = self.__balance_factor(node)
        
        # CHECK IF LEFT SIDE IS HEAVY
        if balanceFactor > 1:
            
            # FOR RIGHT ROTATION
            if self.__balance_factor(node.left) >= 0:
                return self.right_rotation(node)
            
            # FOR LEFT-RIGHT ROTATION
            else:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
            
        # CHECK IF RIGHT IS HEAVY
        if balanceFactor < -1:
            
            # FOR LEFT ROTATION
            if self.__balance_factor(node.right) <= 0:
                return self.left_rotation(node)
            
            # FOR RIGHT LEFT ROTATION
            else:
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
            
    def __check_insertion(self, node, value):
        node.height = 1 + max(self.__Height(node.left), self.__Height(node.right))
        balance_factor = self.__balance_factor(node) 
        
        # CHECK IF LEFT SIDE IS HEAVY 
        if balance_factor >= 2:
            
            # FOR RIGHT ROTATION
            if value < node.left.value: 
                return self.right_rotation(node)
            
            # FOR LEFT-RIGHT ROTATION
            elif value > node.left.value:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
        
        # CHECK IF RIGHT SIDE IS HEAVY
        if balance_factor <= -2:
            
            # FOR LEFT ROTATION
            if value > node.right.value:
                return self.left_rotation(node) 
            
            # FOR RIGHT-LEFT ROTAION
            elif value < node.right.value:
                node.right = self.right_rotation(node.right) 
                return self.left_rotation(node) 
    
    def Search(self, value):
        '''This method is for searching a value in the AVL Tree Class. Time Complexity: O(logn)'''
        if not self.root:
            return None
        
        return self.__Search(self.root, value)
    
    def __Search(self, root, value):
        if not root:
            return None
        
        if root.value == value:
            return root
        
        elif value > root.value:
            return self.__Search(root.right, value)
        
        elif value < root.value:
            return self.__Search(root.left, value)
            
    def Size(self):
        '''This method returns current size of the AVL Tree. Time Complexity: O(logn)'''
        if not self.root:
            return 0
        
        return self.__Size(self.root)
    
    def __Size(self, root):
        if not root:
            return 0
        
        s = 1 + self.__Size(root.left) + self.__Size(root.right)
        
        return s
            
    def Height(self):
        '''This method returns current height of the AVL Tree'''
        if not self.root:
            return 0
        
        return self.__Height(self.root)
    
    def __Height(self, root):
        if not root:
            return -1
        
        h = 1 + max(self.__Height(root.left), self.__Height(root.right))
        
        return h
    
    def Min(self):
        '''This method returns the minimum node in the the AVL Tree'''
        if not self.root:
            return None
        
        return self.__Min(self.root)
    
    def __Min(self, root):
        if not root:
            return None
        
        if not root.left:
            return root
        
        return self.__Min(root.left)
    
    def Max(self):
        '''This method returns the maximum node in the the AVL Tree'''
        if not self.root:
            return None
        
        return self.__Max(self.root)
    
    def __Max(self, root):
        if not root:
            return None
        
        if not root.right:
            return root
        
        return self.__Max(root.right)
    
    def InOrder(self):
        '''This method is for performing in-order traversal. Time Complexity: O(n)'''
        if not self.root:
            return None
        
        self.__InOrder(self.root)
        
    def __InOrder(self, root):
        if root:
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)
            
    def PreOrder(self):
        '''This method is for performing pre-order traversal. Time Complexity: O(n)'''
        if not self.root:
            return None
        
        self.__PreOrder(self.root)
        
    def __PreOrder(self, root):
        if root:
            print(root.value)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            
    def PostOrder(self):
        '''This method is for performing post-order traversal. Time Complexity: O(n)'''
        if not self.root:
            return None
        
        self.__PostOrder(self.root)
        
    def __PostOrder(self, root):
        if root:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value)
    
    def Successor(self, node):
        '''This method returns successor of a node'''
        return self.__Min(node.right)
    
    def Predecessor(self, node):
        '''This method returns predecessor of a node'''
        return self.__Max(node.left)
    
    def left_rotation(self, z):
        '''This method is for performing left-rotation, when AVL Tree is heavy on right side'''
        y = z.right
        var = y.left
        y.left = z    #rotation is being performed
        z.right = var
        z.balance_factor = 1 + max(self.__Height(z.left),self.__Height(z.right))   # updating height of a tree to balance   
        y.balance_factor = 1 + max(self.__Height(y.left),self.__Height(y.right))
        
        return y    #returns new root

    def right_rotation(self, z):
        '''This method is for performing left-rotation, when AVL Tree is heavy on left side'''
        z.parent = z.left
        y = z.left
        var1 = y.right
        y.right = z    #rotation is being performed
        z.left = var1
        z.height = 1 + max(self.__Height(z.left),self.__Height(z.right))     # updating height of a tree to balance   
        y.height = 1 + max(self.__Height(y.left),self.__Height(y.right))
        
        return y  #returns new root


# In[14]:


tree = AVLTree()
tree.Insert(50)
tree.Insert(60)
tree.Insert(45)
tree.Insert(30)


tree.PreOrder()


# In[15]:


tree.Insert(80)
tree.PreOrder()


# In[16]:


tree.Delete(60)
tree.PreOrder()


# In[ ]:




