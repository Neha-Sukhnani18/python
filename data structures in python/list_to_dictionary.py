def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

students=[[1,'jean casro',' V'],[2,'lula powell','V'], [3,'brain howell','v'],[4,'lynne foster','VI'], [5,'zachary simon','VII']]

print("\nOrignal list of lists:")
print(students)
print("\nConverted list to a dictionary")
print(test(students))