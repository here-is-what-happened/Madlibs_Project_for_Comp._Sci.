def calculate_median(lst):
    # 1. Sort the list
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # 2. Check if empty
    if n == 0:
        return None
        
    # 3. Find the middle index
    mid = n // 2
    
    # If odd, return the middle element
    if n % 2 != 0:
        return sorted_lst[mid]
    # If even, return the average of the two middle elements
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0

data = [4, 5, 8, 9, 10, 17]
print(calculate_median(data)) 


