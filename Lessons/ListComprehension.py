a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
b = []
for num in a:
    b.append(num*2)
print(b)

c = [num * 2 for num in a]
print(c)

e = []
for i in range(1, 21):
    e.append(i*2)
print(e)

d = [i * 3 for i in range(1, 35)]
print(d)

arr = [34, 21, 43, 12, 3, 4, 6, 8, 0, -2, -123]
print(arr)

arr_f = []
for i in arr:
    if i < 10:
        arr_f.append(i)
print(arr_f)
print('-------')
arr_ff = [i for i in arr if i > 0]
print(arr_ff)
print('------------')
arr_fff = [i ** 3 for i in arr if i > 0]
print(arr_fff)

print('----------------')
words = ['hello', 'hey', 'goodbye', 'piano', 'hi', 'poker', 'pockerface']
words_filtrated = [i for i in words if len(i) <= 5]
print(words_filtrated)
print('----------------')
t = [i * 2 for i in range(20, 1, -1) if i % 2 == 0]
print(t)
print('----------------')
words_1 = [i+'.' for i in words if len(i) >= 5]
print(words_1)