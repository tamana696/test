class PhoneNumber:
    def __init__(self,number,type):
        self.number = number
        self.type = type
        
    def __str__(self):
        return f"{self.type}:{self.number}"
    

#phone1 = PhoneNumber("09123456789","mobile")
#print(phone1)