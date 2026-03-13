file_read = open('codingal2.txt','r')
print("file in read mode")
print(file_read.read())
file_read.close()

file_write=open('codingal2.txt','w')
file_write.write("file in write mode..")
file_write.write("i am also a student of codingal.")
file_write.close()

file_append=open('codingal2.txt')
file_append.write('\n file in append mode')
file_append.write("i am also a student of codingal.")
file_append.close()