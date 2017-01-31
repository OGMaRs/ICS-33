#Kevin Luu 48783106 Lab 1
import goody
from collections import defaultdict

def read_fa(file : open) -> {str:{str:str}}:
    nums = defaultdict(set)
    tran  = ((file).read()).split('\n')
    for i in range(len(tran)):
        other = tran[i].split(';')
        x = zip((other[1:len(other):2]),(other[2:len(other):2]))
        nums[other[0]] = ({item[0]: item[1]  for item in list(x)})   
    return (dict(nums))           

def fa_as_str(fa : {str:{str:str}}) -> str:
    s = ""
    for key in sorted(fa.keys()):
        s += '  ' + (str(key)) +' transitions: ' + str(sorted(list((fa[key].items())))) + '\n'
    return (s)

def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    end_game = []
    end_game.append(state)
    for change in inputs:
        if change in fa[state].keys():
            keys = fa[state]
            end_game.append((change, keys[change]))
            state = keys[change]
        else:
            end_game.append((change, None))
            break
    return end_game

def interpret(fa_result : [None]) -> str:
    print("Starting new simulation")
    results = ""
    results += "Start state = " + str(fa_result[0]) + '\n'
    for item in fa_result[1:len(fa_result)]:
        if item[1] == None:
            results += '  Input = ' +item[0] +'; ' + 'illegal input: simulation terminated' + '\n'
        else: 
            results += '  Input = ' +item[0] +'; ' + 'new state = ' + item[1] + '\n'
    results += 'Stop state = ' + str(fa_result[-1][-1]) + '\n' 
    return results


if __name__ == '__main__':
    while True:
        try:
            file = input('Enter file with finite automaton:')
            FA = read_fa(open(file, 'r'))
            print ('Finite Automation')
            print (fa_as_str(FA))
        except:
            print("Try another file")
        else:
            break
    while True:
        try:
            changies = input('Enter file with start-state and input:')
            secondary = open(changies, 'r').read().split('\n')
            for i in range(len(secondary)):
                states = secondary[i].split(';')
                begin = states[0]
                rest = states[1:len(states)]
                print(interpret(process(FA, begin,rest)))
        except:
            print("Try another file")
        else:
            break
        
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
