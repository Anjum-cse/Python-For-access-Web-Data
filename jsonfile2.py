import json
inputdetails = '''[

{
   "name" : "anjum",
 "id" : "7890",
 "mail": "@.com"
},

{ "name" : "veer",
 "id" : "7777",
 "mail": "@t.com"
}
]'''

information = json.loads(inputdetails)

print('User count:', len(information))
for item in information:
    print("Name:", item['name'])
    print("ID:", item['id'])
    print("Mail:", item['mail'])
