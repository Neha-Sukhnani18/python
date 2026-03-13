#Program to remove lines starting with any prefix

file1 = open('Codingal.txt',
             'r')
file2 = open('Codingal_Updated.txt',
             'w')

#reading each line from the orignal
#text file
for line in file1.readlines():

    #reading all the lines that dont
    #begin with coding
    if not(line.startswith('coding')):
        #printing those lines
        print(line)

        #storing only those lines that
        #dont begin with codingal
        file2.write(line)

#close and save the files
file2.close()
file1.close()