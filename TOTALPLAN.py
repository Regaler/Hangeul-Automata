#-*- coding: utf-8 -*-
import MealyMachine
import sys
import Chain

f_mm = open(sys.argv[1], "r")
mealy = MealyMachine.makeMealyMachine(f_mm)

val = raw_input("Please enter alphabets: ")
val = val.strip()
arr = val.split('<')
chain = list(arr[0])
backspace = len(arr) - 1

mealy.initialize()
effectiveness, MMoutput = MealyMachine.isSentence(mealy, chain)
MMoutput = list(MMoutput)

if effectiveness == True:
    #chain = Chain.hangeulize_chain(chain)
    #print "MMoutput: ", MMoutput
    #print "chain: ", chain
    #print("VALID!!!!!")
    
    marked_chain = Chain.position_marker(chain, MMoutput)	# rhkwkfmfajrwk->r1h2k2w1k2f1m2f3a1j2r3w1k2
    #print "marked_chain: ", marked_chain
    codonized_chain = Chain.codonize(marked_chain)			# [r1h2k2][w1k2][f1m2f3][a1j2r3][w1k2]
    processed_codonized_chain = Chain.process_del(codonized_chain,backspace)
    letterized_chain = Chain.letterize_chain(processed_codonized_chain)	# ['과','자','를','먹','자']
    #print letterized_chain
    Chain.sentence_printer(letterized_chain)					# >> 과자를먹자
else:
    print("Invalid Hangeul")

f_mm.close()
