#this is needed wordfile = open("your file here", "r")
#file_data = wordfile.read()
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
# this function takes a string as the argument and returns a dictionary where the keys is the word and the value is the amount of times it appears in the given argument
def countwords(document):
    sentences = document 
    sentences = re.sub("[^A-Za-z -]","",sentences)
    allwords = []
    for token in nlp(sentences):
        if token.pos_ not in excluded_tags:
            allwords.append(token.text.lower())
    amount_dict = {i:allwords.count(i) for i in allwords}
    return amount_dict
