#Kevin Luu 48783106 Lab 1

import goody
from collections import defaultdict

def read_voter_preferences(file : open)-> {str:[str]}:
    ballot = defaultdict(list)
    votes  = (file).read().split('\n')
    for i in range(len(votes)):
        new = votes[i].split(';')
        ballot[new[0]] = list((new[1:len(votes[i])]))
    return dict(ballot)

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    thingie = ""
    for key in sorted(d.keys(), key = key, reverse = reverse):
        thingie += '  ' + (str(key)) + ' -> ' + str((d[key])) + '\n'
    return (thingie)


#print (dict_as_str(read_voter_preferences('votepref1.txt')
    
def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    counting = defaultdict(int)
    for value in vp.values():
        for i in range(len(value)):
            if value[i] in cie:
                counting[value[i]] += 1
                break
    return dict(counting)

#print (evaluate_ballot(read_voter_preferences('votepref1.txt'), {'X',"Y", "Z"}))    

def remaining_candidates(vd : {str:int}) -> {str}:
    loser = min(vd, key = vd.get, default = 99999)
    return {c for c in vd.keys() if vd[c] > vd[loser]}

def run_election(vp_file : open) -> {str}:
    ballot = read_voter_preferences(vp_file)
    alpha = set((list(ballot.values())[0]))
    print ("Voter Prefrences")
    print(dict_as_str(ballot))
    counter = 1
    while len(remaining_candidates(evaluate_ballot(ballot, set(alpha)))) >= 0:
        print ("Vote count on ballot #" + str(counter) + ' with candidates (alphabetically) ' + '{' + str(sorted(list(alpha))).strip('[]') +'}')
        print(dict_as_str((evaluate_ballot(ballot,set(alpha)))))
        print ("Vote count on ballot #" + str(counter) + ' with candidates (numerically) ' + '{' + str(sorted(list(alpha), key = lambda x : ((evaluate_ballot(ballot,set(alpha)))[x]), reverse = True)).strip('[]') +'}')
        print(dict_as_str((evaluate_ballot(ballot, set(alpha))), key = lambda x: (x[0]), reverse = True ))
        alpha = (remaining_candidates(evaluate_ballot(ballot, set(alpha))))
        counter += 1
        if len(alpha) == 0:
            print ("No winner")
            break
        elif len(alpha) == 1:
            print ("Winner is "+ (str(alpha)))
            break
    return (alpha)
#run_election('votepref1.txt')

    
if __name__ == '__main__':
    while True:
        try:
            vp_file = input('Enter file with voter preferences')
            run_election(open(vp_file, 'r'))
        except:
            print ("Try another file")
        else:
            break          
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
