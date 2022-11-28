
from pyDatalog import pyDatalog
from random import randrange
from random import choice
from random import randint

if __name__ == "__main__":
    pyDatalog.create_terms('X,Y,Z,Sum,Avg,random_sum,N,result')
   
   
   

    magic_number = 888888

    #Сумма арифметической  прогрессии [1,X]
    Sum[X] = ((1 + X)*X)/2

    #Среднее арифметической  прогрессии [1,X]
    #Avg[X] = Sum[X]/X
    Avg[X] = (X + 1)/2

    random_numbers = [randrange(1, magic_number) for _ in range(100)]

    (result["random_sum"] == sum_(Z, for_each=Z)) <= (Z.in_(random_numbers))
    # N = range(1,100)

    print(f"Sum 1...{magic_number}")
    print(Sum[magic_number] == X)

    print(f"Avg 1...{magic_number}")
    print(Avg[magic_number] == X)

    print("Random sum: ")
    print(result["random_sum"] == X)

    print("Median")
    print(random_numbers[50])
