#Create the two sets of the two guest lists
set1 = {'A','B','C','D','E'}
set2 = {'B','D','V','X','Y','Z'}

#Find union of two sets
union = set1.intersection(set2)

#Converting set into list
#to find total guests to be invited in the party
total_guests = list(union)

print("Total guests to be invited in the party are:", len(total_guests))
print("Guests List:", total_guests) 