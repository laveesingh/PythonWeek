
class BigInteger:

    __num = []

    def __init__(self, init):

        from collections import Iterable

        if not init:
            pass
        if type(init) == int:
            if init > 10**18:
                raise OverflowError("Integer overflow")
            self.__num = map(int, str(init))
        elif isinstance(init, Iterable):
            self.__num = map(int, init)
        else:
            raise TypeError("Initializer can only be integer or iterable type")

    def __add__(self, other):
        print self, other
        anum = self.__num
        bnum = other.__num
        maxlen = max(len(anum), len(bnum))
        anum = [0]*(maxlen - len(anum) + 1) + anum
        bnum = [0]*(maxlen - len(bnum) + 1) + bnum
        cnum = [0] * len(anum)
        carry = 0
        for i in xrange(len(anum)-1, -1, -1):
            amt = (anum[i] + bnum[i] + carry)
            cnum[i] = amt % 10
            carry = amt / 10
        return self.trim(cnum)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __repr__(self):
        return str(self.__num)
        # return ''.join(str(s) for s in self)

    def trim(self, alist):
        ind = -1
        for i in xrange(len(alist)):
            if(alist[i] == 0):
                ind = i
            else:
                break
        alist = alist[ind+1:]
        return alist

a = BigInteger(1234)
print a
b = BigInteger(113)
print b
print a+b
