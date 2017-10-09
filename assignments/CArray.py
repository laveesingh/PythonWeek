
class MyList:
    __alist = []  # it's hidden, thus supporting, encapsulation

    def __init__(self):
        pass

    def __getitem__(self, index):
        return self.__alist[index]

    def __setitem__(self, index, value):
        if type(value) != int:
            raise TypeError("Only integer values are supported!")
        self.__alist[index] = value

    def sort(self):
        self.__alist.sort()
        return self.__alist

    def sum(self):
        return sum(self.__alist)

    def prod(self):
        return reduce(int.__mul__, self.__alist)

    def add_begin(self, value):
        self.__alist = [value] + self.__alist

    def add_end(self, value):
        self.__alist.append(value)

    def add_index(self, index, value):
        self.__alist.insert(index, value)

    def __repr__(self):
        return str(self.__alist)
