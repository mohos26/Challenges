# https://edabit.com/challenge/f48nSAebxBNMfmc9D
# 30.06.2025
# Very Hard

def scrambled(words, mask):
    res = []
    for word in words:
        if len(word) == len(mask):
            for word_letter, mask_letter in zip(word, mask):
                if mask_letter != '*' and mask_letter != word_letter:
                    break
            else:
                res.append(word)
    return sorted(res)
