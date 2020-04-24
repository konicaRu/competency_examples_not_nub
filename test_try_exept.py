import random
class Driver:
    __name = "Hill"
    __age = 26
    __weight = 55

    def nam_drv(self):
        raise NotImplementedError()

    try:
        nam_drv()

    except NotImplementedError:
        print("finish the function.")

    def pr_nam(self):
        return self.__name

    def ag_drv(self, ag):
        self.__age = ag

    def pr_age(self):
        return self.__age

    def weg_drv(self, we):
        self.__weight += we

    def pr_weg(self):
        return self.__weight




dig = int(input())
a = []
count = 0
for i in range(100):
    a.append(random.randint(1, 50))
    b = a[i]
    count += 1
    if a[i] == dig:
        break
else:
    raise NotImplementedError('Вы вели много цифр')
print(count)
print(a)

try:
    a = int(input())
    b = int(input())
    print(a * b)
except Exception:
    print("ERROR")
a = [7, 4, 5, 6, 6, 8, 9, 7, 14]
try:
    min = a[7, 5]
    front_max = a[0]
except TypeError as e:
    print(e)
try:
    for i in range(9):
        if a[i] <= min:
            min = a[i]
        if a[i] < front_max and a[i] > min:
            front_max = a[i]
except IndexError:
    print('InErr')
except TypeError:
    print('TyErr')
except:
    print('AllErr')
try:
    print(min, front_max)
    print(a)
except:
    print('Err')
