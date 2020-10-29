from math import gcd
class Fraction:
  def __init__(self, num, den): 
    self.x = num
    self.y = den
    self.reduce()
  def reduce(self):  
    self.x = (self.x//(gcd(self.x, self.y)))
    self.y = (self.y//(gcd(self.x, self.y)))
  def __add__(self, other):
    new_n = (self.x*other.y)+(other.x*self.y)
    new_d = self.y*other.y
    return Fraction(new_n, new_d)
  def __sub__(self, other):
    new_n = abs(self.x*other.y)-(other.x*self.y)
    new_d = self.y*other.y
    return Fraction(new_n, new_d)
  def __mul__(self, other):
    new_n = self.x*other.x
    new_d = self.y*other.y
    return Fraction(new_n, new_d)
  def __truediv__(self, other):
    new_n = self.x*other.y
    new_d = self.y*other.x
    return Fraction(new_n, new_d)
  def __float__(self):
    return self.x/self.y
  def __str__(self):
    return (str(self.x)+"/"+str(self.y))
iterations = int(input("How many times should the fraction continue? "))
count = Fraction(1,1)
for i in range(iterations):
  count = Fraction(1,1) + Fraction(1,1)/count
  print(count)