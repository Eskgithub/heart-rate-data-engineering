from cleaner import filter_nondigits

#data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]
#clean_data = filter_nondigits(data)

def average(clean_data: list) -> float:
    """
    Calculate the average heart rate from the given clean data.
    """
    total = 0
    if clean_data == []:
        return []
    else:
        for rate in clean_data:
            total += rate
        return round((total / len(clean_data)), 2)

def maximum(clean_data: list) -> float:
    """
    Find the maximum value in the heart rate data list.
    Returns 0 if the list is empty.
    """
    if not clean_data: 
        return []
    max_value = clean_data[0]
    for heart_rate in clean_data:
        if heart_rate > max_value:
            max_value = heart_rate
    return max_value

def variance(clean_data: list) -> float:
    """
    Calculate the variance of the person's heart rate data.
    Returns None if the list has fewer than 2 values.
    """
    if len(clean_data) < 2:  
        return None
    mean_value = sum(clean_data) / len(clean_data)
    squared_diffs = [(x - mean_value) ** 2 
                     for x in clean_data]
    return sum(squared_diffs) / (len(clean_data) - 1)

def standard_deviation(clean_data: list) -> float:
    """
    Calculate the standard deviation of the person's heart rate data.
    Returns None if the list has fewer than 2 values.
    """
    if len(clean_data) < 2:  
        return []
    var = variance(clean_data)
    std = int(var ** 0.5)
    return round(std, 2)

