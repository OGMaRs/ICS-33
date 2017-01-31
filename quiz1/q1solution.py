#Kevin Luu 48783106 Quiz 1
from collections import defaultdict

def between(low : int, high : int) -> bool:
    if high <= low:
        raise AssertionError
    else:
        def between2(num : int) -> bool:
            return num >= low and num <= high
        return between2

def  both(p1 : callable, p2: callable):
    def testing(number : int) -> bool:
        return p1(number) and p2(number)
    return testing
    
def sort_descendants(d : {str:[int]}) -> [str]:
    return sorted(d.keys(), key = lambda x: len(d.get(x)), reverse = False)

def sort_generations(d : {str:[int]}) -> [(str,[int])]:
    return sorted(d.items(), key = lambda x: len(x[1]) , reverse = True)

def big_family(d : {str:[int]}) -> {str}:
    return {e for e in d if sum(d[e]) >= 10}
    
def big_word_map(words : str) -> {str:{str}}:
    return {e : {(",".join(set(e)))} for e in words.split() if len(e) >3}

def near1(s : str, dist : int) -> {str:{str}}:
    new_dict = {}
    for i in range(len(s)):
        if i == 0:
            new_dict[s[i]] = (",".join(set(s[i : (i + dist + 1)])))
        for x in range(dist):
            right = i + (x + 2)
            if right <= len(s):
                for y in range(dist):
                    left = i - (y + 1)
                    if left >= 0:
                        new_dict[s[i]] = (",".join(set(s[left: right])))
    return new_dict

def near2(s : str, dist : int) -> {str:{str}}:
    freq = defaultdict(str)
    for i in range(len(s)):
        if i == 0:
            freq[s[i]] = (",".join(set(s[i : (i + dist + 1)])))
        for x in range(dist):
            left = i - (x + 1)
            if left >= 0:
                for y in range(dist):
                    right = i + (y + 2)
                    if right <= len(s):
                        freq[s[i]] = (",".join(set(s[left: right])))
    return freq  



if __name__ == '__main__':
    from goody import irange
    from predicate import is_prime
   
    # Feel free to test other cases as well
    
    print('Testing between: teenager')
    teenager = between(13,19) 
    print( [(a,teenager(a)) for a in irange(12,20)] )
    
    print('\nTesting between: middle_ager')
    middle_ager = between(30,50) 
    print( [(a,middle_ager(a)) for a in irange(29,51)] )
        
    print('\nTesting both: prime and between 50 and 60 inclusive')
    check = both(is_prime, lambda x : 50 <= x <= 60) 
    print([(i,check(i)) for i in irange(48,62)])
        
    print('\nTesting both: lower-case and consonant')
    check = both(lambda x : 'a' <= x <= 'z', lambda x : x not in 'aeiou') 
    print([(c,check(c)) for c in "Mr. Smith Goes to Washington"])
        

    print('\nTesting sort_descendants: ')
    family = dict(David=[6,4,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(sort_descendants(family))

    print('\nTesting sort_descendants: ')
    family = dict(Allen=[6,4,8],Dody=[3,5],Emile=[5,3],Harold=[6,6,6],Louis=[4,4,4,2,4])
    print(sort_descendants(family))
       
    print('\nTesting sort_generations:')
    family = dict(David=[6,5,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(sort_generations(family))
    
    print('\nTesting sort_generations:')
    family = dict(Allen=[12],Dody=[15],Emile=[8],Harold=[6,6,6],Louis=[4,4,4,2,4],Robert=[6,12])
    print(sort_generations(family))
    
    
    print('\nTesting big_family:')
    family = dict(David=[6,5,8],Muriel=[3,5],Barbara=[5,3],Chester=[6,6,6],Ingrid=[4,4,4,2,4])
    print(big_family(family))

    print('\nTesting big_family:')
    family = dict(Allen=[12],Dody=[15],Emile=[8],Harold=[6,6,6],Louis=[4,4,4,2,4],Robert=[6,12])
    print(big_family(family))

    print('\nTesting big_word_map:')
    print(sorted(big_word_map('To be or not to be that is the question').items()))

    print('\nTesting big_word_map:')
    print(sorted(big_word_map('When in the course of human events').items()))

    
    print('\nTesting near1: radar 1-3')
    print(sorted(near1('radar',1).items()))
    print(sorted(near1('radar',2).items()))
    print(sorted(near1('radar',3).items()))
    
    print('\nTesting near1: whiplash 1-7')
    print(sorted(near1('whiplash',1).items()))
    print(sorted(near1('whiplash',2).items()))
    print(sorted(near1('whiplash',3).items()))
    print(sorted(near1('whiplash',4).items()))
    print(sorted(near1('whiplash',5).items()))
    print(sorted(near1('whiplash',6).items()))
    print(sorted(near1('whiplash',7).items()))
    
    print('\nTesting near2: radar 1-3')
    print(sorted(near2('radar',1).items()))
    print(sorted(near2('radar',2).items()))
    print(sorted(near2('radar',3).items()))
    
    print('\nTesting near2: whiplash 1-7')
    print(sorted(near2('whiplash',1).items()))
    print(sorted(near2('whiplash',2).items()))
    print(sorted(near2('whiplash',3).items()))
    print(sorted(near2('whiplash',4).items()))
    print(sorted(near2('whiplash',5).items()))
    print(sorted(near2('whiplash',6).items()))
    print(sorted(near2('whiplash',7).items()))
    


    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
