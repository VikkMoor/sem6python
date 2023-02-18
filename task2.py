"""Form array with indexes of elements in given range"""

start_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_element = int(input('Enter lower limit: '))
max_element = int(input('Enter upper limit: '))
result = [i for i in range(len(start_list)) if min_element <= start_list[i] <= max_element]
print(result)
