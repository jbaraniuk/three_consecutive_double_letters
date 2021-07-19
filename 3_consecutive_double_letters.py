#Justin Baraniuk 
#February 2, 2021

def three_consecutive_double_letters(word):
    i = 0
    count = 0
    while i+5 < len(word)-1:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
        else:
            i += 1
    return False

    
fin = open('words.txt')

for line in fin:
    word = line.strip()
    if three_consecutive_double_letters(word) == True:
        print(word)
