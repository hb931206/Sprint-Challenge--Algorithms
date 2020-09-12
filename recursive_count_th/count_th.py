'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    wl = len(word)
    thL = 2

    if wl == 0:
        return 0
    if word[0:thL] == "th":
        return count_th(word[thL-1:])+1
    return count_th(word[thL-1:])

    # inputs are a word
    # outputs are number of occurences of "th"
    # Has to utilize reccurision

    # CASES
    # if there's a 'th'
    # if the word parameter is empty
    # if its 'Th' or 'hT'
