from collections import defaultdict
import re
from goody import type_as_str
import math
# Use day_dict, days_in_month, and is_leap_year in your yesterday function

day_dict ={ 1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
           10 : 31,
           11 : 30,
           12 : 31}

def is_leap_year(year:int)->bool:
    return (year%4 == 0 and year%100 != 0) or year%400==0

def days_in(month:int,year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])

def yesterday(date:str)->str:
    to_match = re.match('(?P<Month>(1[0-2]|[1-9])|(0[1-9]))/(?P<Day>0?[1-9]|0?[1-3][0-1]|[1-2][0-9])/(?P<Year>\d{4}|\d{2})$', date)
    assert to_match , "Incorrect date input"
    month = int(to_match.group('Month'))
    day = int(to_match.group('Day'))
    year = int(to_match.group('Year'))
    if day > days_in(month, year):
        raise AssertionError("Incorrect Date Input")
    if year < 100 :
        year = int(year) + 2000
    if day -1 > 0:
        return (str(month) + '/' + str(day -1) + '/' + str(year))
    elif day -1 == 0:
        if month == 1:
            return (str(12) + '/' + str(31) + '/' + str(int(year) - 1))
        else:
            return (str(month - 1) + '/' + str(days_in(month -1, year)) + '/' + str(year))
        

class Point:

    def __init__(self,x,y):
        if type(x)!= int or type(y) != int:
            raise AssertionError(str(x) + "or " + str(y)+ " is not an int")
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return 'Point({xcord},{ycord})'.format(xcord = self.x, ycord = self.y)
    
    def __str__(self):
        return '(x={xpoint},y={ypoint})'.format(xpoint = self.x, ypoint = self.y)
    
    def __bool__(self):
        if self.x == 0 and self.y ==0:
            return False
        else:
            return True
    
    def __add__(self,right):
        if type(right) == Point:
            return Point(self.x + right.x, self.y + right.y)
        else:
            raise TypeError(str(right) + "is not a point object, try again")

    def __mul__(self,right):
        if type(right) == int:
            return Point(self.x * right, self.y * right)
        else:
            raise TypeError(str(right) + "is not a point object, try again")
            
    def __rmul__(self,left):
        return self.__mul__(left)
    
    def __lt__(self,right):
        if type(right) == Point:
            if math.sqrt(((self.y - 0 )**2) + ((self.x- 0) **2)) < math.sqrt(((right.y - 0 )**2) + ((right.x- 0) **2)):
                return True
            else:
                return False
        elif type(right) == int or float:
            if math.sqrt(((self.y - 0 )**2) + ((self.x- 0) **2)) < right:
                return True
            else:
                return False
        else:
            raise TypeError(str(right) + "is not a point/int/float object, try again")
     
        
    def __getitem__(self,index):
        if type(index) != int and type(index) != str:
            raise IndexError(str(index) + " is not x, y, 0 or 1") 
        else:
            if index == 0 or index == 'x':
                return self.x
            if index == 1 or index == 'y':
                return self.y
            else:
                raise IndexError(str(index) + " is not x, y, 0 or 1")
        
    def __call__(self,x,y):
        if type(x) != int or type(y) != int:
            raise AssertionError("{xthing} or {ything} is not an integer, try a new input".format(xthing = x, ything = y))
        else:
            self.x = x
            self.y = y
            return None

        

class History:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def __getattr__(self,name):
        pass
    
    def __setattr__(self,name,value):
        if name.find('_prev') != -1:
            raise NameError("{namething} has '_prev' present inside, try again".format(namething = name))
        else:
            for element in self.__dict__:
                if element == name:
                    self.dictionary[element].append(self.__dict__[element])
            self.__dict__[name] = value
            

    def __getitem__(self,index):
        secondary = defaultdict(set)
        if index > 0:
            raise IndexError
        elif index == 0:
            for element in self.__dict__.keys():
                if type(self.__dict__[element]) == int:
                    secondary[element] = self.__dict__[element]

if __name__ == '__main__':
    from goody import irange
    from predicate import is_prime
    import driver
   
    # Feel free to test other cases as well

    print('\nTesting yesterday:')
    print(yesterday('2/29/2000'))
    print(yesterday('09/4/88'))
    print(yesterday('10/01/1988'))
    print(yesterday('1/01/00'))
    print(yesterday('9/4/88'))
    
    print('\ndriver testing with batch_self_check:')
    driver.driver()
