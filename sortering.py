numbers = []
for i in range(1,10):
    tal = int(input('Ta in ett tal'))
    numbers.append(tal)
    print(numbers)
    numbers.sort()
    print(numbers)
    with open('numbers.txt','w+') as file:
        for numb in numbers:
            file.write(str(numb))