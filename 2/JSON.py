from collections.abc import Iterable



class JSON:
    def __init__(self,typeInfo=False, typeInfoProperty="typeInfo",indent="\t"):
        self.typeInfo = typeInfo
        self.typeInfoProperty = typeInfoProperty
        self.indent = indent

    def toJSON(self, obj):
        return self.__toJSON__(obj)
    def __toJSON__(self,obj,depth = 0):
        if isinstance(obj, bool) or isinstance(obj, float) or isinstance(obj, int):
            if isinstance(obj, bool):
                if (obj):
                    return "true"
                else:
                    return "false"
            return str(obj)
        elif obj is None:
            return "null"
        elif isinstance(obj, str):
            return f"\"{obj}\""
        elif isinstance(obj, dict):
            res = f"\n{self.indent*depth}{{\n"
            for key in obj.keys():
                res += f"{self.indent*(depth+1)}\"{key}\" : {self.__toJSON__(obj[key], depth + 1)},\n"
            if (self.typeInfo):
                res += f"{self.indent*(depth+1)}\"{self.typeInfoProperty}\" : \"{dict.__name__}\""
            else:
                res = res[0:-2]
            res += f"\n{self.indent*depth}}}"
            return res
        elif isinstance(obj, Iterable):
            return self.__iterableToJSON__(obj,depth)
        else:
            res = f"\n{self.indent*depth}{{\n"
            for key in obj.__dict__.keys():
                res += f"{self.indent*(depth+1)}\"{key}\" : {self.__toJSON__(obj.__dict__[key], depth + 1)},\n"
            if (self.typeInfo):
                res += f"{self.indent*(depth+1)}\"{self.typeInfoProperty}\" : \"{type(obj).__name__}\""
            else:
                res = res[0:-2]
            res += f"\n{self.indent*depth}}}"
            return res
    def __iterableToJSON__(self, obj,depth):
        if (not isinstance(obj,Iterable)):
            return None;
        res = "["
        for i, o in enumerate(obj):
            if o is obj:
                res += "[]"
            else:
                res += self.__toJSON__(o, depth + 1)

            if (i != len(obj) - 1):
                res += ", "
        res += "]"
        return res;


if (__name__ == "__main__"):
    class P:
        def __init__(self, name):
            self.name = name

    a = JSON(True,"type_info","    ");
    print(a.toJSON(a))

