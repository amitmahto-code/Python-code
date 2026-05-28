''' write a Python program that performs the following:
 Ex. Inputted String: Hello Technocrates
1. Print all character by skipping 1 character.
2. Print entire string reverse
3. Print length of the String.
'''

string = input("Enter string: ")
print("1. By skipping 1 char",string[::2])
print("2. Reversed string:", string[::-1])
print("3. length of string ",len(string))