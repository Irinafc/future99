from pprint import pprint
from typing import Iterator

goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200,
    },
    {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 500,
    },
    {
        'name': 'REALME C25s',
        'brand': 'REALME',
        'price': 400,
    }
]

'''pprint(sorted(goods, key=lambda item: item['price']))

apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
print(apple_list)

numbers = ['1','2','3','4','5']

numbers = list(map(int,numbers))
print(numbers)'''

names_list = ['Данил', 'Никита', 'Настя', 'Катя']
surnames_list = ['Петров', 'Иванов', 'Даниловна', 'Никитовна']

'''full_name = list(map(lambda name,surname: f'{name} {surname}',names_list,surnames_list))

print(full_name)

for name,surname in zip(names_list,surnames_list):
    print (name,surname)'''

index = []

for i, item in enumerate(goods):
    index.append({i:item})

pprint(index)

















