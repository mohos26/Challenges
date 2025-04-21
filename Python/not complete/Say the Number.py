# https://edabit.com/challenge/im47j9ax22Z5MgqvW
# Expect
# 1.2.2023


def alphabetical_number(num):
    num = int(num)
    d = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
         10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
         17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    dd = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
          9: "ninety"}
    t = []
    if num < 20:
        return d[num]
    else:
        if len(str(num)) == 3:
            t.append(d[int(str(num)[0])] + ' hundred')
            if int(str(num)[-2:]) > 0:
                t[0] += ' and'
        if int(str(num)[-2]) > 0:
            if int(str(num)[-2:]) < 20:
                t.append(d[int(str(num)[-2:])])
                return ' '.join(t)
            else:
                t.append(dd[int(str(num)[-2])])
        if int(str(num)[1]) > 0:
            t.append(d[int(str(num)[-1])])
    return ' '.join(t)


def say_the_number(num):
    num = str(num)
    for i in range(1, (len(num) - 1) // 3 + 1):
        num = num[:-4 * i + 1] + '.' + num[-4 * i + 1:]
    num = num.split('.')
    t = []

    for i in range(1, len(num) + 1):
        if i == 1:
            t.append(alphabetical_number(num[-i]))
        elif i == 2:

            if num[-i] == 1:
                t.append('a thousand')
            else:
                t.append(alphabetical_number(num[-i]) + ' thousand')
        elif i == 3:
            t.append(alphabetical_number(num[-i]) + ' million')
        elif i == 4:
            t.append(alphabetical_number(num[-i]) + ' billion')
        elif i == 5:
            t.append(alphabetical_number(num[-i]) + ' trillion')
        else:
            return ValueError
    return (', '.join(t[::-1]) + '.').capitalize()



