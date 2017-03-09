class BinarySearch(list): # class inherits list

    def __init__(self, a, b):

        self.length = a

        for num in range(b, a * b + b, b):
            self.append(num)

    def search(self, numToSearch):

        count = 0
        index = -1

        first = 0
        last = len(self) - 1

        if numToSearch == self[first]:
            index = 0
        elif numToSearch == self[last]:
            index = last
        else:
            while first<last and index == -1:
                count = count + 1
                midpoint = (first + last)//2
                if self[midpoint] == numToSearch:
                    index = midpoint
                else:
                    if numToSearch < self[midpoint]:
                        last = midpoint-1
                    else:
                        first = midpoint+1

        if index == -1:
            count = count - 1

        return {"count": count, "index": index}

if __name__ == "__main__":
    bs = BinarySearch(20, 2)
    print(bs, bs.search(33))