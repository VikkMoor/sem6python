"""Fill array with terms of an arithmetic progression (an = a1 + (n-1) * d)"""

a1 = int(input("Enter an initial term of an arithmetic progression: "))
d = int(input("Enter a common difference of arithmetic progression: "))
n = int(input("How much members do you want: "))
list3 = [(a1 + (i - 1) * d) for i in range(1, n + 1)]
print(list3)
