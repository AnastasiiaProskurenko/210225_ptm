x = [1]

a, *_ = x

print(a, _)


x = [(1, 2), (3, 4, 5, 6), (2, 3, 4, 5, 6)]

for item, *_ in x:
    print(item)