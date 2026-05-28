""" Write a python program that store characters of a word as List elements and
removes vowels from the list.
Example:
Old List: ['p','r','o','g','r','a','m']
New List: ['p','r','g','r','m']
"""
Old_List = ['p','r','o','g','r','a','m']
new_list =[]
for i in range(0,len(Old_List)):
    if Old_List[i]=='a' or Old_List[i]=='i' or Old_List[i]=='o' or Old_List[i]=='u' or Old_List[i]=='e':
        continue
    else:
        new_list+=Old_List[i]

print(new_list)