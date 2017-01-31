#Kevin Luu #48783106
from collections import defaultdict
from goody import type_as_str
import copy
class Bag:
    def __init__(self, letterList = None):
        self.bag = defaultdict(int)
        if letterList == None:
            pass
        else:
            for letter in letterList:
                self.bag[letter] = letterList.count(letter)
                
    
    def __repr__(self):
        data = []
        for key in self.bag.keys():
            for times in range(self.bag[key]):
                data.append(key)
        return 'Bag({listItems})'.format(listItems = data)
            
    def __str__(self):
        if len(self.bag) == 0:
            return 'Bag()'
        else:
            strReturn = 'Bag('
            for key,value in self.bag.items():
                strReturn += '{x}[{y}],'.format(x = key, y = value)
            else:
                strReturn = strReturn[:-1] + ')'
            return strReturn

    def __len__(self):
        length = 0
        for value in self.bag.values():
            length += value
        return length
    
    def unique(self):
        return len(self.bag)
    
    def __contains__(self, element):
        return element in self.bag
    
    def count(self, element):
        if element not in self.bag:
            return 0
        else:
            return self.bag[element]
        
    
    def add(self, element):
        if element in self.bag:
            self.bag[element] += 1
        else:
            self.bag[element] = 1
    
    def __add__(self, right):
        if type(self) != Bag or type(right) != Bag:
            raise TypeError ("One of the values is not a bag object")
        else: 
            first = copy.deepcopy(self)
            second = copy.deepcopy(right)
            for item in second.bag:
                if item in first.bag:
                    first.bag[item] = first.bag[item] + second.bag[item]
                else:
                    first.bag[item] = second.bag[item]
            return first
        
        
    def remove(self, letter):
        if letter not in self.bag:
            raise ValueError("Value is not in bag")
        else:
            self.bag[letter] -= 1
            if self.bag[letter] == 0:
                self.bag.pop(letter)

        
    def __eq__(self, right):
        if type(right) != Bag:
            return False
        else:
            return self.bag == right.bag
        
        
    def __ne__(self, right):
        if type(right) != Bag:
            return True
        else:
            return self.bag != right.bag
        
        
    def __iter__(self):
        final = []
        for letter in self.bag:
            for occurence in range(self.bag[letter]):
                final.append(letter)
        for value in final:
            yield value

if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
