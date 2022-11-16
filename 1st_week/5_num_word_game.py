""" 1번째 시도

def solution(s):

    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for w in word:

        if w in s:
        
            s.replace('zero','0')
            s.replace('one','1')
            s.replace('two','2')
            s.replace('three','3')
            s.replace('four','4')
            s.replace('five','5')
            s.replace('six','6')
            s.replace('seven','7')
            s.replace('eight','8')
            s.replace('nine','9')
    
    return print(s)
"""

""" 2번째 시도

def solution(s):

    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for w in word: 
        if w in s:
            answer = s.replace(w, str(word.index(w)))
          
            
    return print(int(answer))

"""

def solution(s):

    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for w in word: 
   
        answer = s.replace(w, str(word.index(w)))
        s = answer 
     
    return int(answer)
