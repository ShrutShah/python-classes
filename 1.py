class employee:
    def __init__(self, fname, lname, no):
        self.fname = fname
        self.lname = lname
        self.no = no
    
    def fullname(self):
        print('{} {}'.format(self.fname, self.lname))
        
        
        
e1 = employee('Shrut', 'Shah', 1)
e1.fullname()

employee.fullname(e1)
