class Math:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a
m = Math()
print(m.add(10))
print(m.add(9, 4))
print(m.add(8, 4, 10))