
class JsonSplitter:
    def __init__(self,string : str,chrOpen,chrClosed):
        self.string = self.__unpackString__(string,chrOpen,chrClosed)
        self.currentPos = 0
        self.hasNext = True
    def __unpackString__(self, string: str, chrOpen, chrClosed):
        string = string.strip("\t\n ")
        stack = list()
        first_pos = -1
        second_pos = -1
        match_value = False
        for index, char in enumerate(string):
            if (len(stack) == 0 and char in (chrOpen, chrClosed)):
                if (first_pos == -1):
                    first_pos = index
                elif (second_pos == -1):
                    second_pos = index
            if (char == chrOpen):
                stack.append(chrOpen)
            elif (char == chrClosed):
                stack.pop()
        return string[first_pos+1:second_pos].strip("\t\n ")

    def nextLine(self):
        stack = list()
        start_pos = self.currentPos
        second_pos = -1
        for index in range(self.currentPos,len(self.string)):
            char = self.string[index]
            if (char == '{'):
                stack.append('{')
            elif (char == '}'):
                stack.pop()
            elif (char == '['):
                stack.append('[')
            elif (char == ']'):
                stack.pop()
            if(char == ','):
                if(len(stack) == 0):
                    second_pos = index
                    break;
        if (second_pos == -1):
            second_pos = len(self.string)
            self.hasNext = False
        self.currentPos = second_pos + 1
        return self.string[start_pos:second_pos].strip("\t\n ")

if (__name__ == "__main__"):
    a = JsonSplitter("{ name : name,proper : {name : name, name : name, 4},pr : 123 }",'{','}')
    while(a.hasNext):
        print(a.nextLine())
    a = JsonSplitter("[1,2,3,4,[1,2,3],4]",'[',']')
    while(a.hasNext):
        print(a.nextLine())

