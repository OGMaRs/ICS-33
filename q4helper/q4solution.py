#Kevin Luu 48783106
import inspect
import itertools
from functools import reduce

def code_metric(file):
    file = open(file,"r")
    lines_in = file.readlines()
    not_empty = filter((lambda x: x if len(x.split()) > 0 else ""), lines_in)
    final = map((lambda x:(1, len(x.rstrip()))), not_empty)
    return reduce((lambda x,y:(x[0] + y[0], x[1] + y[1])), final)
    file.close()

def tour_cost(perm,cost):
    mutated = perm
    mutated = mutated + (perm[0],)
    return sum(map(lambda x:cost(x[0],x[1]) , zip(mutated[:-1], mutated[1:])))
    
def trav_sales(n,cost):
    listy= itertools.permutations(range(n))
    value = min(list(listy), key = lambda x: (tour_cost(x, cost)))
    return (tour_cost(value,cost),value)

def sum_count(alist,target,r):
    thingie = itertools.combinations(alist, r)
    x = filter(lambda x: x if sum(x) == target else '', thingie )
    return len(list(x))

# Define Dumpable here
# It must appear before Counter (so can be used as a base class)
class Dumpable:
    def get_state(self):
        final = {}
        x = list(filter(lambda x: x if not inspect.isfunction(self.__dict__[x]) else "", self.__dict__))
        for item in x:
            final[item] = self.__dict__[item]
        return final
         
class Counter(Dumpable):
    def __init__(self,init_value=0):
        self._value = init_value

    def __str__(self):
        return str(self._value)
        
    def reset(self):
        self._value = 0
        
    def inc(self):
        self._value += 1
        
    def value_of(self):
        return self._value

class Modular_Counter(Counter):
    def __init__(self,value,modulus):
        Counter.__init__(self,value)
        self._modulus = modulus
    
    def __str__(self):
        return Counter.__str__(self)+' mod '+str(self._modulus)
        
    def inc(self):
        if self.value_of() == self._modulus - 1:
            Counter.reset(self)
        else:
            Counter.inc(self)
        
    def modulus_of(self):
        return self._modulus

# Testing Script

if __name__ == '__main__':
    print('\nTesting code_metric')
    print(code_metric('cmtest.py'))
    print(code_metric('collatz.py'))
    print(code_metric('q4solution.py'))  # A function analyzing the file it is in
    
    print('\nTesting tour_cost')
    print(tour_cost((1,3,0,2),lambda x,y: (x-y)**2))
    print(tour_cost((1,3,5,2,0,4),lambda x,y: (x-y)**2))
    print(tour_cost((1,3,5,2,0,4,6),lambda x,y: 1 if y == (x+5) % 8 else 2))
    
    print('\nTesting trav_sales')
    print(trav_sales(4,lambda x,y: (x-y)**2))
    print(trav_sales(6,lambda x,y: (x-y)**2))
    print(trav_sales(7,lambda x,y: 1 if y == (x+5) % 7 else 2))
    
    print('\nTesting sum_count')
    print(sum_count(range(5),5,2))
    print(sum_count([3,3,3],6,2))
    print(sum_count([x**2 for x in range(10)],78,4))
    print(sum_count(5*[10],30,3))
    
    print('\nTesting Dumpable via Modular_Counter')
    c = Counter(5)           
    c.afunc = lambda x : x + 1
    mc = Modular_Counter(0,3)
    mc.afunc = lambda x : x + 1
    print(c.get_state())
    print(mc.get_state())
    
    import driver
    driver.driver()
 
    

