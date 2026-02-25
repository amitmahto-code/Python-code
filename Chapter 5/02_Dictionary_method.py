marks={
    "OB":80,
    "OS":90,
    "RDBMS":95,
    "PS":96 ,
    "IKS":97 ,
}
print(marks.items())
print(marks.keys())
print(marks.values())

# #here you can see that update method to dictionary is mutable
marks.update({"IKS":100,"ACE":99}) #we can also new key and values
print(marks)

# # Differnt between get and itmes
print(marks.get("RDBM")) # if the key not found it return "None "
print(marks.get("RDBMS")) 
print(marks.items("RDBMS")) 
print(marks.items("RDBM")) # but this return error  "

#remove that key from dictionary
value=marks.pop("IKS")
print(marks)

item=marks.popitem()
print(item)
print(marks)

