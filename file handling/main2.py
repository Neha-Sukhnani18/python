#program to count the number of lines in this file
#opening a file
file = open('codingal.txt','r')
counter = 0

#reading from file
Content = file.read()
    #splittingt content into lines
    #and storing them in a list
CoList = Content.split("\n")

for i in CoList:
    counter+=1

print("this is the number of lines in this file:")
print(counter) 
