import json
data = '''{
"name"  : "anjum",
"phone" : {
   "type" : "intl",
 "number" : "01687150000"
},

"email" :{
  "hide"  : "yes"
}
}'''
info= json.loads(data)
print("Name:", info['name'])
print('Hide:', info['email']['hide'])

