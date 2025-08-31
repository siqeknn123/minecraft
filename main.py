with open("maps/land3.txt", 'r') as file:
    summa = 0
    for line in file:
        line_lst = line.split(" ")
        for num in line_lst:
            summa += int(num)
        print(summa)