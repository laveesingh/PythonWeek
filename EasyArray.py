# Initial Array class
class Array:

    alist = []  # Not encapsulated
    __blist = []  # encapsulated

    def __init__(this):
        '''This is the official constructor method of  Array class'''
        pass

    def length(this):
        '''This method finds out of the length of Array'''
        return len(this.alist)

    def insert_at_index(this, index, value):
        '''This method takes an index and a value and puts the value at that index, and shifts the values after this index to the right by one'''
        this.alist.insert(index, value)

    def insert_at_end(this, value):
        '''This method takes a value and puts it at the end of the array'''
        this.alist.append(value)

    def remove_by_index(this, index):
        '''This method takes an index and removes the value at that index'''
        del this.alist[index]

    def remove_by_value(this, value):
        '''This method takes a value and removes the first occurrence of the value in the array'''
        this.alist.remove(value)

    def __getitem__(this, index):
        return this.alist[index]

    def __repr__(this):
        return str(this.alist)


# array = Array()
# array.insert_at_end(10)
# array.insert_at_end(8)
# array.insert_at_end(5)
# array.insert_at_end(0)
# array.insert_at_end(7)
# array.insert_at_index(1, 17)
# array.insert_at_index(2, 100)
# array.insert_at_index(5, 3)
