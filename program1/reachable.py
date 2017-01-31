#Kevin Luu 48783106 Lab 1 Problem 1
from collections import defaultdict

def read_graph(file : open) -> {str:{str}}:
    transformed = defaultdict(set)
    new  = ((file).read()).split('\n')
    transformed = {new[i][0] : {new[i][2]} for i in range(len(new))}
    x = {transformed[new[i][0]].update({new[i][2]}) for i in range(len(new)) if new[i][0] in transformed}
    return (transformed)


def graph_as_str(graph : {str:{str}}) -> str:
    string = ""
    for key,value in sorted(graph.items()):
        string += '  ' + (str(key) + ' -> ' + str(sorted(list(value))) + '\n')
    return (string)

def reachable(graph : {str:{str}}, start : str) -> {str}:
    explore = [start]
    reached = set()
    while len(explore) > 0:
        for i in range(len(explore)):
            if explore[0] in reached:
                explore.pop(0)
                break
            reached.update(explore[i])
            explore.extend(list(graph.get(explore[i], explore.pop(i))))
    return (reached)
        

if __name__ == '__main__':
    while True:
        try:
            file = (input('Enter file with graph:'))
            print(graph_as_str(read_graph((open(file, 'r')))))
        except:
            print ("Try another file name")
        else:
            print('Graph: source -> {destination} edges')
            break
    while True:
        start = input(' Enter starting node name:').lower()
        if start == 'quit':
            break
        if start not in read_graph(open(file, 'r')):
            print ( 'Entry Error:'+ str(start) + ';  Illegal: not a source node Please enter a legal String')
        else:
            print('From ' + str(start) + ' the reachable nodes are ' + str(reachable(read_graph(open(file, 'r')),start)))
        break
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()  


            
            
                
            
     
     
    
    





