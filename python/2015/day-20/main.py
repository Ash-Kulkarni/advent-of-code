def calculate_presents(house_num):
    num_presents = 0
    for elf_num in range(1, house_num + 1):
        if house_num % elf_num == 0:
            num_presents += elf_num * 10
    return num_presents

def calculate_presents_2(house_num):
    num_presents = 0
    for elf_num in range(1, house_num + 1):
        if house_num % elf_num == 0:
            if elf_num * 50 >= house_num:
                num_presents += elf_num * 11
    return num_presents

house_num = 786240
lowest = house_num
while house_num > 0:
    # print(house_num)
    check = calculate_presents_2(house_num)
    if check > 34000000:
        if house_num < lowest:
            lowest = house_num
            print(lowest)
    house_num -= 1
# print(lowest)

# for house_num in range(786240, 1000000):
#     print(house_num)
#     check = calculate_presents_2(house_num)
#     if check > 34000000:
#         print(house_num)
#         break


# print(calculate_presents_2(786240))
