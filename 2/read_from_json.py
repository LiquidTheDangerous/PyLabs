from JSONpackage import ClassCreator, JSON
from task_2 import Person, Employee, Manager, Boss,Department
import sys
ClassCreator.SetModule(sys.modules[__name__])




if (__name__ == "__main__"):
    with open("json_boss.txt",'r') as file:
        json = JSON(True)
        string_json = file.read()
        boss_object_dict = json.formJSONtoDict(string_json)
        boss_object = ClassCreator.CreateClassFromDict(boss_object_dict)
        if (isinstance(boss_object,Boss)):
            print(boss_object)