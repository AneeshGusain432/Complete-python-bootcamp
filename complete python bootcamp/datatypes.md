#TODO: I WROTE THIS CODE IN THE TERMINAL FOR PRACTICE

object types / data tupes 

bracket[]  curlybraces{}  ()parenthesis

- number : 1234, 3.1415, 3+4j, 0b111, Deciaml(),
Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2,'three'], 4.5], list(range(10))
Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- dictionary : {'food': 'spam', 'taste': 'yum'}, dict
(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs,txt'), open(r'c:\ham.bin' 'wb')
- None : None
- Function, modules, classes
- Advance: Decorators, Genrators, Iterators, 
MetaProgramming


<!-- sliceing practice -->

>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[0:3]
'012'
>>> num_list[0:7:4]
'04'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:8:2]
'0246'
>>> num_list[0:9:2]
'02468'
>>> num_list[0:6:2]
'024'
>>> num_list[0:9:3]
'036'
>>> num_list[0:9:4]
'048'



<!-- upper lower case -->

>>> chai = "Masala Chai"
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai   
'Masala Chai'




<!-- how to replace object in string -->

> chai = "lemon tea"
>>> print(chai.replace("lemon", "ginger"))
ginger tea
>>>       



<!-- how to split object -->

 chai = "lemon, ginger, masala, mint"                                      
>>> print(chai.split(", "))
['lemon', 'ginger', 'masala', 'mint']



<!-- how find object -->

>>> chai = "masala chai"
>>> print(chai.find("chai"))
7   



<!-- how to count object -->

>>> chai = "masala chai chai chai chai chai"
>>> print(chai.count("chai"))
5   




<!-- order formating -->

chai_type = "masala"
>>> quantity = 2
>>> order = " I ordered {} cups of {} chai"
>>> order 
' I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
 I ordered 2 cups of masala chai



 <!-- how to convert object list to string -->

 chai_variety = ["lemon", "masala", "ginger"]
>>> chai_variety
['lemon', 'masala', 'ginger']
>>> print(", ".join(chai_variety))
lemon, masala, ginger
>>> print("-".join(chai_variety))
lemon-masala-ginger



>>> genjutsu_type = ["koto amatsukami", "rinnegan", "mangekyu", "tusukuyoumi"]
>>> print("  ".join(genjutsu_type))
koto amatsukami  rinnegan  mangekyu  tusukuyoumi
>>> print(", ".join(genjutsu_type))
koto amatsukami, rinnegan, mangekyu, tusukuyoumi



<!-- len function  -->

>>> chai = " masala chai"
>>> chai
' masala chai'
>>> print(len(chai))
12  
>>> for letter in chai:
...  print(letter)
...   
m   
a   
s   
a   
l   
a   
    
c   
h   
a   
i   



<!-- \n -->

chai = "he said, \"masala chai is awesome\""
>>> chai
'he said, "masala chai is awesome"'
>>> chai = "masala\nChai"
>>> chai
'masala\nChai'
>>> print(chai)
masala
Chai
 chai = r"masla\nChai"
>>> print(chai)
masla\nChai



<!-- path -->

>>> chai = r"c:\user\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>>


<!-- list, array practice -->

>>> tea_varities = ["black", "Green", "Oolong", "white"]
>>> tea_varities
['black', 'Green', 'Oolong', 'white']
>>> print(tea_varities)
['black', 'Green', 'Oolong', 'white']
>>> print(tea_varities[0])
black
>>> print(tea_varities[3])
white
>>> print(tea_varities[-1])
white



 print(tea_varities[:2])
['black', 'Green']
>>> print(tea_varities[2:3])
['Oolong']
>>> print(tea_varities[2:2])
>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)



['black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:2] = ["lemon"]
>>> tea_varities
['black', 'lemon', 'Oolong', 'Herbal']



>>> tea_varities[1:3]
['lemon', 'Oolong']
>>> tea_varities[1:3] = ["Green", "Masala"]
>>> tea_varities
['black', 'Green', 'Masala', 'Herbal']



>>> tea_varities     
['black', 'Green', 'Masala', 'white']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1] = ["test", "test"]
>>> tea_varities     
['black', 'test', 'test', 'Green', 'Masala', 'white']
>>> tea_varities[1:3] = []
>>> tea_varities     
['black', 'Green', 'Masala', 'white']



<!-- loops -->

>>> tea_varities
['black', 'Green', 'Masala', 'white']
>>> for tea in tea_varities:
...  print(tea)
... 
black
Green
Masala
white



>>> for tea in tea_varities:
...  print(tea)
... 
black
Green
Masala
white
>>> for tea in tea_varities:
...  print(tea, end="-")
... 
black-Green-Masala-white->>>



tea_varities = ['black', 'Green', 'Masala', 'white']
>>> tea_varities
['black', 'Green', 'Masala', 'white']
>>> if "oolong" in tea_varities:
...     print("i have a oolong tea")

tea_varities.append("oolong")
>>> tea_varities
['black', 'Green', 'Masala', 'white', 'oolong']
>>>


>>> if "oolong" in tea_varities:
...     print("i have a oolong tea")
... 
i have a oolong tea



>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]



>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}



 chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green 
   
    for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh 





<!-- how to remove and add object in list -->

>>> tea_varities
['black', 'Green', 'Masala', 'white', 'oolong']
>>> tea_varities.pop()
'oolong'
>>>     
 tea_varities
['black', 'Green', 'Masala', 'white']



>>> tea_varities
['black', 'Green', 'Masala', 'white']
>>> tea_varities.remove("Green")
>>> tea_varities
['black', 'Masala', 'white']
>>> tea_varities.insert(1,"Green")
>>> tea_varities
['black', 'Green', 'Masala', 'white']




<!-- dictionry -->

chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'


chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> 



 chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green 


    for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh 



for Key, value in chai_types.items():
...     print(Key, value)
... 
Masala Spicy
Ginger Zesty
Green Fresh



>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"] = "citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'citrus'}




>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'citrus'}



>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'citrus'}
>>> chai_types.popitem()
('Earl Grey', 'citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}


 chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}

>>> chai_types_copy = chai_types.copy()



>>> tea_shop = {
... "chai": {"Masala" : "Spicy", "Ginger": "Zesty"},
... "tea" : {"Green": "Mild", "Black": "Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'




keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}


 new_dict = dict.fromkeys(keys, keys)          
 new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>> 




<!-- if and conditional -->

>>> if "Masala" in chai_types:
...     print("I have a Masala chai")
... 
I have a Masala chai

print(len(chai_types))
3



<!-- Tupels -->

>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')


>>> more_tea = ("herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

if "Green" in all_tea:
...     print("I have a Green tea")
... 
I have a Green tea


>>> more_tea = ("Herbal", "Earl Grey", "Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Green")
0
>>> len(more_tea)
3


>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, oolong) = tea_types
>>> black
'Black'
>>> oolong
'Oolong'


type(tea_types)
<class 'tuple'>
>>> type(more_tea)
<class 'tuple'>


<!-- string to int -->

 userscore
'200'
>>> userscore_in_int = int(userscore)
>>> userscore_in_int
200
