import xml.etree.ElementTree as ET
input = '''<person>
<per>
    <entity   x='11'>
                      <name> Veer </name>
                      <phone> +880168715352 </phone>

    </entity>

    <entity   x='15'>
                      <name> zara </name>
                      <phone> +880168715000 </phone>

    </entity>
</per>
</person>'''
person = ET.fromstring(input)
lst = person.findall('per/entity')
print('User Count:', len(lst))

for item in lst:
    print("Attri:", item.get("x"))
    print("Name:", item.find('name').text)
    print("phone:", item.find('phone').text)
