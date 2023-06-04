with open('Google.txt', 'r') as f:
    dictionary = f.read().split('\n')[:-1]

with open('stego_text.txt', 'r') as f:
    mispelled = f.read().split('\n')[:-1]

response = ''
for word in mispelled:
    char = ''
    match = 0
    potential = ''
    for correct in dictionary:
        len_word = len(word)
        if len_word == len(correct):
            errors = sum([mispelled_c != correct_c for mispelled_c, correct_c in zip(word, correct)])
            if errors == 0:
                match = 0
                break
            elif errors == 1:
                potential = correct
                match += 1
            if match > 1:
                break
    if match == 1:
        for mispelled_c, correct_c in zip(word, potential):
            if mispelled_c != correct_c:
                print(mispelled_c, end='')
