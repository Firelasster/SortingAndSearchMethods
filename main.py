from random import randint
import time
import matplotlib.pyplot as plt


def fillNum(nums, n):
    for i in range(n):
        nums.append(randint(0, 6500))


def sort(nums, n):
    flag = True  # Для запуска цикла
    while flag:
        flag = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                # Сравниваем элементы,меняем местами
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Если предыдущее меньше последующего,то flag=True для продолжения работы
                flag = True


numbers1 = []
numbers2 = []
numbers3 = []
n1 = 2500
n2 = 3500
n3 = 6500

# Работа с 2500 элементами
fillNum(numbers1, n1)
numbers1[2] = 1000
print('Массив до сортировки(2500 элементов):\n' + str(numbers1))
tic1 = time.perf_counter()
sort(numbers1, n1)
toc1 = time.perf_counter()
print('Массив после сортировки:' + str(
    numbers1))  # показываю,что сортировка работает.В дальнейшем  выводить массивы не буду.

# Работа с 3500 элементами
fillNum(numbers2, n2)
numbers2[5] = 2000
tic2 = time.perf_counter()
sort(numbers2, n2)
toc2 = time.perf_counter()

# Работа с 6500 элементами
fillNum(numbers3, n3)
numbers3[2] = 5000
tic3 = time.perf_counter()
sort(numbers3, n3)
toc3 = time.perf_counter()

print(f"Сортировка для 2500 элементов заняла {toc1 - tic1:0.4f} секунд")
print(f"Сортировка для 3500 элементов заняла {toc2 - tic2:0.4f} секунд")
print(f"Сортировка для 6500 элементов заняла {toc3 - tic3:0.4f} секунд")

plt.plot([n1, n2, n3], [toc1 - tic1, toc2 - tic2, toc3 - tic3])
plt.show()


# ---------------------
# Интерполяционный поиск
def InterpolationSearch(nums, key):
    lowIndex = 0
    highIndex = (len(nums) - 1)
    while lowIndex <= highIndex and nums[lowIndex] <= key <= nums[highIndex]:
        index = lowIndex + int(
            ((float(highIndex - lowIndex) / (nums[highIndex] - nums[lowIndex])) * (key - nums[lowIndex])))
        if nums[index] == key:
            return index
        if nums[index] < key:
            lowIndex = index + 1;
        else:
            highIndex = index - 1;
    return -1


# Возвращает -1,если ключ не найден

tic4 = time.perf_counter()
print(InterpolationSearch(numbers1, 1000))
toc4 = time.perf_counter()
tic5 = time.perf_counter()
print(InterpolationSearch(numbers2, 2000))
toc5 = time.perf_counter()
tic6 = time.perf_counter()
print(InterpolationSearch(numbers3, 5000))
toc6 = time.perf_counter()

print(f"Интерполяционный поиск для 2500 элементов занял {toc4 - tic4:0.4f} секунд")
print(f"Интерполяционный поиск для 3500 элементов занял {toc5 - tic5:0.4f} секунд")
print(f"Интерполяционный поиск для 6500 элементов занял {toc6 - tic6:0.4f} секунд")
plt.plot([n1, n2, n3], [toc4 - tic4, toc5 - tic5, toc6 - tic6])
plt.show()
