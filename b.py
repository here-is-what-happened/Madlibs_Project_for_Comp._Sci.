# option = input("Word sorter or number statistics? ").lower
num_list = []
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
    range_of_nums_list = max(num_list) - min(num_list)



    mid_point = length_of_list // 2
    first_half_list = sorted_num_list[:mid_point]
    second_half_list = sorted_num_list[mid_point:]
    median1 = (first_half_list[len(first_half_list) // 2] + first_half_list[(len(first_half_list) - 1) // 2]) / 2
    median2 = (first_half_list[len(second_half_list) // 2] + second_half_list[(len(second_half_list) - 1) // 2]) / 2
    print(median1, median2)


    
num_stats()





    
