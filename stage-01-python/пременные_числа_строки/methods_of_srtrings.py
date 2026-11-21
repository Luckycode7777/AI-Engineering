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
# x = 'ivanov ivan ivanich'

# print(x.split())  # split - разбил строку на части по пробелам(по дефолту) >>> ['ivanov', 'ivan', 'ivanich']
# print(len(x.split()))  # длина 3

# z = '23,342,5653,6553,778'.split(',')
# print(z)  # >>> split - разбил строку на части >>> ['23', '342', '5653', '6553', '778']

# z = '-'.join(z)
# print(z)  # >>> join - соеденгил по "-" 23-342-5653-6553-778

# w = 'ivanov ivan ivanich'  # split - разбил строку по букве "i", join - соеденгил по "-"
# w = '-'.join(w.split('i'))
# print(w)  # >>> -vanov -van -van-ch

# q = '   Bob  \n'  # удаляет пробелы и преносы слева и справа
# print(q.strip())  # >>> Bob     # ЕЩЕ ЕСТЬ rstrip и lstrip

# s = '   test . '.upper().replace('S','Z').strip()
# print(s)

# ----------------------------------------------------------
x = 'Hello\nworld\nhi\nbye'
print(x)