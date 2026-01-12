# write a program to print the contents of a directory using the os module 
# search online for function which does that  
import os
directory_path ='/'
contents= os.listdir(directory_path)

for item in contents :
    print(item)
    
