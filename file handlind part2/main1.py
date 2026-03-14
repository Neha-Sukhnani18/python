#create a new file
new_file = open('neha.txt','x')
new_file.close()

#check if a file exists
import os
print("checking if codingal.txt exists or not...")
if os.path.exists("Codingal.txt"):
    os.remove("Codingal.txt")
else:
    print("the file doesnt exists")

#create a new file if it doesnt
my_file = open("neha.txt","w")
my_file.write("hi! my name is neha i am 14 years old.")
my_file.close()

#delete file named codindal_updated
os.remove('codingal_updated.txt')

#delete the folder
#os.rmdir('folder')