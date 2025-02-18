with open('txt/my_file.txt') as file:

    lines = file.readlines()

    # n=0
    # for line in lines:
    #     string = line.split()
    #     for i in range(len(string)):
    #         if string[i] == '1':
    #             n += 1

    # print(f'Кількість елементів у вхідному файлі, які рівні 1: {n}')

    # string = lines[13].split()
    # print(string[7])

    # r=0
    # for line in lines:
    #     string = line.split()
    #     string = list(map(int, string))
    #     for i in range(len(string)):
    #         r += string[i]

    # print(f'Сума елементів у вхідному файлі: {r}')
    
    # r=0
    # string = lines[2].split()
    # for i in range(len(string)):
    #     r += int(string[i])
    

    # string = lines[5].split()
    # for i in range(len(string)):
    #     r += int(string[i])
    

    # string = lines[8].split()
    # for i in range(len(string)):
    #     r += int(string[i])
    

    # string = lines[11].split()
    # for i in range(len(string)):
    #     r += int(string[i])
    # print(r)

    r=0
    for line in lines:
        string = line.split()
        string = list(map(int, string))
        m=0
        for i in string:
            if i > m:
                m = i
        r += m

    print(f'Сума максимальних елементів у вхідному файлі: {r}')