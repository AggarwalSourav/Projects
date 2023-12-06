obj=open("BotFile.txt",'w')
n=int(input("Enter the number of lines you want enter in the file: "))
for i in range(n):
    line=input(f"Enter line {i+1}: ")
    obj.write(line + "\n")
obj.close()
print("Now reading the contents of the file:")
obj=open("BotFile.txt",'r')
for str in obj:
    print(str)
obj.close()
