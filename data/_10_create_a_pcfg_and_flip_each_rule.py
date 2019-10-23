# 10/20: Create a Probabilistic Context-Free Grammar and flip each rule

# Learn a PCFG to describe the input string. Then take the 
# rules and flip each rule's right-hand side. 
# Parse candidates for reverse versions, output the one with 
# the highest probability.

import nltk
import random

def build_tree(word, level):
    if len(word) == 1:
        if word.lower() in "aeiouäöü":
            return "(V{} {})".format(level, word)
        return "(C{} {})".format(level, word)
    return "(N{} {} {})".format(level, 
                                build_tree(word[0], level), 
                                build_tree(word[1:], level+1))

def pcfg_reverse(word):
    s = build_tree(word, 0)
    tree = nltk.Tree.fromstring(s)
    productions = tree.productions()
    for p in productions:
        
        ##################################################
        # !!! THIS IS WHERE THE MAGIC HAPPENS !!!        #
        if len(p._rhs) > 1:                              #
            p._rhs = (p._rhs[1], p._rhs[0])              #
            ##############################################
            
    grammar = nltk.induce_pcfg(nltk.Nonterminal("N0"), productions)
#     print(grammar)     # UNCOMMENT FOR A FUN TIME!
    parser = nltk.pchart.InsideChartParser(grammar)
    
    # Shuffle to generate 1000 possible words; only the correct
    # solution will be parseable with our grammar!
    for i in range(1000):
        cand = random.sample(word, len(word))
#         print(cand)               # UNCOMMENT FOR A FUN TIME!
        parser.parse(cand)
        for parse in parser.parse(cand):
            if parse._ProbabilisticMixIn__prob > 0:
#                 print("number of tries: {}".format(i))  # UNCOMMENT!
                return "".join(cand)
    return "no reverse found, try again"

print(pcfg_reverse("whyyy"))