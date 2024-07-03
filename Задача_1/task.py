"""
1.	Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1
out = list()
while a > 0:
    out.append(arr[a])
    a = a // 1.7
out.merge_sort()

"""
a = len(arr) - 1
out = list()
while a > 0:                    # O(n)
    out.append(arr[a])          # O(1)
    a = a // 1.7
out.merge_sort()                # O(n * log(n))

O(n) * O(1) + O(n*log(n)) -> O(n*log(n))