#These are some functions for word processing
# Function to check if canidate word is in target word. returns true/false
def wordinword(canidate, target):
    if len(canidate) > len(target):
        return False
    tmp_target = list(target)
    for x in canidate:
        if x not in tmp_target:
            return False
        else: 
            tmp_target.remove(x)
    return True
# function argument is word list(dictionary), and word(the word). returns a list of all the possible words
def return_all_words(allwords, word)
    for all in allwords:
        if all == None or all == "" or all==" ":
            continue
                word2 = word
                betalist = list(word)
                betalist = sorted(betalist)
                check = True
                usedletters = []
                if wordinword(word, jumble) == True:
                    poswords.append(all)
                    possiblewords+=1
                return poswords
