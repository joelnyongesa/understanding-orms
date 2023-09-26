def find_needle(haystack):
    # your code here
    # Search from haystack, return index of needle
    for index, junk in enumerate(haystack):
        if junk == "needle":
            return f"found the needle at position {index}"
        
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))