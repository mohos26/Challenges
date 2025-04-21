# https://edabit.com/challenge/Q72X3J8jq7SzSSXui
# 27.10.2024
# Hard

def sentence_searcher(txt, word):
    for phrase in txt.split('.'):
        if word.lower() in phrase.lower():
            return phrase.strip() + '.'
    return ''

