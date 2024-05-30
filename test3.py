# create list
a = [1, 1.1, 'a', [1], (1, 1.1), {1, 2}, {'a': 1}, None, True]
a = []
b = list()
a = (1, 2.1, 3)
list(a)
b = list('abc')

# retrive list
a = [1, 1.1, 'a']
print(a)
print([1, 1.1, 'a'])
a = [1, 1.1, 'a']
a[0]
a[1]
a[2]
a[3]
a[-1]
a[-2]
a[-3]
a[-4]
a = [1, 2, 3]
a.index(3)

# update list
a = [1, 1.1, 'a']
a[0] = 'а'
a[1] = 'б'
a[-1] = 'в'
a = [1, 2, 3]

a = [1, 2, 3]
a.append(4)
a.append(['a', 'b'])
a = [1, 2, 3]
a.insert(0, 4)
a = [1, 2, 3]
a.insert(3, 4)
a = [1, 2, 3]
a.insert(-1, 4)
a = [1, 2, 3]
a.extend([4, 5, 6])

# delete
a = [1, 1.1, 'a']
del a[0]
del a[-1]
del a[-1]
del a

a = [1, 2, 3]
a.clear()
a = [1, 2, 3]
a.pop()
a = [1, 'ab', 3]
a = [1, 2, 'ab']
a.remove('ab')

