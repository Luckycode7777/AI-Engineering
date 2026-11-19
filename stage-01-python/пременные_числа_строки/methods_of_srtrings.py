# x = 'bobpoc'.upper()
# # x.upper()

# print(x)

# -------------------------------------------------------
# y = 'GOBLIN'.lower()
# print(y)

# -------------------------------------------------------
# x = 'xoobiblic riX'
# # print(x.count('b', 3))
# print(x.find('b'))
# print(x.rfind('b'))
# print(x.index('i'))  # возвращается индекс подстроки
# print(x.replace('o','Z', 1))
# print(x.replace('o', '', 2))
# print(x.replace(' ', '-'))
# print(x.isalpha())

# -------------------------------------------------------
# y = '12345'
# # print(y.isdigit())
# print(y.rjust(8, '-'))
# print(y.ljust(8, '-'))

# -------------------------------------------------------
x = 'ivanov ivan ivanich'

print(x.split())
print(len(x.split()))

z = '23, 342,5653,6553,778'.split(',')
print(z)