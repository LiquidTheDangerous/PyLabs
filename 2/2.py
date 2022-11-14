import JSONpackage
import sys

JSONpackage.ClassCreator.SetModule(sys.modules[__name__])

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    @property
    def Name(self):
        return self.name

class Department:
    def __init__(self, departmentName, address):
        self.departmentName = departmentName
        self.address = address
    @property
    def DepartmentName(self):
        return self.departmentName
    @property
    def Address(self):
        return self.Address


class Employee(Person):
    def __init__(self, name, surname, department: Department):
        super().__init__(name, surname)
        self.department = department
    @property
    def Department(self):
        return self.department


class Manager(Employee):
    def __init__(self, name, surname, department: Department, employees : list):
        super().__init__(name, surname, department)
        self.employees = employees

class Boss(Employee):
    def __init__(self, name, surname, department: Department, managers : list):
        super().__init__(name, surname, department)
        self.managers = managers

dep = Department("PNRPU, ITAS","Stud gorodok, Dedykina")
p1 = Employee("Andrey","Semenov",dep)
p2 = Employee("Dmitri","Aksenov",dep)
p3 = Employee("Kostya","Checkin",dep)
p4 = Employee("Anna","Luzina",dep)
m1 = Manager("Aleksandr", "Petrenko",dep,[p1,p2])
m2 = Manager("Oleksandr","Opletin",dep,[p3,p4])
boss = Boss("Tashkinov","Anatoli",dep,[m1,m2])


with open("json_boss.txt","w") as file:
    json = JSONpackage.JSON(True,indent="  ")
    string_json = json.toJSON(boss)
    
    file.write(string_json)

    print("boss __dict__ : ")
    print(boss.__dict__)
    dict_boss = json.formJSONtoDict(string_json)
    boss_obj_from_dict = JSONpackage.ClassCreator.CreateClassFromDict(dict_boss)
    print("Object.__dict__")
    print(boss_obj_from_dict.__dict__)
    if (isinstance(boss_obj_from_dict,Boss)):
        print("boss is instance Boss")
