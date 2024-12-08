import os 
import sys

file = None 

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
                    print(f.read())
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
            

        
file = "test.idx" 
print_menu()


