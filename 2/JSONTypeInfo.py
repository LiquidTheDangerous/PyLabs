from enum import Enum

class TypeInfo(Enum):
    Object = 0
    Array = 1
    boolean = 2
    number = 3
    string = 4
    null = 5

    @staticmethod
    def getType(string : str):
        string = string.strip("\n\t ")
        if (string[0] == '{'):
            return TypeInfo.Object
        if (string[0] == '['):
            return TypeInfo.Array
        if (TypeInfo.__isDigit__(string)):
            return TypeInfo.number
        if(string[0] == "\""):
            return TypeInfo.string
        if (string == "null"):
            return TypeInfo.null
        if (string == "false" or string == "true"):
            return TypeInfo.boolean


    @staticmethod
    def __isDigit__(string : str):
        string = string.strip('\t\n ')
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

if (__name__ == "__main__"):
    print(TypeInfo.getType(" {} "))
    print(TypeInfo.getType(" [] "))
    print(TypeInfo.getType(" 123 "))
    print(TypeInfo.getType(" 123.123 "))
    print(TypeInfo.getType(" \"123.123\" "))
    print(TypeInfo.getType(" null "))
    print(TypeInfo.getType(" false "))
    print(TypeInfo.getType(" true "))