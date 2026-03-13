#open a file and reads its contents
file = open('Codingal.txt','r')
print(file.read())
file.close()
#open a file and reads its beginning 8 characters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()
#append your name and age in the file
file = open('Codingal.txt','a')
file.write("hi! I am a penguin and i am 1 year old.")
file.close()
