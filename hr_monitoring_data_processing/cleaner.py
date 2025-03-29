
def filter_nondigits(data: list) -> list:
    """
    Filters out non-digit strings from the input list and converts valid strings to integers.
    Returns:
        list: A list of integers with valid data only.
    """
    # Print the data before filtering
    clean_data = []
    for items in data:
        # Strip newline character, check if it is digit, then convert to integer
        if items.strip().isdigit():
            clean_data.append(int(items.strip()))
    
    return clean_data

data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"] 
print(filter_nondigits(data))