# create tuple
a = (1, 1.1, 'a', [4, 5, 6], {'a': 1, 'b': 2}, None, True)
a = ()
b = tuple()
b = (1,)
a = [1, 2.1, 3]
tuple(a)
b = tuple('abc')

# retrive tuple
a = (1, 2.1, 'd')
a[0]
a[2]

# update tuple
a = (1, 1.1, 'a')
a[0] = 'a'
a = (1, 2, 3)

# delete tuple
a = (1, 1.1, 'a')
del a[0]
del(a) 