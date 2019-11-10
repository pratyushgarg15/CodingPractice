"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
"""

def returnSentence(d, string):
    l = []
    auxString = ""

    for i in range(len(string)):
        auxString += string[i] 
        if(auxString in d):
            if(auxString not in l):
                l.append(auxString)
                auxString = "" 
                
    return l            

if __name__ == '__main__':
    d = {'snake':0, 'snakes':0, 'sand': 0, 'and':0, 'ladder':0 }
    string = "snakesandladder"
    
    print(returnSentence(d, string))