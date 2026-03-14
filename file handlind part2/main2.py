#program to eliminate repeated lines from a file
#creating the output file
outputFile = open('codingal_updated.txt','w')

#reading the input file
inputFile = open('repeated.txt','r')

#holds lines already seen
lines_seen_so_far = set()
print("eliminating duplicate lines")
#iterating each line in the file
for line in inputFile:
    #checking if line is unique
    outputFile.write(line)
    #adds unique lines to lines_seen_so_far
    lines_seen_so_far.add(line)

#closing the file
inputFile.close()
outputFile.close()