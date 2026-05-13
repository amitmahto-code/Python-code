# write a program to find out whether a given post is talking about "Harry" or not
post = input("enter about your post: ")
if("Harry".lower() in post.lower()):
    print("Yes this post talking about harry ")
else:
    print("this post is not talking about harry ")
    