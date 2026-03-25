#task1
def task1(n):
    if n == 0:
        return
    task1(n-1)
    print(n, end=" ")
print(task1(5))

#task2
def task2(n):
    if n == 0:
        return
    print(n, end=" ")
    task2(n-1)

print(task2(5))

#task3
def task3(n):
    if n == 1:
        return 1
    return n + task3(n - 1)

print(task3(5))

#task4
def task4(n):
    if n <= 1:
        return 1
    return n * task4(n - 1)

print(task4(5))

#task5
def task5(a, b):
    if b == 0:
        return 1
    return a * task5(a, b - 1)

print(task5(2, 4))

#task6
def task6(n):
    if n == 0:
        return 0
    return (n % 10) + task6(n // 10)

print(task6(572))

#task7
def task7(n):
    if n == 0:
        return 0
    return 1 + task7(n // 10)

print(task7(5729))

#task8
def task8(n):
    if n == 0:
        return
    print(n % 10, end="")
    task8(n // 10)

task8(1234)
print()

#task9
def task9(n):
    if n <= 1:
        return n
    return task9(n - 1) + task9(n - 2)

print(task9(6))

#task10
def task10(s):
    if len(s) <= 1:
        return "Palindrome"
    if s[0] != s[-1]:
        return "Not palindrome"
    return task10(s[1:-1])

print(task10("level"))
print(task10("hello"))

#task11
def task11(arr):
    if not arr:
        return 0
    return arr[0] + task11(arr[1:])

print(task11([3, 5, 2, 7]))

#task12
def task12(arr):
    if len(arr) == 1:
        return arr[0]
    m = task12(arr[1:])
    return arr[0] if arr[0] > m else m

print(task12([4, 9, 1, 7, 3]))

#task13
def task13(arr, target):
    if not arr:
        return 0
    c = 1 if arr[0] == target else 0
    return c + task13(arr[1:], target)

print(task13([1, 2, 3, 2, 2, 5], 2))

#task14
def task14(arr, target):
    if not arr:
        return "Not Found"
    if arr[0] == target:
        return "Found"
    return task14(arr[1:], target)

print(task14([4, 7, 1, 9, 3], 9))


# task15
def task15(arr):
    if len(arr) <= 1:
        return "Sorted"
    if arr[0] > arr[1]:
        return "Not sorted"
    return task15(arr[1:])


print(task15([1, 2, 4, 7, 9]))
print(task15([1, 5, 3, 8]))


# task16
def task16(arr, target, low, high):
    if low > high:
        return "Element not found"

    mid = (low + high) // 2

    if arr[mid] == target:
        return f"Element found at index {mid}"
    elif arr[mid] > target:
        return task16(arr, target, low, mid - 1)
    else:
        return task16(arr, target, mid + 1, high)


arr16 = [1, 3, 5, 7, 9, 11]
print(task16(arr16, 7, 0, len(arr16) - 1))