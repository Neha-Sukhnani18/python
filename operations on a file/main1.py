#open the file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open('Codingal.txt','w')
#write in the file
file_write.write("new content 1")
file_write.write("new content 2")
file_write.close()

#open the file in append mode
file_append=open('Codingal.txt','a')
#append in the file
file_append.write("\n File in append mode....")
file_append.write("hi! i am a penguin. i am 1 year old")
file_append.close()