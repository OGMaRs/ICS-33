# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, tuple, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.
#Kevin Luu 48783106
def hide(iterable):
    for v in iterable:
        yield v


def running_count(iterable,p):
    occuerence = 0
    for letter in iterable:
        if p(letter):
            occuerence += 1
        yield occuerence

        
def once_in_a_row(iterable):
    previous = None
    for item in (iterable):
        if item != previous:
            previous = item
            yield item
        else:
            previous = item


def group(iterable,n):
    counter = 0
    final = []
    for item in iterable:
        final.append(item)
        counter += 1
        if counter == n:
            yield final
            final = []
            counter = 0
               
def overlap(word, n, m=1):
    it = iter(word)
    window = [next(it) for i in range(n)] 
    yield window
    for letter in it:
        window[:-m] = window[m:]
        secondary = window[:-m]
        secondary.append(letter)
        for times in range(m - 1):
            secondary.append(next(it))
        window = secondary
        yield secondary
            
        
def sequence(*args):
    for arguments in args:
        for thing in arguments:
            yield thing
                    
def alternate(*args):
    iterables = []
    for element in args:
        iterables.append(iter(element))
    while True:
        for item in iterables:
            yield item.__next__()

                

if __name__ == '__main__':
    print('Testing running_count')
    for i in running_count('bananastand',lambda x : x in 'aeiou'):
        print(i,end=' ')
    print()
    for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'):
        print(i,end=' ')
    print()
    
    
    print('\nTesting once_in_a_row')
    for i in once_in_a_row('abbbcdefffaabccf'):
        print(i,end=' ')
    print()
    for i in once_in_a_row(hide('abbbcdefffaabccf')):
        print(i,end=' ')
    print()
    
    
    print('\nTesting group')
    for i in group('abcdefghijk',3):
        print(i,end=' ')
    print()
    for i in group(hide('abcdefghijk'),3):
        print(i,end=' ')
    print()
    
    
    print('\nTesting overlap')
    for i in overlap('abcdefghijk',4,2):
        print(i,end=' ')
    print()
    for i in overlap(hide('abcdefghijk'),4,2):
        print(i,end=' ')
    print()
    
    
    print('\nTesting sequence')
    for i in sequence('abcde','fg','hijk'):
        print(i,end=' ')
    print()
    for i in sequence(hide('abcde'),hide('fg'),hide('hijk')):
        print(i,end=' ')
    print()
    
    
    print('\nTesting alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end=' ')
    print()
    for i in alternate(hide('abcde'),hide('fg'),hide('hijk')):
        print(i,end=' ')
    print()
    
    print()
    #driver tests
    import driver
    driver.default_file_name = 'bsc3.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
