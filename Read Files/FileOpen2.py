try:
    fp=open("zeba.txt","r")
except FileNotFoundError:
    print("File does not Exists")

else:
    print("File open in the read mode successfully\n")
    print("Type of fp=",type(fp))
    print("File Mode=",fp.mode)
    print("is file readable=",fp.readable())
    print("Is file writeable=",fp.writable())
    
