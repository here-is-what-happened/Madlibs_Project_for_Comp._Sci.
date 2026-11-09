# option = input("Word sorter or number statistics? ").lower
num_list = []
variance_list = []
word_list = []

def num_stats():
    # Reminder for later of stuff:
    # mean, median, range, mode
    # interquartile range
    # variance and standard deviation
    # min and max
    # skew and mean absolute deviation
    amount = int(input("How many numbers would you like to enter? "))
    for _ in range(amount):
        a = int(input("Enter a number: "))
        num_list.append(a)

    sorted_num_list = sorted(num_list)
    length_of_list = int(len(num_list))

    mean = sum(num_list)/length_of_list
    median = (sorted_num_list[length_of_list // 2] + sorted_num_list[(length_of_list - 1) // 2]) / 2
    mode = None
    max_count = 0
    for item in set(num_list):
        count = num_list.count(item)
        if count > max_count:
            max_count = count
            mode = item
    if mode == None:
        mode = 'None'
    range_of_nums_list = max(num_list) - min(num_list)



    mid_point = length_of_list // 2
    first_half_list = sorted_num_list[:mid_point]
    second_half_list = sorted_num_list[mid_point:]
    median1 = (first_half_list[len(first_half_list) // 2] + first_half_list[(len(first_half_list) - 1) // 2]) / 2
    median2 = (second_half_list[len(second_half_list) // 2] + second_half_list[(len(second_half_list) - 1) // 2]) / 2
    interquartile_range = abs(median1 - median2)

    for num in range(length_of_list):
        b = (num - mean) ** 2
        b.append[variance_list]
    variance = sum(variance_list) / length_of_list

    standard_deviation = variance ** 0.5
    coefficient_of_variation = standard_deviation / mean












    print(f"The mean is {mean}")
    print(f"The median is {median}")
    print(f"The mode is {mode}")
    print(f"The range is {range_of_nums_list}")
    print(f"The midpoint is {mid_point}")
    print(f"The max is {max(num_list)}")
    print(f"The min is {min(num_list)}")
    print(f"The sum is {sum(num_list)}")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")


num_stats()

    
