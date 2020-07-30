import re
data = open('sum.txt').read()
lst= list()
temp = re.findall("[0-9]+", data)
lst.append(temp)
print(lst)
            ##flattened
updatelst = flattened = []
for sublist in lst:
    for val in sublist:
        flattened.append(val)


        # Printing modified list
updatelst = [int(i) for i in updatelst]
print("Modified list is : " + str(updatelst))
print(updatelst)
print("SUM:", sum(updatelst))

