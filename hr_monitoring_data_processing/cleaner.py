
def filter_nondigits(data: list) -> list:
    """
    Filters out non-digit strings from the input list and converts valid strings to integers.
    Returns: A list of integers with valid data only.
    """
    
    clean_data = [] #create an empty list to store cleaned data
    for items in data:
        # for every item in data, strip newline character, check if it is digit, then convert to integer
        if items.strip().isdigit():
            clean_data.append(int(items.strip()))
    
    return clean_data
