# import datetime as dt

# class Human:
#     def __init__(self, fname, lname, age):
#         self.firstname = fname
#         self.lastname = lname
#         self.age = age

#     def datebirth(self):
#         now = dt.datetime.now()
#         return now.year - self.age
        


#     def __str__(self):
#         return f"name : {self.firstname} {self.lastname}\nAge : {self.age}"

# h1 = Human("artin", "nouri", 12)
# print(h1.datebirth())


# class Teacher(Human):
#     def __init__(self, fname, lname, age, salary):
#         super().__init__(fname, lname, age)
#         self.salary = salary

#     def __str__(self):
#         return super().__str__() + f"\nsalary : {self.salary}"
    

# mojtaba = Teacher("mojtaba", "ghahri", 39, 1000)
# print(mojtaba)

# print("-"*50)


# class Student(Human):
#     def __init__(self, fname, lname, age, student_number):
#         super().__init__(fname, lname, age)
#         self.student_number = student_number

#     def __str__(self):
#         return super().__str__() + f"\nstudent number : {self.student_number}"

# artin = Student("artin", "nourian", 12, "0099")
# print(artin)

# print("-"*50)


# class Personnal(Human):
#     def __init__(self, fname, lname, age, date_join):
#         super().__init__(fname, lname, age)
#         self.date_join = date_join

#     def work_history(self):
#         now = dt.datetime.now()
#         return now.year - self.date_join

#     def datebirth(self):
#         return "nahar nakherdim"

#     def __str__(self):
#         return super().__str__() + f"\ndate_join : {self.date_join}"

# p1 = Personnal("naghi", "mamooli", 50, 1990)
# print(p1)
# print(p1.datebirth())

class Address:
    def __init__(self, city, street, alley, zipcode):
        self.city = city
        self.street = street
        self.alley = alley
        self.zipcode = zipcode

    def __str__(self):
        return f"address : {self.city} , {self.street}, {self.alley}, {self.zipcode}"

addr1 = Address("karaj", "baghestan", "sakineh32", "14151617181920")
addr2 = Address("LS", "baghestan", "sakineh32", "00141516")



class Human:
    def __init__(self, fname, lname, age, add):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.add = add


    def __str__(self):
        return f"name : {self.firstname} {self.lastname}\nAge : {self.age}\n{self.add}"


h1 = Human("sam", "karimkhani", 14, [addr1, addr2])
print(h1)

for i in h1.add:
    print(i)
    print("-"*50) 