a = set()
print(a)
a = set([1, 10, 5, 'hello', 2.1, 'a'])
print(a)
b = {1, 4, 'hello', 'hey', 5}
print(b)
c = set()
c.add(1)
c.add(2)
c.add('hello')
c.add(10)
print(c)
c.add(2)
print(c)
for elements in c:
    print (elements)
my_list = [1, 2, 1, 1, 5, 'hallo', 'hallo']
print(my_list)
print('---------------')
my_set = set()
for el in my_list:
    my_set.add(el)
print(my_set)
my_set1 = set(my_list)
print(my_set1)
my_list1 = list (my_set1)
print(my_list1)

d = {1, 3, 5, 'hello', 'hey'}
print(5 in d)
print (15 not in d)

list2 = [1, 1, 3, 5, 5, 10, 10, 10, 32]

print(sum(set(list2)))

def my_func (input_set, input_list):
    if len(input_list) > len(input_set):
        return False
    for list_el in input_list:
        if list_el not in input_set:
            return False
    return True

print(my_func({1, 2, 3, 10, 4, 5, 'hello'}, [5]))
print(my_func({1, 2, 3, 10, 4, 5, 'hello'}, [5, 4, 1, 'hello']))
print(my_func({1, 2}, [3]))
print(my_func({1, 2, 3, 4, 5}, [2, 3, 10]))
print(my_func({1, 2, 3, 10, 4, 5, 'hello'}, [1,2,3,10,4,5]))