class BinarySearch(list): # class inherits list

    def __init__(self, a, b):

        self.length = a

        for num in range(b, a * b + b, b):
            self.append(num)

if __name__ == "__main__":
    print(BinarySearch(20, 2))