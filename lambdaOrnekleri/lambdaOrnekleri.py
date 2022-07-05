"""def square(num): return num ** 2
numbers = [1,3,5,8]

result = list (map(square, numbers))
print(result)

for item in map(square, numbers):
    print(item)
"""

"""numaralar = [2,4,6,8]
sonuc = list( map (Lambda num: nnum ** 2, sayilar) )

spuare = lambda num: num ** 2
print (sonuc)"""


square = lambda num: num ** 2
number = [1,2,3,4,5,6,8,9,10,12]

def check_even(num): 
    return num % 2 == 0

#result= list(filter(check_even, number))
result= list(filter(lambda num: num % 2 == 0, number))

print(result)