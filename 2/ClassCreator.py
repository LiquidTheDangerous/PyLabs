import inspect
import JSON

class ClassCreator:
    @staticmethod
    def CreateClass(ClassName : str):
        return globals()[ClassName].__new__(globals()[ClassName])
    @staticmethod
    def CreateClassFromDict(d: dict, typeInfoName="typeInfo"):
        if (not isinstance(d,dict)):
            return d
        if (typeInfoName not in d):
            return d
        className = d[typeInfoName]
        obj = ClassCreator.CreateClass(className)
        for key, val in d.items():
            if key == typeInfoName:
                continue
            if (isinstance(val,dict)):
                if (typeInfoName in val):
                    val = ClassCreator.CreateClassFromDict(val,typeInfoName)
            if(isinstance(val,list)):
                for i in range(len(val)):
                    val[i] = ClassCreator.CreateClassFromDict(val[i],typeInfoName)
            setattr(obj,key,val)
        return obj


if (__name__ == "__main__"):
    class Point:
        def __init__(self, x , y,z):
            self.x = x
            self.y = y
            self.z = z
        def __repr__(self) -> str:
            return f"x={self.x};y={self.y};z={self.z}"
    class Plane:
        def __init__(self,p1, p2, p3,other = None):
            self.p1 = p1;
            self.p2 = p2
            self.p3 = p3
            self.other = other
        def __repr__(self) -> str:
            res = ""
            for i in (self.p1,self.p2,self.p3):
                res += i.__repr__()
            return f"plane : {res}"
    plane = Plane(Point(0,0,0),Point(1,1,1),Point(3,4,5),[Point([1,Point(1,2,3)],1,2)])
    print(plane.__dict__)
    #{'p1': x=0;y=0;z=0, 'p2': x=1;y=1;z=1, 'p3': x=3;y=4;z=5, 'other': [x=[1, x=1;y=2;z=3];y=1;z=2]}
    print(plane)
    json = JSON.JSON(True)
    str = json.toJSON(plane)
    print(str)
    d = json.formJSONtoDict(str)
    print(d)
    plane2 = ClassCreator.CreateClassFromDict(d)
    print(plane2)
    print(plane2.__dict__)
    #{'p1': x=0;y=0;z=0, 'p2': x=1;y=1;z=1, 'p3': x=3;y=4;z=5, 'other': [x=[1, x=1;y=2;z=3];y=1;z=2]}
