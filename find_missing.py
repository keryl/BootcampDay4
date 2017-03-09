def find_missing(list1, list2):

    # initialize dict to store occurrences of numbers in both lists e.g.
    # numbers = { 1: 2, 3: 1 }

    numbers = {}

    # go through both lists and add occurrences to numbers

    for num in list1:
        occurrence = numbers.get(num, 0) # get any existing occurrence of num
        numbers[num] = occurrence + 1 # increment occurrence by 1 and save it back to the dict

    for num in list2:
        occurrence = numbers.get(num, 0) # get any existing occurrence of num
        numbers[num] = occurrence + 1 # increment occurrence by 1 and save it back to the dict

    # loop through the dictionary and return if a a number that occurred once is found

    for number, occurrence in numbers.items():
        if occurrence == 1:
            return number

