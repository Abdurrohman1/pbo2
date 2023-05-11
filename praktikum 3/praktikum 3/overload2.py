class Math:
    def add(self, *args):
        total = 0
        for arg in args:
            total += arg
        return total
m = Math()
print(m.add(12))
print(m.add(50, 4))
print(m.add(8, 4, 16))
