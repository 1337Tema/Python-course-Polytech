numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_num = sum(numbers[:4]) + sum(numbers[5:])
count_num = len(numbers)
average = sum_num / count_num
numbers[4] = average

print("Измененный список:", numbers)
