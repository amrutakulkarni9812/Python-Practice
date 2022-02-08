"""
want you to write me a simple spell checking engine.
The query language is a very simple regular expression-like language, with one special character: . (the dot character), which means EXACTLY ONE character (it can be any character). So, for example, 'c.t' would match 'cat' as the dot matches any character. There may be any number of dot characters in the query (or none).
Your spell checker will have to be optimized for speed, so you will have to write it in the required way. There would be a one-time setUp() function that does any pre-processing you require, and then there will be an isMatch() function that should run as fast as possible, utilizing that pre-processing.
"""


def spellcheck(word, lst):
    if len(word) not in [len(x) for x in lst]:
        return False
    elif word in lst:
        return True
    else:
        lst1 = [x for x in lst if len(x) == len(word)]
        for z in lst1:
            c = 0
            for i in range(len(word)):
                if word[i] == z[i] and word[i] != '.':
                    c += 1
            if len(word) - word.count('.') == c:
                return True
    return False


print(spellcheck('c.t', ['cot', 'abcd']))
