from collections import defaultdict

def read_graph(file : open) -> {str:{str}}:
    transformed = defaultdict(dict)
    new  = (open(file, 'r').read()).split('\n')
    transformed = {new[i][0] : {new[i][2]} for i in range(len(new))}
    x = {transformed[new[i][0]].update({new[i][2]}) for i in range(len(new)) if new[i][0] in transformed}
    return dict(transformed)


def graph_as_str(graph : {str:{str}}) -> str:
    string = ""
    for node in graph:
        for value in graph[node]:
            string += (str(node) + ';' + str(value) + '\n')
    return (string)
        

        

def reachable(graph : {str:{str}}, start : str) -> {str}:
    explore = [start]
    reached = set()
    while len(explore) > 0:
        for i in range(len(explore)):
            if explore[0] in reached:
                explore.pop(0)
            else:
                reached.update(explore[i])
                explore.extend(list(graph.get(explore[i], explore.pop(i))))
    return (reached)

    
(reachable(read_graph('graph2.txt'),'a'))
