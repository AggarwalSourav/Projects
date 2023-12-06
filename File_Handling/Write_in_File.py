#1st method
my_object=open("AutoFile.txt",'w')
Number=2522
my_object.write(str(Number))
print("File Created Succefully And Writing Done Successfully")
my_object.close()

#2nd Method
with open("DemoFile.txt",'w') as obj:
    obj.write(str('Hello Welcome to file handling'))
    print('File Created')
