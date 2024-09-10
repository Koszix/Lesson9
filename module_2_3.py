my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
positive = []
while start < len(my_list):
    if my_list[start] >= 1:
        print(my_list[start])
        start += 1
        continue
    positive.append(my_list[start])
    start += 1