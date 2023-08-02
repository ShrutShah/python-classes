class employee:
    count = 0
    rate = 1.04
    def __init__(self, n, p):
        self.name = n
        self.pay = p
        employee.count += 1
        
    
    def ratechange(self):
        self.pay = self.pay * self.rate
        
    @classmethod
    def set_raise(cls, amount):
        cls.rate = amount
        
    @classmethod
    def from_string(cls, stri):
        n, p = stri.split('-')
        return cls(n, p)
        

str1 = "Shrut-50000"
e1 = employee.from_string(str1)
print(e1.name)
print(e1.pay)
  
