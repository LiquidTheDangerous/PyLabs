from collections.abc import Iterable
from JsonSplitter import JsonSplitter
from JSONTypeInfo import TypeInfo

class JSON:
    def __init__(self,typeInfo=False, typeInfoProperty="typeInfo",indent="\t"):
        self.typeInfo = typeInfo
        self.typeInfoProperty = typeInfoProperty
        self.indent = indent

    def toJSON(self, obj):
        return self.__toJSON__(obj)
    def __toJSON__(self,obj,depth = 0):
        if isinstance(obj, bool) or isinstance(obj, float) or isinstance(obj, int) or obj is None or isinstance(obj, str):
            return self.__primitiveToJSON__(obj)
        elif isinstance(obj, dict):
            return self.__dictToJSON__(obj,depth)
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
    def __primitiveToJSON__(self,obj):
        if isinstance(obj, bool) or isinstance(obj, float) or isinstance(obj, int) or obj is None or isinstance(obj, str):
            if (isinstance(obj,bool)):
                if (obj):
                    return "true"
                else:
                    return "false"
            if (isinstance(obj,int) or isinstance(obj,float)):
                return str(obj)
            if (obj is None):
                return "null"
            if (isinstance(obj,str)):
                return f"\"{obj}\""
    def __dictToJSON__(self, obj,depth):
        res = f"\n{self.indent*depth}{{\n"
        for key in obj.keys():
            res += f"{self.indent*(depth+1)}\"{key}\" : {self.__toJSON__(obj[key], depth + 1)},\n"
        if (self.typeInfo):
            res += f"{self.indent*(depth+1)}\"{self.typeInfoProperty}\" : \"{type(obj).__name__}\""
        else:
            res = res[0:-2]
        res += f"\n{self.indent*depth}}}"
        return res

    def formJSONtoDict(self, string: str):
        json_type = TypeInfo.getType(string);
        if (json_type == TypeInfo.Object):
            splitter =  JsonSplitter(string,"{","}")
            dict_result = dict()
            while(splitter.hasNext):
                line = splitter.nextLine()
                key,value = map(lambda x : x.strip("\t\n "),line.split(':',1))
                key = key.strip("\"")
                dict_result[key] = self.formJSONtoDict(value)
            return dict_result
        if(json_type == TypeInfo.Array):
            splitter = JsonSplitter(string, "[", "]")
            list_result = list()
            while(splitter.hasNext):
                value = splitter.nextLine();
                list_result.append(self.formJSONtoDict(value))
            return list_result
        if(json_type == TypeInfo.boolean):
            if (string == "true"):
                return True
            elif(string == "false"):
                return False
        if (json_type == TypeInfo.number):
            try:
                return int(string)
            except ValueError:
                return float(string)
        if(json_type == TypeInfo.string):
            return string.strip("\"\t\n ");
        if (json_type == TypeInfo.null):
            return None
if (__name__ == "__main__"):
    class P:
        def __init__(self, name,other):
            self.other = other
            self.name = name

    a = JSON();
    print("TO JSON")
    string = a.toJSON(P("Andrey",[1,2,3,P("hello","world")]))
    print(string,"\n")
    print("FROM JSON")
    res = a.formJSONtoDict(string)
    print(res)
    print(res['other'])
    print(res['name'])
    print(res['other'][3]['name'])

