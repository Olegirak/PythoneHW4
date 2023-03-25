# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

n=int(input("Введите количество кустов = "))
num=list(int(input(f" Введите количество ягод {i} куста = ")) for i in range(1,n+1))
print(num)
summax=num[0]+num[1]+num[n-1]
nmax=0
for i in range(1,n):
    if i!=n-1:
        sum=num[i]+num[i-1]+num[i+1]
    else:
        sum=num[i]+num[i-1]+num[0]
    if sum>summax:
        summax=sum
        nmax=i

print(f" Максимальная сбор = {summax} ягод  c {nmax} куста")