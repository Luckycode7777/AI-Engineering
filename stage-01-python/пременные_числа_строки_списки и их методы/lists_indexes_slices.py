# -----------------------------------------------------------
numbers = [34, 23, 12, 28, 9, 15]

print(numbers[4])  # 9
print(numbers[-1])  # 15
# print(numbers[7])  # IndexError: list index out of range

print(numbers[1: 5])
print(numbers[-6:-1])
numbers[-1]= 'bob' # замена значения по индексу
print(numbers)

del(numbers[0]) # удаление значения по индексу == 0
print(numbers)
print('*' * 20)


# копися
a = [1, 2, 3]
c = a
c = ['100'] # нет копии C меняет A
print(a)
print(c)


print('*' * 20)
b = a[:] # есть копия B не меняет A. Каждая переменная ссылается на свой список
b = [1, 'bob', 3]
print(a)
print(b)
