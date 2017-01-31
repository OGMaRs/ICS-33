#Kevin Luu 48783106
from goody import type_as_str  # Useful in some exceptions
from builtins import StopIteration
from collections import defaultdict
import copy
class DictList:
    def __init__(self,*data):
        self.dl = []
        if len(data) == 0:
            raise AssertionError
        for item in data:
            if type(item) != dict or len(item) == 0:
                raise AssertionError(" DictList.__init__: {errorItem} is not a dictionary".format(errorItem = item))
            else:
                self.dl.append(item)
                
    def __len__(self):
        counterList = []
        for item in self.dl:
            for key in item.keys():
                if key not in counterList:
                    counterList.append(key)
        return len(counterList)

    def __bool__(self):
        return len(self.dl) != 1
    
    def __repr__(self):
        thing = str(self.dl)
        newthing = thing.replace("[", "")
        finalthing = newthing.replace("]", "")
        return ("DictList({itemHere})".format(itemHere = finalthing))
    
    def __contains__(self, look):
        for item in self.dl:
            if look in item.keys():
                return True
        else:
            return False
    
    def __getitem__(self,find):
        if self.__contains__(find) == True:
            for item in self.dl[::-1]:
                if find in item.keys():
                    return item[find]
        else:
            raise KeyError("{thing} is not in DictList".format(thing = find))
    
    def __setitem__(self, change, value):
        if self.__contains__(change) == True:
            for item in self.dl[::-1]:
                if change in item.keys():
                    item[change] = value
                    break
        else:
            x = change
            self.dl.append(dict(x = value))
    
    def __delitem__(self, toDelete):
        if self.__contains__(toDelete) == True:
            for item in self.dl[::-1]:
                if toDelete in item.keys():
                    item.pop(toDelete, item[toDelete])
                    break
        else:
            raise KeyError("The key you wish to delete is not in any dictionary within the list")
    
    def __call__(self, callItem):
        toReturn = []
        if self.__contains__(callItem) == True:
            for i in range(len(self.dl)):
                if callItem in self.dl[i].keys():
                    toReturn.append((i,self.dl[i][callItem]))
            return toReturn
        else:
            return toReturn
    
    def __iter__(self):
        final = []
        for dictionaries in self.dl[::-1]:
            for things in sorted(dictionaries.keys()):
                if things not in final:
                    final.append(things)
                    yield things
    
    def items(self):
        present = self.__iter__()
        for key in present:
            yield (key,self.__getitem__(key))
    
    def collapse(self):
        masterList = defaultdict(set)
        answer = self.__iter__()
        for opener in answer:
            x = self.__getitem__(opener)
            masterList[opener] = x
        return dict(masterList)
    
    def __eq__(self,right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("Right operand is not a DictList or dictionary")
        else:
            y = right
            if type(right) == DictList:
                y = right.collapse()
            x= self.collapse()
            if x.keys() != y.keys():
                return False
            for key in y.keys():
                if x[key] != y[key]:
                    return False
                    break
            return True
        
    def __lt__(self, right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("Right operand is not a DictList or dictionary")
        else:
            start = self.collapse()
            z = right
            if type(right) == DictList:
                z = right.collapse()
            if len(start.keys()) >= len(z.keys()):
                return False
            for key in start.keys():
                if key not in z.keys():
                    return False
                    break
                if start[key] != z[key]:
                    return False
                    break
            return True
        
    def __gt__(self,right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("Right operand is not a DictList or dictionary")
        else:
            start = self.collapse()
            z = right
            if type(right) == DictList:
                z = right.collapse()
            if len(start.keys()) == len(z.keys()):
                return False
            for key in z.keys():
                if key not in start.keys():
                    return False
                    break
                if start[key] != z[key]:
                    return False
                    break
            return True
        
    def __add__(self, right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("Right operand is not a DictList or dictionary")
        else:
            if type(right) == DictList:
                final = copy.deepcopy(self)
                secondary = final.dl
                third = copy.deepcopy(right)
                fourth = third.dl
                secondary.extend(fourth)
                return final
            elif type(right) == dict:
                newDict = copy.deepcopy(self)
                newList = newDict.dl
                last = copy.deepcopy(right)
                newList.append(last)
                return newDict
    
    def __radd__(self,right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("Right operand is not a DictList or dictionary")
        else:
            begin = copy.deepcopy(right)
            end = copy.deepcopy(self)
            newThing = DictList(begin)
            toExtend = newThing.dl
            final = end.dl
            toExtend.extend(final)
            return newThing
    
    def __setattr__(self,name,value):
        if "dl" in  name:
            for element in self.__dict__:
                if element == name:
                    self.data[element].append(self.__dict__[element])
            self.__dict__[name] = value
        else:
            raise AssertionError("Incorrect value storage")


if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests
    d = DictList(dict(a=1,b=2), dict(b=12,c=13))
    print('len(d): ', len(d))
    print('bool(d):', bool(d))
    print('repr(d):', repr(d))
    print(', '.join("'"+x+"'" + ' in d = '+str(x in d) for x in 'abcx'))
    print("d['a']:", d['a'])
    print("d['b']:", d['b'])
    print("d('b'):", d('b'))
    print('iter results:', ', '.join(i for i in d))
    print('item iter results:', ', '.join(str(i) for i in d))
    print('d.collapse():', d.collapse())
    print('d==d:', d==d)
    print('d+d:', d+d)
    print('(d+d).collapse():', (d+d).collapse())
    d3 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d4 = dict(x='anx',b='two')
    print (d4 + d3)
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
