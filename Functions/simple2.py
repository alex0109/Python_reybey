import random
import math

opp = random.randint(0, 100)

def func1(number):
    result = math.sqrt(number)
    print("Корень из", number, "это", result)

def func2(number):
    result = number**2
    print("Квадрат из", number, "это", result)

def func3(number):
    result = number**3
    print("Куб из", number, "это", result)

func1(opp)
func2(opp)
func3(opp)
