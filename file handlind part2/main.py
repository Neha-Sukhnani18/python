#write in the file using the with() function
with open ('Codingal.txt','w') as file:
    file.write("hi! i am a penguin and i am 1 year old")
file.close()
#split the file in words
with open('Codingal.txt','r') as file:
    data = file.readlines()
    print("words in this file are:")
    for line in data:
        word = line.split()
        print(word)
file.close()