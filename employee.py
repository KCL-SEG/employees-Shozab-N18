"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Contract:
    def __init__(self, monthly,hours_worked,hourly):
        self.monthly = monthly
        self.hours_worked = hours_worked
        self.hourly = hourly

    def get_salary_type(self):
        if(self.monthly != None):
            return self.monthly
        elif(self.hourly != None):
            return self.hourly * self.hours_worked
        else:
            return None
    
    def get_description(self):
        if(self.monthly != None):
            return f'monthly salary of {self.monthly}'
        elif(self.hourly != None and self.hours_worked != None):
            return f'contract of {self.hours_worked} hours at {self.hourly}/hour'
        else:
            return ''

class Commission:
    def __init__(self,fixed,contracts,commission_per_contract):
        self.fixed = fixed
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract
    
    def get_commission(self):
        if (self.fixed != None):
            return self.fixed
        elif(self.contracts != None and self.commission_per_contract != None):
            return self.contracts * self.commission_per_contract
        else:
            return None

    def get_description(self):
        if (self.fixed != None):
            return f'receives a bonus commission of {self.fixed}'
        elif(self.contracts != None and self.commission_per_contract != None):
            return f'receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract'
        else:
            return ''

class Employee:
    def __init__(self, name,contract,commission):
        self.name = name
        self.contract = contract
        self.commisssion = commission

    def get_pay(self):
        pay = 0
        if (self.contract.get_salary_type() != None):
            pay += self.contract.get_salary_type() 
        if (self.commisssion.get_commission() != None):
            pay += self.commisssion.get_commission()
        return pay

    def __str__(self):
        if self.contract.get_description() != '' and self.commisssion.get_description() == '':
            string = self.contract.get_description() + '.'

        elif  self.contract.get_description() != '' and self.commisssion.get_description() != '':
            string = self.contract.get_description() + ' and ' + self.commisssion.get_description()+ '.'

        elif  self.contract.get_description() == '' and self.commisssion.get_description() != '':
            string = self.commisssion.get_description()+ '.'

        # elif  self.contract.get_description() == '' and self.commisssion.get_description() == '':
        #     string = self.contract.get_description() + ' and ' + self.commisssion.get_description()+ '.'

        return f'{self.name} works on a {string}  Their total pay is {self.get_pay()}.' 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',Contract(4000,None,None),Commission(None,None,None))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',Contract(None,100,25),Commission(None,None,None))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',Contract(3000,None,None),Commission(None,4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',Contract(None,150,25),Commission(None,3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',Contract(2000,None,None),Commission(1500,None,None))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',Contract(None,120,30),Commission(600,None,None))
