# option = input("Word sorter or number statistics? ").lower
num_list = []
variance_list = []
mean_absolute_deviation = []
word_list = []
word_ratios = []

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
    if max_count == 1:
        mode = 'None'
    range_of_nums_list = max(num_list) - min(num_list)



    mid_point = (max(num_list) + min(num_list)) / 2
    mid = length_of_list // 2
    first_half_list = sorted_num_list[:mid]
    second_half_list = sorted_num_list[mid:]
    median1 = (first_half_list[len(first_half_list) // 2] + first_half_list[(len(first_half_list) - 1) // 2]) / 2
    median2 = (second_half_list[len(second_half_list) // 2] + second_half_list[(len(second_half_list) - 1) // 2]) / 2
    interquartile_range = abs(median1 - median2)

    for num in num_list:
        b = (num - mean) ** 2
        variance_list.append(b)
    p_variance = sum(variance_list) / length_of_list
    s_variance = sum(variance_list) / ( length_of_list - 1 )

    standard_deviation = p_variance ** 0.5
    if mean == 0:
        coefficient_of_variation = None
    else:
        coefficient_of_variation = standard_deviation / mean

    for num in num_list:
        c = abs(num - mean)
        mean_absolute_deviation.append(c)
    mean_absolute_deviation_amount = sum(mean_absolute_deviation) / len(mean_absolute_deviation)




    print(f"Mean: {mean}")
    print(f"Median {median}")
    print(f"Mode: {mode}")
    print(f"Range: {range_of_nums_list}")
    print(f"Midpoint: {mid_point}")
    print(f"Max: {max(num_list)}")
    print(f"Min: {min(num_list)}")
    print(f"Sum: {sum(num_list)}")
    print(f"Quartile 1: {median1}")
    print(f"Quartile 3: {median2}")
    print(f"Interquartile range: {interquartile_range}")
    print(f"Population variance: {p_variance}")
    print(f"Sample variance: {s_variance}")
    print(f"Standard deviation: {standard_deviation}")
    if coefficient_of_variation is None:
        print("Coefficient of variation (CV): None")
    else:
        print(f"Coefficient of variation (CV): {coefficient_of_variation:.2%}")
    print(f"Mean absolute deviation: {mean_absolute_deviation_amount}")

def word_sorter():
    #filler
    # alphabetical
    # reverse alphabetical
    # number of characters
    

    total_words = int(input("How many words would you like to enter? (Remember enter 1 at a time): "))
    for _ in range(total_words):
        d = input("Enter a word: ")
        word_list.append(d)

    alphabetically = sorted(word_list, key=str)
    reverse_alphabetically = sorted(word_list, reverse=True, key=str)

    print(reverse_alphabetically, alphabetically)



    vowels = 'aeiouAEIOU'
    for word in word_list:
        consonants = 0
        vowels = 0
        for letter in word:
            







    print(f"Alphabetically: {alphabetically}")
    print(f"Reverse alphabetically: {reverse_alphabetically}")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")

        
word_sorter()