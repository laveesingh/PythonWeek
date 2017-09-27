class Array:

    DTYPE_DIFF_ERROR = "Datatype of value cannot be different from the datatype of array, to know datatype of array, use array.dtype"

    def __init__(self, n=0, dtype=int, val=0):
        '''This is the official constructor method of  Array class'''
        self.__array = [val] * n
        self.dtype = dtype

    def __getitem__(self, index):
        return self.__array[index]

    def __repr__(self):
        return str(self.__array)

    def length(self):
        return len(self.__array)

    def insert_at_index(self, index, value):
        if type(value) != self.__dtype:
            raise TypeError(self.DTYPE_DIFF_ERROR)
        self.__array.insert(index, value)

    def insert_at_end(self, value):
        if type(value) != self.__dtype:
            raise TypeError(self.DTYPE_DIFF_ERROR)
        self.__array.append(value)

    def remove_by_index(self, index):
        del self.__array[index]

    def remove_from_end(self):
        self.__array.pop()

    def remove_by_value(self, value):
        self.__array.remove(value)


