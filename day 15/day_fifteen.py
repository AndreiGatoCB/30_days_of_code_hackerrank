class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        dif = []
        for _ in range(len(self.__elements)):
            for _ in range(len(self.__elements)):
                dif.append(abs(self.__elements[0] - self.__elements[_]))
            self.__elements.remove(self.__elements[0])
        self.maximumDifference = max(dif)
# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
