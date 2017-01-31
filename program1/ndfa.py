#Kevin Luu 48783106 Lab 1

import goody
from collections import defaultdict
    
def read_ndfa(file : open) -> {str:{str:{str}}}:
    final = defaultdict(set)
    cut  = ((file).read()).split('\n')
    for i in range(len(cut)):
        inside = cut[i].split(';')
        x = zip((inside[1:len(inside):2]),(inside[2:len(inside):2]))
        final[inside[0]] = ({item[0]: {item[1]} for item in list(x)})
        z = zip((inside[1:len(inside):2]),(inside[2:len(inside):2]))
        for val in list(z):
            for ab in range(len(final.keys())):
                if val[0] in final[inside[ab]]:
                    final[inside[ab]][val[0]].update({val[1]})
                break
    return (dict(final))

#print (read_ndfa(open('ndfaendin01.txt', 'r')))


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    eval = ""
    for key,val in sorted(ndfa.items()):
        eval += '  ' + str(key) + ' transitions: ' + str(sorted(list(zip((val),[sorted(list(c)) for c in val.values()])))) + '\n'
    return eval

#print (ndfa_as_str((read_ndfa(open('ndfaendin01.txt', 'r')))))   
       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    final = [state]
    testing = {state}
    x = set()
    for num in inputs:
        for status in testing:
            if num in ndfa[status]:
                x.update(ndfa[status][num])
        final.append((num,set(x)))
        testing = {}
        testing = (x)
        x = set()
    return final
            
   
#print(process(read_ndfa(open('ndfaendin01.txt', 'r')), state = 'start', inputs = ['1','0','1','1','0','0']))

def interpret(result : [None]) -> str:
    print("Starting new simulation")
    to_print = ""
    to_print += "Start state = " + str(result[0]) + '\n'
    for values in result[1:len(result)]:
        if values[1] != None:
            to_print += '  Input = ' +str(values[0]) +'; ' + 'new possible states = ' + str(sorted((list(values[1])))) + '\n'
        else:
            to_print += '  Input = ' +str(values[0]) +'; ' + 'illegal input: simulation terminated' + '\n'
    to_print += 'Stop state(s) = ' + str(sorted(list(result[-1][-1]))) + '\n' 
    return to_print


if __name__ == '__main__':
    while True:
        try:
            file = input(' Enter file with non-deterministic finite automaton:')
            ndfa = read_ndfa(open(file, 'r'))
            print (ndfa_as_str(ndfa))
        except:
            print("Enter a valid file")
        else:
            break
    while True:
        try:
            input_files = input(" Enter file with start-state and input:")
            commands = open(input_files, 'r').read().split('\n')
            for i in range(len(commands)):
                splits = commands[i].split(';')
                start = splits[0]
                end = splits[1:len(splits)]
                print(interpret(process(ndfa, start,end)))
        except:
            print("Try another file")
        else:
            break
            
    # For running batch self-tests
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
