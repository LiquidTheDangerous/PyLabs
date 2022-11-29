from typing import final

class ObjStream:
    def __init__(self, obj, func):

        if (hasattr(obj, "__iter__")):
            self._iter = iter(obj)

        elif (hasattr(obj, "__next__")):
            self._iter = obj

        else:
            raise AttributeError("obj is not iterable")

        self._func = func
    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iter)

    def filter(self,predicate):
        return Filter(self,predicate)

    def map(self,func):
        return Map(self,func)

    @final
    def reduce(self,init_value,BinaryFunction):
        result = init_value
        try:
            value = next(self)
            result = BinaryFunction(result,value)
            while(True):
                value = next(self)
                result = BinaryFunction(result, value)
        except StopIteration:
            return result
    @final
    def collect(self):
        return list(self)
    @final
    @staticmethod
    def int_stream(start, end, step = 1):
        return ObjStream(range(start,end,step),lambda x : x)

class Map(ObjStream):

    def __init__(self,obj, func):
        super().__init__(obj,func)

    def __next__(self):
        return self._func(next(self._iter))

class Filter(ObjStream):
    def __init__(self,obj,predicate):
        super().__init__(obj,predicate)

    def __next__(self):

        value = next(self._iter)

        while (not self._func(value)):
            value = next(self._iter)

        return value

def ExtendCollectionClass(cls):
    return type(f"extend_{cls.__name__}", (cls,ObjStream), {
        "__init__": cls.__init__
    })


if __name__ == "__main__":

    def f(x): return x * 2 + 1
    def pred(x): return x % 2 == 0

    lst = [1,2,3,4,5,6]

    for i in Map(Filter(lst,pred),f):
        print(i)

    print("------")

    for i in Filter(Map(lst,lambda x : x - 1),pred):
        print(i)
    print("------")
    

    @ExtendCollectionClass
    class TestCollection(list):
        def __init__(self,iterable):
            super().__init__(iterable)
    collection = TestCollection([1,2,3,4,5,6])
    result = collection.filter(lambda x : x % 2 == 1).map(str).reduce("",lambda x,y : f"{x}_{y}")
    print(result)
    res = Map.int_stream(1,2,3)
    print("------")
    
    lst = [1,2,3,4,5,5,5,3,6,7]
    def append(lst,value):
        lst.append(value)
        return lst

    result = TestCollection(lst).filter(lambda x : x%2).collect()
    print(result)
