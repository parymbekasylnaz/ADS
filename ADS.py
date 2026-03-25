#task1
def task1(n):
    if n == 0:
        return
    task1(n-1)
    print(n, end=" ")
task1(5)