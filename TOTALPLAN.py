#-*- coding: utf-8 -*-
import DFA
import os
import sys

f_dfa = open(sys.argv[1], "r")
dfa = DFA.makeDFA(f_dfa)

val = raw_input("Please enter alphabets: ")
chain = val.strip()

dfa.initialize()
effectiveness = DFA.isSentence(dfa, chain)

if effectiveness == True:
	chain = list(chain)
	print("VALID!!!!!")
	"""
	marked_chain = position_marker(chain)				# rhkwkfmfajrwk->r1h2k2w1k2f1m2f3a1j2r3w1k2
	codonized_chain = codonize(marked_chain)			# [r1h2k2][w1k2][f1m2f3][a1j2r3][w1k2]
	letterized_chain = letterize_chain(codonized_chain)	# ['과','자','를','먹','자']
	sentence_printer(letterized_chain)					# >> 과자를먹자
	"""
else:
	print("Invalid Hangeul")

f_dfa.close()


# Functions used
def position_marker(chain):
	"""Gets a chain, outputs the mareked chain"""
	marked_chain = []
    for index, current in enumerate(chain):
    	if index < len(chain) - 1:
    		next_ = current[index + 1]
    	# Black? Red? Blue?	
        if current == Black:
        	current.position = 1
            continue
        elif current == Red:
            marked_chain.append([current,2])
            if next_ == Red:
                    next_.position = 2
                    marked_chain.append([])
                    continue
            elif next_ == Blue:
                    next_.position = 3
                    continue
        elif current == Blue:
            if next_ = Black:
                    current.position = 3
                    next_.position = 1
                    continue
            elif next_ = Red:
                    current.position = 1
                    next_.position = 2
                    continue
            elif next_ = Blue:
                    current.position = 3
                    next_.position = 3
                    continue
	return marked_chain

def codonize(marked_chain):
	"""Gets a marked_chain, outputs the codonized chain"""
	return 2

def codon_merge(codon):
	"""Gets single codon, outputs the merged form, namely the letter"""
	return 2

def letterize_chain(codonized_chain):
	"""Gets codonized_chain, outputs the letterized chain"""
	return 2

def sentence_printer(letterized_chain):
	"""Gets letterized_chain, outputs the correct hangeul sentence"""
	return 2