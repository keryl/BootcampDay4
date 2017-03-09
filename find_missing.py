def find_missing(list1, list2):

    # initialize dict to store occurrences of numbers in both lists e.g.
    # numbers = { 1: 2, 3: 1 }

    numbers = {}

    # loop through the dictionary and return if a a number that occurred once is found

    for number, occurrence in numbers.items():
        if occurrence == 1:
            return number
