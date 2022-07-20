class Fourcal:
   def __init__(self, first, second):
        self.first = first
        self.second = second
   def add(self):
        result = self.first +self.second
        return result
a = Fourcal(4,2)
b = Fourcal(2,4)

print(a.add())