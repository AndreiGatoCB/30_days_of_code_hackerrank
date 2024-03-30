class ContOnes:
    def __init__(self, n_):
        self.r = str()
        while n_ >= 1:
            if n_ % 2 == 0:
                n_ /= 2
                self.r = '0' + self.r
            else:
                n_ = (n_ - 1) / 2
                self.r = '1' + self.r

    def consecutive(self):
        max_count = 1
        count = 1
        for i in range(len(self.r)):
            try:
                if self.r[i] == '1' and self.r[i + 1] == '1':
                    count += 1
                    if count > max_count:
                        max_count += 1
                    else:
                        pass
                else:
                    count = 1
            except IndexError:
                break
        return max_count


co = ContOnes(5)
print(co.consecutive())
