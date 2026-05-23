#write a python to convert all ther character of a lower case to upper case and upper case to lower case
text = input("Enter string: ")
new_text = ""
for i in range(len(text)):
    if text[i].islower():
        new_text+= text[i].upper()
    elif text[i].isupper():
        new_text+= text[i].lower()
    else:
        new_text+=text[i]
print(new_text)
        