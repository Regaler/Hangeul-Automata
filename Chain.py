#-*- coding: utf-8 -*-
# Functions used
import sys

def position_marker(chain, MMoutput):
    """Gets a chain, outputs the mareked chain"""
    marked_chain = []
    Black = ['V']
    Red = ['O','U','A','I']
    Blue = ['K','N','F','L']
    for elem in chain:
        marked_chain.append([elem,0])
    
    for index, current in enumerate(chain):
        #print current
        # Define next_
    	if index < len(chain) - 1:
    	    next_ = chain[index+1]
    	# Now test
        if MMoutput[index] in Black: # Black
            #print "It's black"
            marked_chain[index][1] = 1
            continue
        elif MMoutput[index] in Red: # Red
            #print "It's Red"
            marked_chain[index][1] = 2
            if index == len(chain) - 1:
                continue
            elif MMoutput[index+1] in Red:
                marked_chain[index+1][1] = 2
                continue
            elif MMoutput[index+1] in Blue:
                marked_chain[index+1][1] = 3
                continue
        elif MMoutput[index] in Blue: # Blue
            #print "It's Blue"
            if index == len(chain) - 1:
                continue
            elif MMoutput[index+1] in Black:
                marked_chain[index][1] = 3
                marked_chain[index+1][1] = 1
                continue
            elif MMoutput[index+1] in Red:
                marked_chain[index][1] = 1
                marked_chain[index+1][1] = 2
                continue
            elif MMoutput[index+1] in Blue:
                marked_chain[index][1] = 3
                marked_chain[index+1][1] = 3
                continue
        else:
            print "It's else"
    #print "This print statement works"
    return marked_chain

def codonize(marked_chain):
    """Gets a marked_chain, outputs the codonized chain"""
    codonized_chain = []
    codon = []
    for index, elem in enumerate(marked_chain):
        if index == len(marked_chain) - 1:
            codon.append(elem)
            codonized_chain.append(codon)
        elif index == 0:
            codon.append(elem)
        elif not (elem[1] == 1):
            codon.append(elem)
        elif (elem[1] == 1) and (not (index == 0)):
            codonized_chain.append(codon)
            codon = []
            codon.append(elem)
    return codonized_chain

def process_del(codonized_chain, backspace):
    processed_codonized_chain = codonized_chain
    last = codonized_chain[-1]
    if backspace < len(last):
        for i in range(backspace):
            processed_codonized_chain[-1].pop()
    elif backspace == len(last):
        processed_codonized_chain.pop()
    elif backspace > len(codonized_chain):
        processed_codonized_chain = []
    else:
        processed_codonized_chain.pop()
        for i in range(backspace - len(last)):
            processed_codonized_chain.pop()
    #print processed_codonized_chain
    return processed_codonized_chain

def codon_merge(codon):
    """Gets single codon, outputs the merged form, namely the letter"""
    first = [];second = [];third = []
    f = 0;s = 0;t = 0;order = 0;
    for elem in codon:
        if elem[1] == 1:
            first.append(elem[0])
        elif elem[1] == 2:
            second.append(elem[0])
        elif elem[1] == 3:
            third.append(elem[0])
        else:
            print "codon_merge error"
    #f
    if first[0] == 'r': f = 1       #ㄱ
    elif first[0] == 's': f = 3     #ㄴ
    elif first[0] == 'e': f = 4     #ㄷ
    elif first[0] == 'f': f = 6     #ㄹ
    elif first[0] == 'a': f = 7     #ㅁ
    elif first[0] == 'q': f = 8     #ㅂ
    elif first[0] == 't': f = 10    #ㅅ
    elif first[0] == 'd': f = 12    #ㅇ
    elif first[0] == 'w': f = 13    #ㅈ
    elif first[0] == 'c': f = 15    #ㅊ
    elif first[0] == 'z': f = 16    #ㅋ
    elif first[0] == 'x': f = 17    #ㅌ
    elif first[0] == 'v': f = 18    #ㅍ
    elif first[0] == 'g': f = 19    #ㅎ
    elif first[0] == 'R': f = 2     #ㄲ
    elif first[0] == 'T': f = 11    #ㅆ
    elif first[0] == 'E': f = 5     #ㄸ
    elif first[0] == 'Q': f = 9     #ㅃ
    elif first[0] == 'W': f = 14    #ㅉ
    #s
    if len(second) == 1:
        if second[0] == 'k': s = 1      #ㅏ
        elif second[0] == 'i': s = 3    #ㅑ
        elif second[0] == 'j': s = 5    #ㅓ
        elif second[0] == 'u': s = 7    #ㅕ
        elif second[0] == 'h': s = 9    #ㅗ
        elif second[0] == 'y': s = 13   #ㅛ
        elif second[0] == 'n': s = 14   #ㅜ
        elif second[0] == 'b': s = 18   #ㅠ
        elif second[0] == 'm': s = 19   #ㅡ
        elif second[0] == 'l': s = 21   #ㅣ
        elif second[0] == 'o': s = 2    #ㅐ
        elif second[0] == 'O': s = 4    #ㅒ
        elif second[0] == 'p': s = 6    #ㅔ
        elif second[0] == 'P': s = 8    #ㅖ
    elif len(second) == 2:
        if second[0] == 'h' and second[1] == 'k': s = 10   #ㅘ
        elif second[0] == 'h' and second[1] == 'o': s = 11   #ㅙ
        elif second[0] == 'h' and second[1] == 'l': s = 12   #ㅚ
        elif second[0] == 'n' and second[1] == 'j': s = 15   #ㅝ
        elif second[0] == 'n' and second[1] == 'p': s = 16   #ㅞ
        elif second[0] == 'n' and second[1] == 'l': s = 17   #ㅟ
        elif second[0] == 'm' and second[1] == 'l': s = 20   #ㅢ
    #t
    if len(third) == 0:
        t = 1
    elif len(third) == 1:
        if third[0] == 'r': t = 2       #ㄱ
        elif third[0] == 's': t = 5     #ㄴ
        elif third[0] == 'e': t = 8     #ㄷ
        elif third[0] == 'f': t = 9     #ㄹ
        elif third[0] == 'a': t = 17    #ㅁ
        elif third[0] == 'q': t = 18    #ㅂ
        elif third[0] == 't': t = 20    #ㅅ
        elif third[0] == 'd': t = 22    #ㅇ
        elif third[0] == 'w': t = 23    #ㅈ
        elif third[0] == 'c': t = 24    #ㅊ
        elif third[0] == 'z': t = 25    #ㅋ
        elif third[0] == 'x': t = 26    #ㅌ
        elif third[0] == 'v': t = 27    #ㅍ
        elif third[0] == 'g': t = 28    #ㅎ
    elif len(third) == 2:
        if third[0] == 'r' and third[1] == 'r': t = 3        #ㄲ
        elif third[0] == 'r' and third[1] == 't': t = 4      #ㄳ
        elif third[0] == 's' and third[1] == 'w': t = 6      #ㄵ
        elif third[0] == 's' and third[1] == 'g': t = 7      #ㄶ
        elif third[0] == 'f' and third[1] == 'r': t = 10     #ㄺ
        elif third[0] == 'f' and third[1] == 'a': t = 11     #ㄻ
        elif third[0] == 'f' and third[1] == 'q': t = 12     #ㄼ
        elif third[0] == 'f' and third[1] == 't': t = 13     #ㄽ
        elif third[0] == 'f' and third[1] == 'x': t = 14     #ㄾ
        elif third[0] == 'f' and third[1] == 'v': t = 15     #ㄿ
        elif third[0] == 'f' and third[1] == 'g': t = 16     #ㅀ
        elif third[0] == 'q' and third[1] == 't': t = 19     #ㅄ
        elif third[0] == 't' and third[1] == 't': t = 21     #ㅆ

    if f >= 1 and s == 0:
        if first[0] == 'r': f = 1       #ㄱ
        elif first[0] == 's': f = 4     #ㄴ
        elif first[0] == 'e': f = 7     #ㄷ
        elif first[0] == 'f': f = 9     #ㄹ
        elif first[0] == 'a': f = 17    #ㅁ
        elif first[0] == 'q': f = 18    #ㅂ
        elif first[0] == 't': f = 21    #ㅅ
        elif first[0] == 'd': f = 23    #ㅇ
        elif first[0] == 'w': f = 24    #ㅈ
        elif first[0] == 'c': f = 26    #ㅊ
        elif first[0] == 'z': f = 27    #ㅋ
        elif first[0] == 'x': f = 28    #ㅌ
        elif first[0] == 'v': f = 29    #ㅍ
        elif first[0] == 'g': f = 30    #ㅎ
        elif first[0] == 'R': f = 2     #ㄲ
        elif first[0] == 'T': f = 16    #ㅆ
        elif first[0] == 'E': f = 6     #ㄸ
        elif first[0] == 'Q': f = 13    #ㅃ
        elif first[0] == 'W': f = 19    #ㅉ
        order = 12592 + f
        #print unichr(order)
    else:
        order = 44032 + (f-1)*21*28 + (s-1)*28 + (t-1)
    return unichr(order)

def letterize_chain(codonized_chain):
    """Gets codonized_chain, outputs the letterized chain"""
    sentence = []
    for codon in codonized_chain:
        sentence.append(codon_merge(codon))
    return sentence

def sentence_printer(sentence):
    """Gets letterized_chain, outputs the correct hangeul sentence"""
    if len(sentence) == 0:
        return 2;
    for letter in sentence:
        sys.stdout.write(letter)
