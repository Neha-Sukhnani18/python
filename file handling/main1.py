#open the file in the read mode
file_read=open('codingal.txt','r')
print("file in read mode-")
print (file_read.read())
file_read.close()

#open te file in write mode
file_write = open('codingal.txt','w')
#write in the file 
file_write.wrtie("file in write mode....")
file_write.write("hi! i am a penguin. i am 1 yr old") 
file_write.close()

#open the file in append mode
file_append = open('codingal.txt','a')
#apppend in the file
file_append.write ("\n file in append mode....")
file_append.write("hi! i  am penguin. i am 1 yr old")
file_append.close()