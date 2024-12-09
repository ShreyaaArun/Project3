import os 
import sys

file = None 
bTree = None

def print_menu(): 
    
    while True: 
        print('------------------------------------------------------')
        
        if file is None: 
            print('                   Menu                           ')
            
        else: 
            print('                   Menu (' + file + ')                ')
        
        print('------------------------------------------------------')
        print(' create - Create new index')
        print(' open - Set current index')
        print(' insert - Insert a new key/value pair into current index')
        print(' search - Search for a key in current index')
        print(' load - Insert key/value pairs from a file into current index')
        print(' print - Print all key/value pairs in current index in key order')
        print(' extract - Save all key/value pairs in current index into a file')
        print(' quit - Exit the program')
        print('------------------------------------------------------')
        
        command = input("Enter command: ").strip()
        command.lower()
        
        if command == 'create':
            
            filename = input("Enter filename: ").strip()
            
            try:
                f = open(filename, 'x')
                f.write("This is the write command")
                print(f.read())
                
            except:
                
                print("!!File Already Exists!!")
                overwrite = input("Would you like to overwrite it? (yes/no) ").strip().lower()
                if overwrite == 'yes': 
                    f = open(filename, 'w')
                    f.write("This is the write command")
                if overwrite == 'no':
                    pass
                    
        if command == 'open':
            
            filename = input("Enter filename: ").strip()
            
            if os.path.exists(filename): 
                f = open(filename, 'a')
            else: 
                print("!!File Does Not Exist!!")
                pass
        
        if command == 'quit': 
            
            break
        
        if command == 'insert':
            
            key =  input("Enter the key to insert: ").strip().lower()
            value =  input("Enter the value to insert: ").strip().lower()
            print ("Inserted value " + value + " at key " + key)
        
        if command == 'search': 
            
            key =  input("Enter the key to search: ").strip().lower()
        
        if command == 'load': 
            filename = input("Enter filename: ").strip().lower()
            
        if command == 'extract': 
            filename = input("Enter filename: ").strip().lower()
        
class BNode:
    
    def __init__(self, isroot=False, isleaf=True):
        
        self.isroot = isroot
        self.isleaf = isleaf
        self.children = []
        self.keys = []

class BTree:
    
    def __init__(self):
        
        self.root = None

    def insert(self, key): 
        
        if self.root is None: 
            self.root = BNode(isroot=True, isleaf=True)
            self.root.keys.append(key)
        else: 
            self.split_check()
            self.search_and_insert(key)
        
    def search_and_insert(self, key):
        
        if self.root.isleaf:
            self.root.keys.append(key)
            self.root.keys.sort()
        else:
            c = len(self.root.keys) - 1
            find = False
    
            while c >= 0:
                if key > self.root.keys[c]:
                    root_child = self.root.children[c+1]
                    root_child.keys.append(key)
                    root_child.keys.sort()
                    find = True
                    return
                c =  c-1
            
            if find is False:
                root_child = self.root.children[0]
                root_child.keys.append(key)
                root_child.keys.sort()

                
    def split_check(self): 
        
        if len(self.root.keys) == 7: 
            self.split(None, self.root)
        else:
            
            for root_child in self.root.children:
                if len(root_child.keys) == 7:
                    self.split(self.root, root_child)

    def split(self, parent, child):
        
        mid = child.keys[3]
        lessNode = BNode(isleaf=child.isleaf)
        greaterNode = BNode(isleaf=child.isleaf)
        lessNode.keys = child.keys[:3]
        greaterNode.keys = child.keys[4:]

        if parent is None:
            newroot = BNode(isroot=True, isleaf=False)
            newroot.keys.append(mid)
            newroot.children.append(lessNode)
            newroot.children.append(greaterNode)
            self.root = newroot
        else:
            parent.keys.append(mid)
            parent.keys.sort()
            parent.children.remove(child)
            parent.children.append(lessNode)
            parent.children.append(greaterNode)
    
    def traverse(self, level, Node=None):

        if Node is None: 
            
            Node = self.root 
            print("Current Level: Root (0) -> " + str(Node.keys))
            
            if Node.isleaf is False: 
                
                for root_child in Node.children: 
                    new_level = level+1
                    self.traverse(new_level, root_child)
                    
        elif Node.isleaf is False:
            
            print("Current Level" + level, "Keys:", str(Node.keys))
            for Node_child in Node.children: 
                new_level = level+1
                self.traverse( new_level, Node_child)
                
        elif Node.isleaf is True: 
            
            print("Current Level: " + str(level) + " -> " + str(Node.keys))
            return 
             
    
            
file = "test.idx" 
print_menu()


