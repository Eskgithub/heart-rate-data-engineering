from cleaner import filter_nondigits

def average(clean_data: list) -> float:
    """
    Calculate the average heart rate from the given clean data.
    """
    # Initialize a variable to hold the total sum of the heart rates
    total = 0 
    
    # check if clean_data is empty, if so, return an empty list as no average can be computed
    if not clean_data:
        return []
    else: #Loop through each heart rate in the clean_data list, add it to total
        for rate in clean_data:
            total += rate
        return total / len(clean_data) # devide the sum to length of items in clean_data

def maximum(clean_data: list) -> float:
    """
    Find the maximum value in the heart rate data list.
    Returns 0 if the list is empty.
    """
    if not clean_data: 
        return []
    max_value = clean_data[0]
    # Loop through each heart rate value in the clean_data list
    for heart_rate in clean_data:
    
    # If the current heart rate is greater than the current max_value, update max_value
        if heart_rate > max_value:
            max_value = heart_rate
    return max_value


def variance(clean_data: list) -> float:
    """
    Calculate the variance of the person's heart rate data.
    Returns None if the list has fewer than 2 values.
    """
    if not clean_data:  
        return []
    #mean_value = sum(clean_data) / len(clean_data)
    n = len(clean_data)
    avg = average(clean_data)
    new_value = 0
    
    #Loop through each heart rate value and calculate the squared difference between the current heart rate and the average
    for item in clean_data:
        result = (item-avg) **2
    
    # Add the squared difference to the total sum
        new_value += result
    return new_value/n

def standard_deviation(clean_data: list) -> float:
    """
    Calculate the standard deviation of the person's heart rate data.
    Returns None if the list has fewer than 2 values.
    """
    if not clean_data:  
        return []
    
    # Call the 'variance' function to calculate the variance of the data
    var = variance(clean_data)
    
    # Calculate the standard deviation by taking the square root of the variance
    stddev = var ** 0.5
    return stddev
    

