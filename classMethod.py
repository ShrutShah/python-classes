class employee:
    count = 0
    rate = 1.04
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        employee.count += 1
        
    
    def ratechange(self):
        self.pay = self.pay * self.rate
        
    @classmethod
    def set_raise(cls, amount):
        cls.rate = amount
        
e1 = employee('Shrut', 50000)
e2 = employee('Piyush', 40000)
print(e1.name)
print(e1.pay)
e1.ratechange()
print(e1.pay)
print(employee.count)
employee.set_raise(1.05)
print(employee.rate)
