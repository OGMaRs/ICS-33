def test_number(val : int, state: str) -> bool:
    if state == "positive":
        return (val > 0) 
    elif state == "negative":
        return (val < 0) 
    if state == "even":
        return val % 2 == 0
    elif state == "negative":
        return val % 2 == 1

def display():
    word = input("Enter a word:")
    for letter in word:
        print (letter)
        
    
def square_list(num_list : list) -> int:
    for item in num_list:
        print (item ** 2)

def match_first_letter(letter: str, line: str) -> str:
    for word in line:
        if word[0] == letter:
            print (word)
def match_area_code(area: list, phone:list) -> str:
    for code in area:
        for num in phone:
            if code in num[1:4]:
                print (num)

def is_vowel(letter: str) -> bool:
    vowels = "aeiouAEIOU"
    return letter in vowels

def non_vowels(chars: str)->str:
    for letter in chars:
        if not is_vowel(letter):
            print (letter)

