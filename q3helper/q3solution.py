#Kevin Luu 48783106
#Helper functions for testing (both in this module and in bsc)
from predicate import is_prime

def primes(maxp=None):
    p = 2
    while maxp == None or p <= maxp:
        if is_prime(p):
            yield p
        p += 1

def lets(string):
    for let in string:
        yield let
    
def in_a_row(n,iterable):
    nextLet = iter(iterable)
    toReturn = set()
    counter = 1
    if n < 2:
        raise AssertionError("Length of iterable is not greater than 2")
    letter = nextLet.__next__()
    while True:
        try:
            if counter == n:
                toReturn.add(letter)
            x = nextLet.__next__()
            if letter == x:
                counter += 1
            elif letter != x:
                letter = x
                counter = 1
        except:
            break
    return toReturn
        

def differences(it1,it2):
    everything = zip(it1,it2)
    counter = 0
    for thing in everything:
        if thing[0] != thing[1]:
            yield (counter, thing[0], thing[1])
        counter +=1


def skipper(iterable,n=0):
    letter = iter(iterable)
    for item in letter:
        for times in range(n):
            try:
                letter.__next__()
            except:
                break
        yield item

def separate(pred,lst):
    if len(lst) == 0:
        return ([], [])
    else:
        onward = separate(pred,lst[1:])
        if pred(lst[0]) == True:
            return ([lst[0]] + onward[0], onward[1])
        if pred(lst[0]) == False:
            return (onward[0], [lst[0]] + onward[1])
    
def is_sorted(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] <= s[1]
    else:
        return is_sorted(s[1:]) and s[0] <= s[1]
        
def sort(l):
    if len(l) == 0:
        return []
    else:
        def less(item):
            return item < l[0]
        x = separate(less, l[1:])
        return sorted(x[0]) + [l[0]] + sorted(x[1])


def update_min_max(t,mm):
    if mm == (None, None):
        if t[0] < t[1]:
            return (t[0], t[1])
        else:
            return (t[1], t[0])
    else:
        small = t[1]
        big = t[0]
        if t[0] < t[1]:
            small = t[0]
            big = t[1]
        if mm[0] < small:
                small = mm[0]
        if mm[1] > t[1]:
                big = mm[1]
    return (small,big)

def min_max(l):
    if len(l) == 0:
        return (None,None)
    elif len(l) == 1:
        return (l[0],l[0])
    elif len(l) == 2:
        if l[0] < l[1]:
            return (l[0], l[1])
        else:
            return (l[1], l[0])
    else:
        begin = (l[0], l[1])
        end = min_max(l[1:])
        return update_min_max(begin,end)
        

if __name__ == '__main__':
    import driver, random
   
    print('\ndriver testing with batch_self_check:')
    driver.driver() # type quit in driver to return and execute code below
    
    from goody import irange
    from predicate import is_positive
    print('Testing separate')
    print(separate(is_positive,[]))
    print(separate(is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,
                   'to be or not to be that is the question'.split(' ')))

    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))

    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
