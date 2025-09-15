class Even_num:
    def __init__(self, num):
        self.num = num
        self.curr_num = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.curr_num += 2
        if self.curr_num <= self.num:
            return self.curr_num
        else:
            raise StopIteration

for n in Even_num(20):
    print(n)