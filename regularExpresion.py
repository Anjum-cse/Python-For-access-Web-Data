
## find start with....

import re
data = open('test.txt')
for line in data:
    line = line.rstrip()
    if re.search('^Khulke', line):
        print(line)

        #findNumbers

d2= 'i am anjum. age 24. cr7 is my idol '
extractedD2 = re.findall("[0-9]+",d2)
print(extractedD2)

#greedy Matching


s= "I :love myself: Selfish?"
extractedS= re.findall("I.+:",s) ##greedy
print(extractedS)
extractedS= re.findall("I.+?:",s) #not #greedy
print(extractedS)

        #findEmailAddress

email= "From tanvir15@diu.edu.bd 4/2/2020 test"
extractEmail = re.findall("\S+@+\S+",email)
print(extractEmail)

#by parenthases (Filter Line)
extractEmail = re.findall("^From (\S+@+\S+)",email)
print(extractEmail)


       #double split #find org
extractOrg = re.findall("@([^ ]*)",email)
print(extractOrg)
#by parenthases (Filter Line)
extractOrg = re.findall("^From .*@([^ ]*)",email)
print(extractOrg)


#Escape charecter
purse = "i have $20.5 you have $2.00"
extraxtCharacter =re.findall("\$[0-9.]+",purse)
print("Maximum:",max(extraxtCharacter))

# using list comprehension to
# perform conversion
lst=[['8814', '3846', '1132', '2823', '2301', '9551', '809', '8637', '1584', '2071', '1939', '4258', '4814', '1831', '6703', '6722', '9036', '9453', '4318', '9551', '3069', '5677', '3925', '6207', '6225', '4146', '8281', '4099', '4669', '971', '6270', '675', '3099', '2262', '9624', '7933', '8340', '118', '9141', '1495', '7146', '1833', '6640', '7303', '4553', '8500', '1138', '2211', '5134', '4034', '4671', '4', '2077', '3064', '9318', '219', '6622', '569', '9806', '3871', '4536', '9907', '4859', '7433', '7462', '3944', '5956', '2479', '3101', '4', '3', '42']]

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