#Kevin Luu 48783106 Lab 1
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query

def all_prefixes(fq : (str,)) -> {(str,)}:
    return {fq[:i] for i in irange(len(fq))}

#print(all_prefixes(('u','m', 'c')))

def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    {prefix[item].update({new_query}) for item in all_prefixes(new_query)}
    query[new_query] +=1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    pre = defaultdict(set)
    que = defaultdict(int)
    for beta in open_file:
        new= tuple(beta.rstrip('\n').split(' '))
        add_query(pre, que, new)
    return (pre, que)
           
#print(read_queries(open('googleq0.txt', 'r')))
def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    queries = ""
    for key in sorted(d, key = key, reverse = reverse):
        queries += '  ' + (str((key))) + ' -> ' + str(d[key]) + '\n'
    return (queries)

#print (dict_as_str((read_queries(open('googleq0.txt', 'r')))[1], key = lambda x:read_queries(x)[1][1]))

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    if a_prefix in prefix.keys():
        x = sorted((prefix[a_prefix]), key = lambda x: query[x], reverse = True)[:n]
        return x
    else:
        return []

if __name__ == '__main__':
    while True:
        try:
            opening = input('Enter name of file with full queries:')
            searches = read_queries(open(opening, 'r'))
            print("Prefix dictionary:")
            print (dict_as_str((searches[0]),  key = lambda x: len(read_queries(x)[0][1]), reverse = True))
            print ("Query dictionary:")
            print (dict_as_str((searches[1]), key = lambda x:read_queries(x)[1][1], reverse = True))
        except:
            print("Try another file")
        else:
            break
    while True:
        try:
            delta = input("Enter prefix (or quit):")
            if (delta) == 'quit':
                break
            print("Top 3 (at most) full queires = " + str((top_n(str(ask,), 3, prefix = (searches[0]), query = (searches[1])))))
            second_input = input("Enter full query (or quit)")
            if second_input == 'quit':
                break
            add_query(read_queries(open(opening, 'r'))[0], read_queries(open(opening, 'r'))[1], (second_input,))
            print("Prefix dictionary:")
            print (dict_as_str((searches[0]),  key = lambda x: len(read_queries(x)[0][1]), reverse = True))
            print ("Query dictionary:")
            print (dict_as_str((searches[1]), key = lambda x:read_queries(x)[1][1], reverse = True))
        except:
            print ("Failure")
        else:
            break
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
